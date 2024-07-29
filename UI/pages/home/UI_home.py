# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeuRPSZV.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, IconWidget, PrimaryPushButton,
    PushButton, ToolButton, TransparentToolButton)

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.setWindowModality(Qt.WindowModality.NonModal)
        Home.resize(418, 300)
        self.horizontalLayout = QHBoxLayout(Home)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ConnectionCard = CardWidget(Home)
        self.ConnectionCard.setObjectName(u"ConnectionCard")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConnectionCard.sizePolicy().hasHeightForWidth())
        self.ConnectionCard.setSizePolicy(sizePolicy)
        self.ConnectionCard.setMinimumSize(QSize(400, 250))
        self.ConnectionCard.setMaximumSize(QSize(600, 600))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        self.ConnectionCard.setFont(font)
        self.ConnectionCard.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.ConnectionCard)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.BottomVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.BottomVerticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, -1, -1, -1)
        self.CountryIcon = IconWidget(self.ConnectionCard)
        self.CountryIcon.setObjectName(u"CountryIcon")
        self.CountryIcon.setMinimumSize(QSize(20, 20))
        self.CountryIcon.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/images/alarms.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CountryIcon.setProperty("icon", icon)

        self.horizontalLayout_2.addWidget(self.CountryIcon)

        self.HorizontalSpacerSelectCOuntry_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.HorizontalSpacerSelectCOuntry_5)

        self.CurrentCountryText = BodyLabel(self.ConnectionCard)
        self.CurrentCountryText.setObjectName(u"CurrentCountryText")
        self.CurrentCountryText.setFont(font)
        self.CurrentCountryText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CurrentCountryText.setWordWrap(True)
        self.CurrentCountryText.setMargin(0)
        self.CurrentCountryText.setProperty("lightColor", QColor(96, 96, 96))
        self.CurrentCountryText.setProperty("darkColor", QColor(206, 206, 206))

        self.horizontalLayout_2.addWidget(self.CurrentCountryText)

        self.HorizontalSpacerSelectCOuntry_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.HorizontalSpacerSelectCOuntry_6)

        self.ChooseServerButton = TransparentToolButton(self.ConnectionCard)
        self.ChooseServerButton.setObjectName(u"ChooseServerButton")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(20)
        font1.setItalic(False)
        font1.setKerning(True)
        self.ChooseServerButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.ChooseServerButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.horizontalLayout_1.setContentsMargins(5, -1, -1, -1)
        self.HorizontalSpacerSelectCOuntry_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_1.addItem(self.HorizontalSpacerSelectCOuntry_2)

        self.CurrentIPText = BodyLabel(self.ConnectionCard)
        self.CurrentIPText.setObjectName(u"CurrentIPText")
        self.CurrentIPText.setFont(font)
        self.CurrentIPText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CurrentIPText.setWordWrap(True)
        self.CurrentIPText.setMargin(0)
        self.CurrentIPText.setProperty("lightColor", QColor(96, 96, 96))
        self.CurrentIPText.setProperty("darkColor", QColor(206, 206, 206))

        self.horizontalLayout_1.addWidget(self.CurrentIPText)

        self.HorizontalSpacerSelectCOuntry = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_1.addItem(self.HorizontalSpacerSelectCOuntry)


        self.verticalLayout.addLayout(self.horizontalLayout_1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, -1, -1, -1)
        self.HorizontalSpacerSelectCOuntry_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.HorizontalSpacerSelectCOuntry_8)

        self.ConnectBtn = PrimaryPushButton(self.ConnectionCard)
        self.ConnectBtn.setObjectName(u"ConnectBtn")
        font2 = QFont()
        font2.setFamilies([u"HoloLens MDL2 Assets"])
        font2.setPointSize(16)
        self.ConnectBtn.setFont(font2)
        self.ConnectBtn.setAutoDefault(True)

        self.horizontalLayout_3.addWidget(self.ConnectBtn)

        self.HorizontalSpacerSelectCOuntry_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.HorizontalSpacerSelectCOuntry_7)

        self.ChangeIpBtn = PrimaryPushButton(self.ConnectionCard)
        self.ChangeIpBtn.setObjectName(u"ChangeIpBtn")
        self.ChangeIpBtn.setFont(font2)
        self.ChangeIpBtn.setAutoDefault(True)

        self.horizontalLayout_3.addWidget(self.ChangeIpBtn)

        self.HorizontalSpacerSelectCOuntry_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.HorizontalSpacerSelectCOuntry_9)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.TopVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.TopVerticalSpacer)


        self.horizontalLayout.addWidget(self.ConnectionCard)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Form", None))
        self.CurrentCountryText.setText(QCoreApplication.translate("Home", u"Russia", None))
        self.CurrentIPText.setText(QCoreApplication.translate("Home", u"78.104.156.123", None))
        self.ConnectBtn.setText(QCoreApplication.translate("Home", u"Loading...", None))
        self.ChangeIpBtn.setText(QCoreApplication.translate("Home", u"change ip", None))
    # retranslateUi

