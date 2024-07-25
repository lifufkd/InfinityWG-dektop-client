##########################
#       Created By       #
#          SBR           #
##########################
import sys
from PySide6.QtCore import Qt, QLocale
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentTranslator, setTheme, Theme, SplitTitleBar, isDarkTheme
from UI.pages.login.UI_login import Ui_Login
from utilities.UI.utilities import isWin11, select_window
from UI.pages.registration.registration import RegistrationWindow
from resources.vars import APP_NAME

##########################

##########################


Window = select_window()


class LoginWindow(Window, Ui_Login):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        setTheme(Theme.AUTO)

        self._startup = True
        self._registration_page = None
        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()
        self.LoginImage.setScaledContents(False)
        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon("../resources/images/logo.svg"))
        self.resize(1280, 720)

        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=isDarkTheme())
        if not isWin11():
            color = QColor(25, 33, 42) if isDarkTheme() else QColor(240, 244, 249)
            self.setStyleSheet(f"LoginWindow{{background: {color.name()}}}")

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
        self.RegistrationpushButton.clicked.connect(self.open_registration_page)

    def open_registration_page(self):
        if self._startup:
            self._registration_page = RegistrationWindow(self)
            self._startup = False
        self._registration_page.show()
        self.hide()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap("../resources/images/login_background.jpg").scaled(
            self.LoginImage.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.LoginImage.setPixmap(pixmap)