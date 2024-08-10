##########################
#       Created By       #
#          SBR           #
##########################
import os
import sys
from typing import Optional

from PySide6.QtCore import Qt
from API.Requests import VPN
from qfluentwidgets import (InfoBar, InfoBarPosition, InfoBarIcon,
                            MessageBoxBase, SubtitleLabel, LineEdit, ComboBox)
from modules.system import send_notification, country_serializer
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


class SelectCountryMessageBox(MessageBoxBase):

    def __init__(self, vpn: VPN, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('Select country')
        self.country_combo_box = ComboBox()
        self._vpn = vpn
        self.populateComboBox()
        self.setDefaultValue(vpn.get_country_config())

        # Add components to the layout
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.country_combo_box)

        # Set the minimum width of the dialog box
        self.widget.setMinimumWidth(350)

    def populateComboBox(self):
        countries = list()
        data = self._vpn.get_countries()
        if data["status"]:
            for country in data["data"].keys():
                countries.append((data["data"][country]["name"], data["data"][country]["name"]))
        else:
            createWarningInfoBar(title="Error", content=data["detail"], parent=self)
        countries.append(
            ("Unknown", "Auto")
        )
        for country, name in countries:
            icon_path = country_serializer("resources/country_flags", country)
            if icon_path is not None:
                self.country_combo_box.addItem(icon=icon_path, text=name)
            else:
                self.country_combo_box.addItem(text=name)

    def setDefaultValue(self, country: str = "Auto"):
        index = self.country_combo_box.findText(country)
        if index != -1:
            self.country_combo_box.setCurrentIndex(index)
            return True
        index = self.country_combo_box.findText("Auto")
        self.country_combo_box.setCurrentIndex(index)


def createSuccessInfoBar(parent, title: str, content: str, duration: int = 2000):
    InfoBar.success(
        title=title,
        content=content,
        orient=Qt.Horizontal,
        isClosable=False,
        position=InfoBarPosition.TOP_RIGHT,
        duration=duration,
        parent=parent
    )


def createWarningInfoBar(parent, title: str, content: str, duration: int = 5000):
    InfoBar.warning(
        title=title,
        content=content,
        orient=Qt.Horizontal,
        isClosable=False,
        position=InfoBarPosition.TOP_RIGHT,
        duration=duration,
        parent=parent
    )


def error_info_bar(parent, title: str, content: str, duration: int = -1):
    InfoBar.error(
        title=title,
        content=content,
        orient=Qt.Vertical,  # Use vertical layout when the content is too long
        isClosable=True,
        position=InfoBarPosition.TOP_RIGHT,
        duration=duration,
        parent=parent
    )


def createInfoInfoBar(parent, title: str, content: str, duration: int = 5000):
    InfoBar(
        icon=InfoBarIcon.INFORMATION,
        title=title,
        content=content,
        orient=Qt.Vertical,
        isClosable=False,
        position=InfoBarPosition.TOP_RIGHT,
        duration=duration,
        parent=parent
    )


def wg_status_notify(parent: object, connect_status: bool):
    if not connect_status:
        notification_text = "WireGuard tunnel successfully disconnected"
    else:
        notification_text = "WireGuard tunnel successfully connected"
    notify = send_notification(title="InfinityWG", text=notification_text)
    if not notify["status"]:
        createWarningInfoBar(title="Error", content=notify["detail"], parent=parent)