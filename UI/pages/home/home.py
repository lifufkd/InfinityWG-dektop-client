##########################
#       Created By       #
#          SBR           #
##########################
import os
import time

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon
from UI.pages.home.UI_home import Ui_Home
from modules.network import get_ip_address, get_country_by_ip
from modules.ui import SelectCountryMessageBox, createWarningInfoBar, error_info_bar
from API.Requests import VPN
from modules.schedule import TaskScheduler
from modules.wireguard import WireGuard
from modules.ui import wg_status_notify
from modules.system import update_servers, country_serializer
##########################

##########################


class Home(Ui_Home, QWidget):
    info_bar_signal = Signal(str, str, str, object)

    def __init__(self, vpn: VPN, scheduler: TaskScheduler, wireguard: WireGuard, parent=None):
        super().__init__(parent=parent)
        self._vpn = vpn
        self._scheduler = scheduler
        self._wireguard = wireguard
        self._parent = parent
        self.connected = False

        self.setupUi(self)
        self.ChooseServerButton.setIcon(FluentIcon.UPDATE)

        self.info_bar_signal.connect(self.info_bar_handler)
        self.ChooseServerButton.clicked.connect(self.select_country)
        self.ConnectBtn.clicked.connect(self.connect_wg)
        self.ChangeIpBtn.clicked.connect(self.new_connection_wg)

    @Slot(str, str, str, object)
    def info_bar_handler(self, title, text, type, parent):
        match type:
            case "info":
                pass
            case "warning":
                createWarningInfoBar(title=title,
                                     content=text,
                                     parent=parent)
            case "error":
                error_info_bar(title=title,
                               content=text,
                               parent=parent)

    def new_connection_wg(self):
        self._scheduler.add_task(task_name="wg_update_config", task=self._new_connection_wg)

    def connect_wg(self):
        self._scheduler.add_task(task_name="wg_connector", task=self._connect_wg)

    def update_country_and_ip(self):
        self._scheduler.add_task(task_name="ip_updater", task=self._update_country_and_ip)

    def _connect_wg(self, stop_callback, config: str | None = None) -> bool:
        self.ConnectBtn.setEnabled(False)
        if self.connected:
            self._wireguard.disconnect()
            self.connected = False
            self.ConnectBtn.setText("Connect")
        else:
            self._wireguard.connect(config)
            self.connected = True
            self.ConnectBtn.setText("Disconnect")

        wg_status_notify(connect_status=self.connected, parent=self)
        time.sleep(1)
        _status = self._update_country_and_ip(None)
        self.ConnectBtn.setEnabled(True)
        return _status

    def _update_country_and_ip(self, stop_callback) -> bool:
        current_country = get_country_by_ip()
        current_ip_address = get_ip_address()
        if not current_ip_address["status"] or not current_country["status"]:
            self.info_bar_signal.emit("Error", current_ip_address["detail"],
                                      "warning", self._parent)
            return False
        self.CurrentIPText.setText(current_ip_address["data"])
        self.CurrentCountryText.setText(current_country["data"])
        ico_path = country_serializer("resources/country_flags", current_country["data"])

        if ico_path is not None:
            self.CountryIcon.setIcon(ico_path)
        else:
            self.CountryIcon.setIcon(None)
        return True

    def _new_connection_wg(self, stop_callback, server_quality: int = -1) -> bool:
        __status = bool
        counter = 0

        self.ChangeIpBtn.setEnabled(False)
        self.ChooseServerButton.setEnabled(False)
        while True:
            status = self._vpn.create_config_request(country=self._vpn.get_country_config(),
                                                     server_quality=server_quality)
            if "data" not in status:
                self.info_bar_signal.emit("Error", status["detail"], "warning", self._parent)
                __status = False
                break
            elif not status["status"]:
                if status["data"]["code"] in range(2):
                    _status = update_servers(self._vpn, status["data"]["code"])
                    if not _status:
                        self.info_bar_signal.emit("Error", f"Error getting config - {status['data']['detail']}",
                                                  "warning", self._parent)
                        __status = False
                        break
                    continue
                else:
                    self.info_bar_signal.emit("Error", f"Error getting config - {status['data']['detail']}",
                                              "warning", self._parent)
                    __status = False
                    break
            else:
                while True:
                    if counter >= 45:
                        self.info_bar_signal.emit("Warning", f"Riches timeout while waiting config",
                                                  "warning", self._parent)
                        __status = False
                        break
                    _status = self._vpn.get_config(request_id=status["data"]["request_id"])
                    if _status["status"]:

                        if self.connected:
                            self._connect_wg(None)

                        if self.isVisible():
                            __status = self._connect_wg(None, config=_status["data"]["config"])
                        else:
                            __status = self._wireguard.update_config(config=_status["data"]["config"])["status"]
                        break
                    counter += 1
                    time.sleep(2)
                break

        self.ChangeIpBtn.setEnabled(True)
        self.ChooseServerButton.setEnabled(True)
        return __status

    def select_country(self):
        w = SelectCountryMessageBox(vpn=self._vpn, parent=self._parent)
        if w.exec():
            selected_country = w.country_combo_box.currentText()
            self._vpn.set_country_config(selected_country)
            self.new_connection_wg()
