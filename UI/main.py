##########################
#       Created By       #
#          SBR           #
##########################
import time

from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import NavigationItemPosition, SplitFluentWindow, FluentIcon as FIF, Dialog

from UI.pages.login.login import LoginWindow
from UI.pages.registration.registration import RegistrationWindow
from UI.pages.home.home import Home
from resources.vars import APP_NAME
from API.Requests import Authorization, VPN
from modules.schedule import TaskScheduler
from modules.wireguard import WireGuard
from modules.ui import createWarningInfoBar, error_info_bar
from modules.network import check_internet_and_dns
from modules.config import Config
##########################

##########################


class Main(SplitFluentWindow):
    def __init__(self, vpn: VPN, scheduler: TaskScheduler, wireguard: WireGuard, parent):
        super().__init__()
        # create sub interface
        self.HomeInterface = Home(vpn=vpn, scheduler=scheduler, wireguard=wireguard, parent=self)
        self._config = Config()

        self._scheduler = scheduler
        self._wireguard = wireguard
        self._parent = parent

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
        self.resize(self._config.get(self._config.app_width), self._config.get(self._config.app_height))
        self.setWindowIcon(QIcon('resources/images/logo.svg'))
        self.setWindowTitle(APP_NAME)

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def process_logout(self):
        self._scheduler.remove_task("internet_check")
        self._scheduler.remove_task("token_check")
        self._parent.logout_signal.emit()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self._config.set(self._config.app_width, e.size().width())
        self._config.set(self._config.app_height, e.size().height())

    def closeEvent(self, event):
        w = Dialog("Exit", "Are you sure you want to close the program?", self)
        if w.exec():
            self._scheduler.remove_task("token_check")
            self._scheduler.remove_task("internet_check")
            self._scheduler.remove_task("network_stats")
            if self.HomeInterface.connected:
                self.HomeInterface._connect_wg(None)
        else:
            event.ignore()


class App(QWidget):
    run_function_signal = Signal(object)
    info_bar_signal = Signal(str, str, str, object)
    logout_signal = Signal()

    def __init__(self,
                 authorization: Authorization,
                 scheduler: TaskScheduler,
                 vpn: VPN,
                 wireguard: WireGuard,
                 token_status: bool):
        super().__init__()

        self._scheduler = scheduler
        self._vpn = vpn
        self._wireguard = wireguard
        self._authorization = authorization
        self._token_status = token_status
        self._config = Config()

        self._login_window = None
        self._reg_window = None
        self._main = None

        self._token_check_flag = None

        self.init()

    @Slot(str, str, str, object)
    def info_bar_handler(self, title, text, type, parent):
        match type:
            case "info":
                pass
            case "warning":
                createWarningInfoBar(title=title,
                                     content=text,
                                     parent=parent)
            case "error":
                error_info_bar(title=title,
                               content=text,
                               parent=parent)

    @Slot(object)
    def thread_handler(self, action):
        action()

    def init(self):
        self.run_function_signal.connect(self.thread_handler)
        self.info_bar_signal.connect(self.info_bar_handler)
        self.logout_signal.connect(self.logout)
        if not self._token_status:
            self.load_login()
            self.load_reg()
            self.open_login()
        else:
            self.load_app()
            self._scheduler.add_task(task_name="token_check", task=self.check_token, interval=5000)
            self._scheduler.add_task(task_name="internet_check", task=self.check_internet_available, interval=2000)
            self._scheduler.add_task(task_name="network_stats", task=self._main.HomeInterface._update_network_stats, interval=0)
            self._main.show()

    def load_login(self):
        if self._login_window is None:
            self._login_window = LoginWindow(self._authorization)
            self._login_window.sw_open_app.connect(self.open_app)
            self._login_window.sw_open_reg.connect(self.open_reg)

    def load_reg(self):
        if self._reg_window is None:
            self._reg_window = RegistrationWindow(self._authorization)
            self._reg_window.sw_open_login.connect(self.open_login)

    def load_app(self):
        if self._main is None:
            self._main = Main(vpn=self._vpn, scheduler=self._scheduler, wireguard=self._wireguard, parent=self)
        update_ip_status = self._vpn.update_ip_address()
        if not update_ip_status["status"]:
            self.info_bar_signal.emit("Warning", update_ip_status["detail"],
                                      "warning", self._main)
        self._main.HomeInterface.update_country_and_ip()

    def open_app(self):
        self.load_app()
        self._scheduler.add_task(task_name="token_check", task=self.check_token, interval=5000)
        self._scheduler.add_task(task_name="internet_check", task=self.check_internet_available, interval=2000)
        self._scheduler.add_task(task_name="network_stats", task=self._main.HomeInterface._update_network_stats,
                                 interval=0)
        self._main.show()
        self._login_window.hide()
        self._reg_window.hide()

    def open_reg(self):
        self._reg_window.resize(self._config.get(self._config.login_width), self._config.get(self._config.login_height))
        self._reg_window.show()
        self._login_window.hide()

    def open_login(self):
        self._login_window.resize(self._config.get(self._config.login_width), self._config.get(self._config.login_height))
        self._login_window.show()
        self._reg_window.hide()

    def logout(self):
        self._authorization.change_token(token="")
        self._scheduler.remove_task("network_stats")
        # UI
        self.load_login()
        self.load_reg()
        self.open_login()
        self._main.hide()
        if self._main.HomeInterface.connected:
            self._main.HomeInterface.connect_wg()

    def check_internet_available(self, stop_signal):

        def logout():
            self.logout_signal.emit()
            self._scheduler.remove_task("token_check")
            stop_signal()

        if not check_internet_and_dns(hosts=self._config.get(self._config.internet_check), duration=5) and self._config.get(self._config.is_internet_check):
            if self._main.HomeInterface.connected:

                for i in range(2):
                    self._main.HomeInterface._connect_wg(None)

                if not check_internet_and_dns(hosts=self._config.get(self._config.internet_check), duration=5):
                    for i in range(3):
                        if self._main.HomeInterface._new_connection_wg(None, server_quality=-i-1):
                            return True
                    logout()
                else:
                    return True
            else:
                logout()
            return False
        return True

    def check_token(self, stop_callback):
        status = self._authorization.check_token()
        if not status["status"]:
            if status["code"] == 0:
                self._scheduler.remove_task("internet_check")
                stop_callback()
                self.logout_signal.emit()
            else:
                if self._token_check_flag:
                    if status["code"] == 1:
                        self.info_bar_signal.emit("Warning", status["detail"],
                                                  "warning", self._main)
                    elif status["code"] == 2:
                        self.info_bar_signal.emit("Error", "Lost connection to server",
                                                  "error", self._main)
                        self._token_check_flag = False
        else:
            if not self._token_check_flag:
                self._token_check_flag = True



