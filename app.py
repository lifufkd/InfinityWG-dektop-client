##########################
#       Created By       #
#          SBR           #
##########################
import sys

from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentTranslator
from PySide6.QtCore import QLocale

from utilities.UI.config import Config
from API.Requests import Authorization
from UI.main import App
##########################

##########################


def start_gui() -> None:
    app = QApplication(sys.argv)
    app.installTranslator(FluentTranslator(QLocale()))  # TODO: Change to config load method
    window = App(authorization, authorization.check_token()["status"])
    app.exec()


if __name__ == '__main__':
    config = Config()
    authorization = Authorization(config)
    start_gui()
    