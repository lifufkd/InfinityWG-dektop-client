##########################
#       Created By       #
#          SBR           #
##########################
from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWidgets import QApplication
from qfluentwidgets import (NavigationItemPosition, MessageBox,
                            NavigationAvatarWidget,  SplitFluentWindow)
from qfluentwidgets import FluentIcon as FIF

from UI.pages.login.login import LoginWindow
from UI.pages.registration.registration import RegistrationWindow
from API.Requests import Authorization
##########################

##########################


class Main(SplitFluentWindow):
    def __init__(self):
        super().__init__()

        # create sub interface
        self.focusInterface = FocusInterface(self)
        self.stopWatchInterface = StopWatchInterface(self)

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        # add sub interface
        self.addSubInterface(self.focusInterface, FIF.RINGER, '专注时段')
        self.addSubInterface(self.stopWatchInterface, FIF.STOP_WATCH, '秒表')

        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('zhiyiYo', 'resource/images/shoko.png'),
            onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM,
        )
        self.navigationInterface.addItem(
            routeKey='settingInterface',
            icon=FIF.SETTING,
            text='设置',
            position=NavigationItemPosition.BOTTOM,
        )

        self.navigationInterface.setExpandWidth(280)

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('PyQt-Fluent-Widgets')

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def showMessageBox(self):
        w = MessageBox(
            '支持作者🥰',
            '个人开发不易，如果这个项目帮助到了您，可以考虑请作者喝一瓶快乐水🥤。您的支持就是作者开发和维护项目的动力🚀',
            self
        )
        w.yesButton.setText('来啦老弟')
        w.cancelButton.setText('下次一定')

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://afdian.net/a/zhiyiYo"))


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
            # self._reg_window = RegistrationWindow(self._authorization)

            # Connect the signal to the slot
            self._login_window.sw_open_app.connect(self._load_app)
            self._reg_window.sw_open_app.connect(self._load_app)
            self.open_login()
        else:
            self.load_app()
            self.open_app()

    def _load_app(self):
        self.load_app()
        self.open_app()
        self.close_login()
        self.close_registration()

    def load_app(self):
        self._main = Main()

    def open_app(self):
        self._main.show()

    def hide_app(self):
        self._main.hide()

    def close_app(self):
        self._main.close()

    def open_login(self):
        self._login_window.show()

    def hide_login(self):
        self._login_window.hide()

    def open_registration(self):
        self._reg_window.show()

    def hide_registration(self):
        self._reg_window.hide()

    def close_login(self):
        self._login_window.close()

    def close_registration(self):
        self._reg_window.close()


