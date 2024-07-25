##########################
#       Created By       #
#          SBR           #
##########################
import sys
from PySide6.QtCore import Qt, QLocale
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentTranslator, setTheme, Theme, SplitTitleBar, isDarkTheme, FluentIcon
from UI.pages.registration.UI_registration import Ui_Registration
from utilities.UI.utilities import isWin11, select_window
from resources.vars import APP_NAME

##########################

##########################


Window = select_window()


class RegistrationWindow(Window, Ui_Registration):

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        setTheme(Theme.AUTO)

        self._login_page = parent
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

        self.LoginPushButton.clicked.connect(self.open_login_page)
        self.LoginPushButton.setIcon(FluentIcon.RETURN)

    def open_login_page(self):
        self._login_page.show()
        self.hide()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap("../resources/images/register_background.jpg").scaled(
            self.LoginImage.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.LoginImage.setPixmap(pixmap)