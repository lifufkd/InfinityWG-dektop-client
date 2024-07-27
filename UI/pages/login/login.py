##########################
#       Created By       #
#          SBR           #
##########################
import sys
import time

from PySide6.QtCore import Qt, QTimer, Signal
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtWidgets import QApplication
from qfluentwidgets import setTheme, Theme, SplitTitleBar, isDarkTheme
from UI.pages.login.UI_login import Ui_Login
from utilities.UI.utilities import isWin11, select_window, createWarningInfoBar, createSuccessInfoBar
from UI.pages.registration.registration import RegistrationWindow
from resources.vars import APP_NAME
from API.Requests import Authorization
##########################

##########################


Window = select_window()


class LoginWindow(Window, Ui_Login):
    sw_open_app = Signal()

    def __init__(self, authorization: Authorization):
        super().__init__()
        self.setupUi(self)
        setTheme(Theme.AUTO)

        self._startup = True
        self._registration_page = None
        self._authorization = authorization
        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()
        self.LoginImage.setScaledContents(False)
        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon("resources/images/logo.svg"))
        self.resize(1280, 720)

        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=isDarkTheme())
        if not isWin11():
            color = QColor(25, 33, 42) if isDarkTheme() else QColor(240, 244, 249)
            self.setStyleSheet(f"LoginWindow{{background: {color.name()}}}")

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
        self.LoginpushButton.clicked.connect(self.login)
        self.RegistrationpushButton.clicked.connect(self.open_registration_page)

    def login(self):
        login = self.LoginlineEdit.text()
        password = self.PasswordlineEdit.text()
        if len(login) == 0 or len(password) == 0:
            createWarningInfoBar(
                parent=self,
                title="Error",
                content="login and password cannot be empty.",
            )
            return False
        auth_response = self._authorization.login(
                login=login,
                password=password
            )
        if not auth_response["status"]:
            createWarningInfoBar(
                parent=self,
                title="Error",
                content=str(auth_response["detail"])
            )
            return auth_response
        createSuccessInfoBar(
            parent=self,
            title="Success",
            content=str(auth_response["detail"])
        )
        QTimer.singleShot(2000, self.open_app)
        return True

    def open_app(self):
        self.sw_open_app.emit()

    def open_registration_page(self):
        if self._startup:
            self._registration_page = RegistrationWindow(self._authorization, self)
            self._startup = False
        self._registration_page.show()
        self.hide()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap("resources/images/login_background.jpg").scaled(
            self.LoginImage.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.LoginImage.setPixmap(pixmap)