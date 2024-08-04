##########################
#       Created By       #
#          SBR           #
##########################
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import NavigationItemPosition, SplitFluentWindow, FluentIcon as FIF, Dialog

from UI.pages.login.login import LoginWindow
from UI.pages.registration.registration import RegistrationWindow
from UI.pages.home.home import Home
from resources.vars import APP_NAME
from API.Requests import Authorization, VPN
from modules.schedule import TaskScheduler
from modules.wireguard import WireGuard
from modules.ui import thread_handler
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

        self.navigationInterface.addItem(
            routeKey='logoutInterface',
            icon=FIF.POWER_BUTTON,
            onClick=self.process_logout,
            text='Logout',
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

    def process_logout(self):
        self._scheduler.remove_task("token_check")
        self.HomeInterface.logout_signal.emit()

    def closeEvent(self, event):
        w = Dialog("Exit", "Are you sure you want to close the program?", self)
        if w.exec():
            self._scheduler.remove_task("token_check")
            if self.HomeInterface.connected:
                self.HomeInterface._connect_wg(None)
        else:
            event.ignore()


class App(QWidget):
    thread_handler_signal = Signal(object)

    def __init__(self,
                 authorization: Authorization,
                 scheduler: TaskScheduler,
                 token_status: bool,
                 wireguard: WireGuard,
                 vpn: VPN):
        super().__init__()

        self._scheduler = scheduler
        self._vpn = vpn
        self._wireguard = wireguard
        self._authorization = authorization
        self._token_status = token_status
        self._login_window = None
        self._reg_window = None
        self._main = None

        self.init()

    def init(self):
        self.thread_handler_signal.connect(thread_handler)
        if not self._token_status:
            self.load_login()
            self.load_reg()
            self._login_window.show()
        else:
            self.load_app()
            self._scheduler.add_task(task_name="token_check", task=self.check_token, interval=5000)
            self._main.show()

    def load_login(self):
        if self._login_window is None:
            self._login_window = LoginWindow(self._authorization)
            self._login_window.sw_open_app.connect(self.show_app)
            self._login_window.sw_open_reg.connect(self.open_reg)

    def load_reg(self):
        if self._reg_window is None:
            self._reg_window = RegistrationWindow(self._authorization)
            self._reg_window.sw_open_login.connect(self.open_login)

    def load_app(self):
        if self._main is None:
            self._main = Main(vpn=self._vpn, scheduler=self._scheduler, wireguard=self._wireguard)
            self._main.HomeInterface.logout_signal.connect(self.logout)
            if not self._vpn.update_ip_address()["status"]:
                self.logout()

    def show_app(self):
        self.load_app()
        self._main.resize(1280, 720)
        self._scheduler.add_task(task_name="token_check", task=self.check_token, interval=5000)
        self._main.show()
        self._login_window.hide()
        self._reg_window.hide()

    def logout(self):
        self._authorization.change_token(token="")

        # UI
        self.load_login()
        self.load_reg()
        self.open_login()
        self._main.hide()
        if self._main.HomeInterface.connected:
            self._main.HomeInterface.connect_wg()

    def open_reg(self):
        self._reg_window.resize(1280, 720)
        self._reg_window.show()
        self._login_window.hide()

    def open_login(self):
        self._login_window.resize(1280, 720)
        self._login_window.show()
        self._reg_window.hide()

    def check_token(self, stop_callback):
        status = self._authorization.check_token()["status"]
        if not status:
            self.thread_handler_signal.emit(self.logout)
            stop_callback()


