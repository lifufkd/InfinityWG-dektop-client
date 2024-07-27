##########################
#       Created By       #
#          SBR           #
##########################
from PySide6.QtCore import Qt, QTimer, Signal
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtWidgets import QApplication
from qfluentwidgets import setTheme, Theme, SplitTitleBar, isDarkTheme, FluentIcon
from UI.pages.registration.UI_registration import Ui_Registration
from utilities.UI.utilities import isWin11, select_window, createSuccessInfoBar, createWarningInfoBar
from resources.vars import APP_NAME
from API.Requests import Authorization
##########################

##########################


Window = select_window()


class RegistrationWindow(Window, Ui_Registration):
    sw_open_app = Signal()
    sw_open_login = Signal()

    def __init__(self, authorization: Authorization):
        super().__init__()
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

        self.RegisterpushButton.clicked.connect(self.registrate)
        self.LoginPushButton.clicked.connect(self.open_login)
        self.LoginPushButton.setIcon(FluentIcon.RETURN)

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
        elif len(login) < 8 or len(password) < 8 or len(full_name) < 8:
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
        QTimer.singleShot(2000, self.open_app)
        return True

    def open_app(self):
        self.sw_open_app.emit()

    def open_login(self):
        self.sw_open_login.emit()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap("resources/images/register_background.jpg").scaled(
            self.LoginImage.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.LoginImage.setPixmap(pixmap)