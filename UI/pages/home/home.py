##########################
#       Created By       #
#          SBR           #
##########################
import os
import time

from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon
from UI.pages.home.UI_home import Ui_Home
from utilities.network import get_ip_address, get_country_by_ip
from utilities.ui import SelectCountryMessageBox
from API.Requests import VPN
from utilities.schedule import TaskScheduler
from utilities.wireguard import WireGuard
from utilities.ui import wg_status_notify
##########################

##########################


class Home(Ui_Home, QWidget):

    def __init__(self, vpn: VPN, scheduler: TaskScheduler, wireguard: WireGuard, parent=None):
        super().__init__(parent=parent)
        self._vpn = vpn
        self._scheduler = scheduler
        self._wireguard = wireguard
        self.connected = False

        self.setupUi(self)
        self.ChooseServerButton.setIcon(FluentIcon.UPDATE)

        self.ChooseServerButton.clicked.connect(self.select_country)
        self.ConnectBtn.clicked.connect(self.connect_wg)

        self.update_country_and_ip()

    def new_connection_wg(self, config: str):
        self._wireguard.connect()

    def connect_wg(self):
        self._scheduler.add_task(task_name="wg_connector", task=self._connect_wg)

    def update_country_and_ip(self):
        self._scheduler.add_task(task_name="ip_updater", task=self._update_country_and_ip)

    def _connect_wg(self, stop_callback):
        if self.connected:
            self._wireguard.disconnect()
            self.connected = False
            self.ConnectBtn.setText("Connect")
        else:
            self._wireguard.connect()
            self.connected = True
            self.ConnectBtn.setText("Disconnect")
        wg_status_notify(connect_status=self.connected, parent=self)
        time.sleep(1)
        self._update_country_and_ip(None)

    def _update_country_and_ip(self, stop_callback):
        current_country = get_country_by_ip()
        self.CurrentIPText.setText(get_ip_address())
        self.CurrentCountryText.setText(current_country)
        ico_path = f"resources/country_flags/{current_country}.ico"
        if os.path.exists(ico_path):
            self.CountryIcon.setIcon(ico_path)
        else:
            self.CountryIcon.setIcon(None)

    def select_country(self):
        w = SelectCountryMessageBox(vpn=self._vpn, parent=self)
        if w.exec():
            selected_country = w.country_combo_box.currentText()
            self._vpn.set_country_config(selected_country)
            self.update_country_and_ip()
