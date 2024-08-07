##########################
#       Created By       #
#          SBR           #
##########################
from PySide6.QtCore import Qt, QTimer, Signal
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtWidgets import QApplication
from qfluentwidgets import setTheme, Theme, SplitTitleBar, isDarkTheme, FluentIcon
from UI.pages.registration.UI_registration import Ui_Registration
from modules.ui import (isWin11, select_window, createWarningInfoBar,
                        createSuccessInfoBar, SettingMessageBox)
from resources.vars import APP_NAME
from API.Requests import Authorization
from modules.config import Config
##########################

##########################


Window = select_window()


class RegistrationWindow(Window, Ui_Registration):
    sw_open_login = Signal()

    def __init__(self, authorization: Authorization):
        super().__init__()

        self.original_pixmap = None
        self._config = Config()

        self.setupUi(self)
        setTheme(Theme.AUTO)

        self._authorization = authorization
        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()
        self.LoginImage.setScaledContents(False)
        self.setWindowTitle(APP_NAME)

        self.RegisterpushButton.clicked.connect(self.registrate)
        self.LoginPushButton.clicked.connect(lambda: self.sw_open_login.emit())
        self.SettingsPushButton.clicked.connect(self.open_settings)
        self.LoginPushButton.setIcon(FluentIcon.RETURN)
        self.SettingsPushButton.setIcon(FluentIcon.SETTING)

        self.initWindow()

    def initWindow(self):
        self.resize(self._config.get(self._config.login_width), self._config.get(self._config.login_height))
        self.setWindowIcon(QIcon("resources/images/logo.svg"))
        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=isDarkTheme())
        if not isWin11():
            color = QColor(25, 33, 42) if isDarkTheme() else QColor(240, 244, 249)
            self.setStyleSheet(f"LoginWindow{{background: {color.name()}}}")

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.original_pixmap = QPixmap("resources/images/login_background.jpg")

    def registrate(self):
        login = self.LoginlineEdit.text()
        password = self.PasswordlineEdit.text()
        repeat_password = self.RepeatPasswordlineEdit.text()
        full_name = self.FioLineEdit.text()
        if len(login) == 0 or len(password) == 0 or len(full_name) == 0:
            createWarningInfoBar(
                parent=self,
                title="Error",
                content="login and password cannot be empty",
            )
            return False
        elif len(password) < 8:
            createWarningInfoBar(
                parent=self,
                title="Error",
                content="All fields must be greater than 8 characters",
            )
            return False
        elif password != repeat_password:
            createWarningInfoBar(
                parent=self,
                title="Error",
                content="Passwords do not match",
            )
            return False
        auth_response = self._authorization.registration(
            login=login,
            password=password,
            full_name=full_name
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
        QTimer.singleShot(2000, self.open_login_registrated)
        return True

    def open_login_registrated(self):
        self.LoginlineEdit.setText("")
        self.PasswordlineEdit.setText("")
        self.RepeatPasswordlineEdit.setText("")
        self.FioLineEdit.setText("")
        self.sw_open_login.emit()

    def open_settings(self):
        w = SettingMessageBox(self)
        w.urlLineEdit.setText(self._authorization.get_host_url())
        if w.exec():
            self._authorization.change_host_url(w.urlLineEdit.text())

    def resizeEvent(self, e):
        self._config.set(self._config.login_width, e.size().width())
        self._config.set(self._config.login_height, e.size().height())
        super().resizeEvent(e)
        pixmap = self.original_pixmap.scaled(
            self.LoginImage.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.LoginImage.setPixmap(pixmap)