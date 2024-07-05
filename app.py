##########################
#       Created By       #
#          SBR           #
##########################
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from qfluentwidgets import setTheme, Theme
from PySide6.QtGui import QIcon
from qframelesswindow import FramelessWindow
from UI.sidebar import SideBar
from UI.TitleBar import CustomTitleBar
##########################
config_path = 'config.json'
##########################


class Window(FramelessWindow):
    def __init__(self):
        super().__init__()
        setTheme(Theme.AUTO)
        SideBar(self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
    