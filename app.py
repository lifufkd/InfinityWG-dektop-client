##########################
#       Created By       #
#          SBR           #
##########################
import sys
import time

from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentTranslator
from PySide6.QtCore import QLocale

from utilities.config import Config
from utilities.schedule import TaskScheduler
from utilities.wireguard import WireGuard
from API.Requests import Authorization, VPN
from UI.main import App
##########################

##########################


def start_gui() -> None:
    app = QApplication(sys.argv)
    app.installTranslator(FluentTranslator(QLocale()))  # TODO: Change to config load method
    window = App(authorization=authorization,
                 scheduler=scheduler,
                 vpn=vpn,
                 wireguard=wireguard,
                 token_status=authorization.check_token()["status"])
    app.exec()


if __name__ == '__main__':
    config = Config()
    authorization = Authorization(config)
    vpn = VPN(config, authorization)
    wireguard = WireGuard()
    scheduler = TaskScheduler()
    start_gui()
    