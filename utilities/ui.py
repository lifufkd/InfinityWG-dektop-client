##########################
#       Created By       #
#          SBR           #
##########################
import sys
from typing import Optional

from PySide6.QtCore import Qt
from API.Requests import VPN
from qfluentwidgets import (InfoBar, InfoBarPosition, InfoBarIcon,
                            MessageBoxBase, SubtitleLabel, LineEdit, ComboBox)
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
        self.populateComboBox()
        self.setDefaultValue(vpn.get_country())

        # Add components to the layout
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.country_combo_box)

        # Set the minimum width of the dialog box
        self.widget.setMinimumWidth(350)

    def populateComboBox(self):
        countries = [
            ("United States.ico", "United States"),
            ("Canada.ico", "Canada"),
            ("United Kingdom.ico", "United Kingdom"),
            ("Australia.ico", "Australia"),
            ("Germany.ico", "Germany"),
            # Add more countries as needed
        ]
        countries.append(
            ("Unknown.ico", "Auto")
        )
        for icon_path, name in countries:
            self.country_combo_box.addItem(icon=f"resources/country_flags/{icon_path}", text=name)

    def setDefaultValue(self, country: str = "Auto"):
        index = self.country_combo_box.findText(country)
        if index != -1:
            self.country_combo_box.setCurrentIndex(index)
            return True
        index = self.country_combo_box.findText("Auto")
        self.country_combo_box.setCurrentIndex(index)


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
