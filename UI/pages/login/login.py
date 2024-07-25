##########################
#       Created By       #
#          SBR           #
##########################
import sys
from PySide6.QtCore import Qt, QLocale
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentTranslator, setTheme, Theme, SplitTitleBar, isDarkTheme
from UI_login import Ui_Login
from utilities.UI_utilities import isWin11, select_window
##########################

##########################


Window = select_window()


class LoginWindow(Window, Ui_Login):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        setTheme(Theme.AUTO)

        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()

        self.LoginImage.setScaledContents(False)
        self.setWindowTitle('InfinityWG')
        self.setWindowIcon(QIcon("../../../resources/images/logo.svg"))
        self.resize(1280, 720)

        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=isDarkTheme())
        if not isWin11():
            color = QColor(25, 33, 42) if isDarkTheme() else QColor(240, 244, 249)
            self.setStyleSheet(f"LoginWindow{{background: {color.name()}}}")

        self.titleBar.titleLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 13px 'Segoe UI';
                padding: 0 4px;
                color: white
            }
        """)

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap("../../../resources/images/login_background.jpg").scaled(
            self.LoginImage.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.LoginImage.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Internationalization
    translator = FluentTranslator(QLocale())
    app.installTranslator(translator)

    w = LoginWindow()
    w.show()
    app.exec()