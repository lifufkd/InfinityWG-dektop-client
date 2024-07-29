##########################
#       Created By       #
#          SBR           #
##########################
import sys
from typing import Optional

from PySide6.QtCore import Qt
from qfluentwidgets import InfoBar, InfoBarPosition, InfoBarIcon, MessageBoxBase, SubtitleLabel, LineEdit
##########################

##########################


def isWin11():
    return sys.platform == 'win32' and sys.getwindowsversion().build >= 22000


def select_window() -> Optional[object]:
    if isWin11():
        from qframelesswindow import AcrylicWindow as Window
    else:
        from qframelesswindow import FramelessWindow as Window
    return Window


class SettingMessageBox(MessageBoxBase):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('Host URL')
        self.urlLineEdit = LineEdit()

        self.urlLineEdit.setPlaceholderText("Enter the server's URL")
        self.urlLineEdit.setClearButtonEnabled(True)

        # Add components to the layout
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)

        # Set the minimum width of the dialog box
        self.widget.setMinimumWidth(350)


def createSuccessInfoBar(parent, title: str, content: str):
    InfoBar.success(
        title=title,
        content=content,
        orient=Qt.Horizontal,
        isClosable=True,
        position=InfoBarPosition.TOP_RIGHT,
        # position='Custom',   # NOTE: use custom info bar manager
        duration=2000,
        parent=parent
    )


def createWarningInfoBar(parent, title: str, content: str):
    InfoBar.warning(
        title=title,
        content=content,
        orient=Qt.Horizontal,
        isClosable=False,  # disable close button
        position=InfoBarPosition.TOP_RIGHT,
        duration=5000,
        parent=parent
    )


def createInfoInfoBar(parent, title: str, content: str):
    InfoBar(
        icon=InfoBarIcon.INFORMATION,
        title=title,
        content=content,
        orient=Qt.Vertical,  # vertical layout
        isClosable=True,
        position=InfoBarPosition.TOP_RIGHT,
        duration=5000,
        parent=parent
    )
