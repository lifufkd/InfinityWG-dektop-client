##########################
#       Created By       #
#          SBR           #
##########################
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from qfluentwidgets import NavigationItemPosition, SplitFluentWindow
from qfluentwidgets import FluentIcon as FIF

from UI.pages.login.login import LoginWindow
from UI.pages.registration.registration import RegistrationWindow
from UI.pages.home.home import Home
from resources.vars import APP_NAME
from API.Requests import Authorization
##########################

##########################


class Main(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        # create sub interface
        self.focusInterface = Home(self)

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        # add sub interface
        self.addSubInterface(self.focusInterface, FIF.HOME, 'Home')

        self.navigationInterface.addItem(
            routeKey='settingInterface',
            icon=FIF.SETTING,
            text='settings',
            position=NavigationItemPosition.BOTTOM,
        )

        self.navigationInterface.setExpandWidth(280)

    def initWindow(self):
        self.resize(1280, 720)
        self.setWindowIcon(QIcon('resources/images/logo.svg'))
        self.setWindowTitle(APP_NAME)

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)


class App:
    def __init__(self, authorization: Authorization, token_status: bool):
        super().__init__()
        self._authorization = authorization
        self._token_status = token_status
        self._login_window = None
        self._reg_window = None
        self._main = None
        self.init()

    def init(self):
        if not self._token_status:
            self._login_window = LoginWindow(self._authorization)
            self._reg_window = RegistrationWindow(self._authorization)

            # Connect the signal to the slot
            self._login_window.sw_open_app.connect(self.load_app)
            self._login_window.sw_open_reg.connect(self.open_reg)

            self._reg_window.sw_open_app.connect(self.load_app)
            self._reg_window.sw_open_login.connect(self.open_login)

            self._login_window.show()
        else:
            self._main = Main()
            self._main.show()

    def load_app(self):
        self._main = Main()
        self._main.show()
        self._login_window.close()
        self._reg_window.close()

    def open_reg(self):
        self._reg_window.resize(1280, 720)
        self._reg_window.show()
        self._login_window.hide()

    def open_login(self):
        self._login_window.show()
        self._reg_window.hide()



