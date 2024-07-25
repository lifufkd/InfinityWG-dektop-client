##########################
#       Created By       #
#          SBR           #
##########################
import sys
from typing import Optional
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
