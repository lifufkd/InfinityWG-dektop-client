##########################
#       Created By       #
#          SBR           #
##########################
import os

from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon
from UI.pages.home.UI_home import Ui_Home
from utilities.network import get_ip_address, get_country_by_ip
from utilities.ui import SelectCountryMessageBox, createWarningInfoBar
from API.Requests import VPN
from utilities.schedule import TaskScheduler
from utilities.wireguard import WireGuard
from utilities.system import send_notification
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
        self._scheduler.add_task("ip_updater", self.update_country_and_ip, 2000)

    def new_connection_wg(self, config: str):
        self._wireguard.connect()

    def connect_wg(self):
        self._scheduler.stop_task("wg_connector")
        self._scheduler.add_task("wg_connector", self._connect_wg)

    def _connect_wg(self):
        if self.connected:
            self._wireguard.disconnect()
            self.connected = False
            self.ConnectBtn.setText("Connect")
            notification_text = "WireGuard tunnel successfully disconnected"
        else:
            self._wireguard.connect()
            self.connected = True
            self.ConnectBtn.setText("Disconnect")
            notification_text = "WireGuard tunnel successfully connected"
        notify = send_notification(title="InfinityWG", text=notification_text)
        if not notify["status"]:
            createWarningInfoBar(title="Error", content=notify["detail"], parent=self)

    def update_country_and_ip(self):
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
