##########################
#       Created By       #
#          SBR           #
##########################
import os

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon
from UI.pages.home.UI_home import Ui_Home
from utilities.network import get_ip_address, get_country_by_ip
from utilities.ui import SelectCountryMessageBox
from API.Requests import VPN
from utilities.schedule import TaskScheduler
##########################

##########################


class Home(Ui_Home, QWidget):

    def __init__(self, vpn: VPN, scheduler=TaskScheduler, parent=None):
        super().__init__(parent=parent)
        self._vpn = vpn
        self._scheduler = scheduler
        self.setupUi(self)
        self.ChooseServerButton.setIcon(FluentIcon.UPDATE)
        self.ChooseServerButton.clicked.connect(self.select_country)
        self.update_country_and_ip()

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
            self._vpn.set_country(selected_country)
            self.update_country_and_ip()
