##########################
#       Created By       #
#          SBR           #
##########################
import sys
from typing import Optional

from PySide6.QtCore import Qt
from qfluentwidgets import InfoBar, InfoBarPosition

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
