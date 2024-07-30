##########################
#       Created By       #
#          SBR           #
##########################
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from qfluentwidgets import NavigationItemPosition, SplitFluentWindow, FluentIcon as FIF, Dialog

from UI.pages.login.login import LoginWindow
from UI.pages.registration.registration import RegistrationWindow
from UI.pages.home.home import Home
from resources.vars import APP_NAME
from API.Requests import Authorization, VPN
from utilities.schedule import TaskScheduler
from utilities.wireguard import WireGuard
##########################

##########################


class Main(SplitFluentWindow):
    def __init__(self, vpn: VPN, scheduler: TaskScheduler, wireguard: WireGuard):
        super().__init__()
        # create sub interface
        self.HomeInterface = Home(vpn=vpn, scheduler=scheduler, wireguard=wireguard, parent=self)

        self._scheduler = scheduler
        self._wireguard = wireguard
        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        # add sub interface
        self.addSubInterface(self.HomeInterface, FIF.HOME, 'Home')

        self.navigationInterface.addItem(
            routeKey='settingInterface',
            icon=FIF.SETTING,
            text='Settings',
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

    def closeEvent(self, event):
        w = Dialog("Exit", "Are you sure you want to close the program?", self)
        if w.exec() and self.HomeInterface.connected:
            self._wireguard.disconnect()


class App:
    def __init__(self,
                 authorization: Authorization,
                 scheduler: TaskScheduler,
                 token_status: bool,
                 wireguard: WireGuard,
                 vpn: VPN):
        super().__init__()
        # TODO: Make sure that when the program starts, the window loads in
        #  accordance with the received token status for security
        self._scheduler = scheduler
        self._vpn = vpn
        self._wireguard = wireguard
        self._authorization = authorization
        self._token_status = token_status
        self._login_window = None
        self._reg_window = None
        self._main = None
        self._stop_check_token = False
        self._token_started = False
        self.init()

    def init(self):
        self._main = Main(vpn=self._vpn, scheduler=self._scheduler, wireguard=self._wireguard)
        self._login_window = LoginWindow(self._authorization)
        self._reg_window = RegistrationWindow(self._authorization)

        # Connect the signal to the slot
        self._login_window.sw_open_app.connect(self.show_app)
        self._login_window.sw_open_reg.connect(self.open_reg)

        self._reg_window.sw_open_app.connect(self.show_app)
        self._reg_window.sw_open_login.connect(self.open_login)
        if not self._token_status:
            self._login_window.show()
        else:
            self._scheduler.add_task("token_check", self.check_token, 5000)
            self._token_started = True
            self._main.show()

    def show_app(self):
        self._main.resize(1280, 720)
        self._main.show()
        if not self._stop_check_token:
            self._token_started = True
            self._scheduler.add_task("token_check", self.check_token, 5000)
        self._login_window.hide()
        self._reg_window.hide()

    def open_reg(self):
        self._reg_window.resize(1280, 720)
        self._reg_window.show()
        self._login_window.hide()

    def open_login(self):
        self._login_window.resize(1280, 720)
        self._login_window.show()
        self._reg_window.hide()

    def check_token(self):
        if not self._stop_check_token:
            status = self._authorization.check_token()["status"]
            if not status:
                self.open_login()
                self._main.hide()
                self._wireguard.disconnect()
                self._stop_check_token = True


