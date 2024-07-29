##########################
#       Created By       #
#          SBR           #
##########################
from PySide6.QtCore import Qt, QTimer, Signal
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtWidgets import QApplication
from qfluentwidgets import setTheme, Theme, SplitTitleBar, isDarkTheme, FluentIcon
from UI.pages.login.UI_login import Ui_Login
from utilities.UI.utilities import (isWin11, select_window, createWarningInfoBar,
                                    createSuccessInfoBar, SettingMessageBox)
from resources.vars import APP_NAME
from API.Requests import Authorization
##########################

##########################


Window = select_window()


class LoginWindow(Window, Ui_Login):
    sw_open_app = Signal()
    sw_open_reg = Signal()

    def __init__(self, authorization: Authorization):
        super().__init__()
        # TODO: Add setting menu to login and reg page with host url line edit
        self.setupUi(self)
        setTheme(Theme.AUTO)

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
        self.RegistrationpushButton.clicked.connect(self.open_reg)
        self.SettingsPushButton.clicked.connect(self.open_settings)
        self.SettingsPushButton.setIcon(FluentIcon.SETTING)

    def login(self):
        login = self.LoginlineEdit.text()
        password = self.PasswordlineEdit.text()
        remember_me = self.RememberMecheckBox.checkState().value
        if remember_me == 0:
            remember_me = False
        else:
            remember_me = True
        if len(login) == 0 or len(password) == 0:
            createWarningInfoBar(
                parent=self,
                title="Error",
                content="login and password cannot be empty.",
            )
            return False
        auth_response = self._authorization.login(
                login=login,
                password=password,
                remember_me=remember_me
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

    def open_reg(self):
        self.sw_open_reg.emit()

    def open_settings(self):
        w = SettingMessageBox(self)
        w.urlLineEdit.setText(self._authorization.get_host_url())
        if w.exec():
            self._authorization.change_host_url(w.urlLineEdit.text())

    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap("resources/images/login_background.jpg").scaled(
            self.LoginImage.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.LoginImage.setPixmap(pixmap)