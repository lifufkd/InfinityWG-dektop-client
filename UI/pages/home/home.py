##########################
#       Created By       #
#          SBR           #
##########################
from PySide6.QtWidgets import QWidget
from UI.pages.home.UI_home import Ui_Home
##########################

##########################


class Home(Ui_Home, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)