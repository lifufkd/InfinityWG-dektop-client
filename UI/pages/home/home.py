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
from modules.ui import SelectCountryMessageBox, createWarningInfoBar
from API.Requests import VPN
from modules.schedule import TaskScheduler
from modules.wireguard import WireGuard
from modules.ui import wg_status_notify, thread_handler
##########################

##########################


class Home(Ui_Home, QWidget):
    info_bar_signal = Signal(str, str, str, object)
    logout_signal = Signal()

    def __init__(self, vpn: VPN, scheduler: TaskScheduler, wireguard: WireGuard, parent=None):
        super().__init__(parent=parent)
        self._vpn = vpn
        self._scheduler = scheduler
        self._wireguard = wireguard
        self.connected = False

        self.setupUi(self)
        self.ChooseServerButton.setIcon(FluentIcon.UPDATE)

        self.info_bar_signal.connect(self.info_bar_handler)
        self.ChooseServerButton.clicked.connect(self.select_country)
        self.ConnectBtn.clicked.connect(self.connect_wg)
        self.ChangeIpBtn.clicked.connect(self.new_connection_wg)

        self.update_country_and_ip()

    @Slot(str, str, str, object)
    def info_bar_handler(self, title, text, type, parent):
        match type:
            case "info":
                pass
            case "warning":
                createWarningInfoBar(title=title,
                                     content=text,
                                     parent=parent)
                return True

    def new_connection_wg(self):
        self._scheduler.add_task(task_name="wg_update_config", task=self._new_connection_wg)

    def connect_wg(self):
        self._scheduler.add_task(task_name="wg_connector", task=self._connect_wg)

    def update_country_and_ip(self):
        self._scheduler.add_task(task_name="ip_updater", task=self._update_country_and_ip)

    def process_logout(self):
        self._scheduler.remove_task("token_check")
        self.logout_signal.emit()

    def _connect_wg(self, stop_callback, config: str | None = None, recovery: bool | None = None):
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

        internet_connection_status = self._update_country_and_ip(None)
        if recovery:
            self.process_logout()
        elif not internet_connection_status and self.connected:
            self._vpn.set_country_config("Auto")
            if not self._new_connection_wg(None, recovery=True):
                self.process_logout()
        elif not internet_connection_status and not self.connected:
            self.process_logout()

    def _update_country_and_ip(self, stop_callback) -> bool:
        current_country = get_country_by_ip()
        current_ip_address = get_ip_address()
        if not current_ip_address["status"] or not current_country["status"]:
            self.info_bar_signal.emit("Error", current_ip_address["detail"],
                                      "warning", self)
            return False
        self.CurrentIPText.setText(current_ip_address["data"])
        self.CurrentCountryText.setText(current_country["data"])
        ico_path = f"resources/country_flags/{current_country['data']}.ico"
        if os.path.exists(ico_path):
            self.CountryIcon.setIcon(ico_path)
        else:
            self.CountryIcon.setIcon(None)
        return True

    def _new_connection_wg(self, stop_callback, recovery: bool | None = None):
        while True:
            status = self._vpn.get_wg_config(country=self._vpn.get_country_config())
            if "data" not in status:
                self.info_bar_signal.emit("Error", status["detail"], "warning", self)
                return False
            elif not status["status"]:
                methods = [self._vpn.update_best_vpn_address, self._vpn.update_best_vpn_countries]
                if status["data"]["code"] in range(2):
                    _status = methods[status["data"]["code"]]()
                    if not _status["status"]:
                        self.info_bar_signal.emit("Error", f"Error getting config - {status['data']['detail']}",
                                                  "warning", self)
                        return False
                    continue
                else:
                    self.info_bar_signal.emit("Error", f"Error getting config - {status['data']['detail']}",
                                              "warning", self)
                    return False
            else:
                if self.connected:
                    self._connect_wg(None)
                self._connect_wg(None, config=status["data"]["config"], recovery=recovery)
                return True

    def select_country(self):
        w = SelectCountryMessageBox(vpn=self._vpn, parent=self)
        if w.exec():
            selected_country = w.country_combo_box.currentText()
            self._vpn.set_country_config(selected_country)
            self.new_connection_wg()
