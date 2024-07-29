# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerHUdiEY.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, LineEdit, PrimaryPushButton, PushButton,
    ToolButton, TransparentToolButton)
import resources.UI_resources

class Ui_Registration(object):
    def setupUi(self, Registration):
        if not Registration.objectName():
            Registration.setObjectName(u"Registration")
        Registration.resize(1235, 839)
        Registration.setMinimumSize(QSize(700, 500))
        self.horizontalLayout = QHBoxLayout(Registration)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(Registration)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(360, 0))
        self.widget.setMaximumSize(QSize(360, 16777215))
        self.widget.setStyleSheet(u"QLabel{\n"
"	font: 13px 'Microsoft YaHei'\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 25, -1, 25)
        self.LoginPushButton = TransparentToolButton(self.widget)
        self.LoginPushButton.setObjectName(u"LoginPushButton")
        self.LoginPushButton.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.LoginPushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.Logo_Layout = QHBoxLayout()
        self.Logo_Layout.setObjectName(u"Logo_Layout")
        self.Logo_Layout.setContentsMargins(5, -1, -1, -1)
        self.HorizontalSpacerSelectCOuntry_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Logo_Layout.addItem(self.HorizontalSpacerSelectCOuntry_2)

        self.Logo = QLabel(self.widget)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy1)
        self.Logo.setMinimumSize(QSize(100, 100))
        self.Logo.setMaximumSize(QSize(100, 100))
        self.Logo.setPixmap(QPixmap(u":/login/resources/images/logo.svg"))
        self.Logo.setScaledContents(True)

        self.Logo_Layout.addWidget(self.Logo)

        self.HorizontalSpacerSelectCOuntry = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.Logo_Layout.addItem(self.HorizontalSpacerSelectCOuntry)


        self.verticalLayout.addLayout(self.Logo_Layout)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_5 = BodyLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.LoginlineEdit = LineEdit(self.widget)
        self.LoginlineEdit.setObjectName(u"LoginlineEdit")
        self.LoginlineEdit.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.LoginlineEdit)

        self.label_6 = BodyLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.PasswordlineEdit = LineEdit(self.widget)
        self.PasswordlineEdit.setObjectName(u"PasswordlineEdit")
        self.PasswordlineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.PasswordlineEdit.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.PasswordlineEdit)

        self.label_7 = BodyLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.RepeatPasswordlineEdit = LineEdit(self.widget)
        self.RepeatPasswordlineEdit.setObjectName(u"RepeatPasswordlineEdit")
        self.RepeatPasswordlineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.RepeatPasswordlineEdit.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.RepeatPasswordlineEdit)

        self.label_8 = BodyLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.FioLineEdit = LineEdit(self.widget)
        self.FioLineEdit.setObjectName(u"FioLineEdit")
        self.FioLineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        self.FioLineEdit.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.FioLineEdit)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.RegisterpushButton = PrimaryPushButton(self.widget)
        self.RegisterpushButton.setObjectName(u"RegisterpushButton")
        font = QFont()
        font.setFamilies([u"HoloLens MDL2 Assets"])
        font.setPointSize(16)
        self.RegisterpushButton.setFont(font)

        self.verticalLayout.addWidget(self.RegisterpushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.SettingsPushButton = TransparentToolButton(self.widget)
        self.SettingsPushButton.setObjectName(u"SettingsPushButton")
        self.SettingsPushButton.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.SettingsPushButton)


        self.horizontalLayout.addWidget(self.widget)

        self.LoginImage = QLabel(Registration)
        self.LoginImage.setObjectName(u"LoginImage")
        self.LoginImage.setFrameShape(QFrame.Shape.NoFrame)
        self.LoginImage.setPixmap(QPixmap(u":/login/resources/images/register_background.jpg"))
        self.LoginImage.setScaledContents(True)
        self.LoginImage.setMargin(25)

        self.horizontalLayout.addWidget(self.LoginImage)


        self.retranslateUi(Registration)

        QMetaObject.connectSlotsByName(Registration)
    # setupUi

    def retranslateUi(self, Registration):
        Registration.setWindowTitle(QCoreApplication.translate("Registration", u"Form", None))
        self.Logo.setText("")
        self.label_5.setText(QCoreApplication.translate("Registration", u"Login", None))
        self.LoginlineEdit.setPlaceholderText(QCoreApplication.translate("Registration", u"WG-admin", None))
        self.label_6.setText(QCoreApplication.translate("Registration", u"Password", None))
        self.PasswordlineEdit.setPlaceholderText(QCoreApplication.translate("Registration", u"\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.label_7.setText(QCoreApplication.translate("Registration", u"Repeat Password", None))
        self.RepeatPasswordlineEdit.setPlaceholderText(QCoreApplication.translate("Registration", u"\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.label_8.setText(QCoreApplication.translate("Registration", u"Your name", None))
        self.FioLineEdit.setPlaceholderText(QCoreApplication.translate("Registration", u"Alex Sure", None))
        self.RegisterpushButton.setText(QCoreApplication.translate("Registration", u"Register", None))
        self.LoginImage.setText("")
    # retranslateUi

