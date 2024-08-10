# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homefTGesU.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLayout,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, IconWidget, IndeterminateProgressBar,
    PrimaryPushButton, PushButton, ToolButton, TransparentToolButton)

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.setWindowModality(Qt.WindowModality.NonModal)
        Home.resize(917, 654)
        self.gridLayout_2 = QGridLayout(Home)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.ConnectionCard = CardWidget(Home)
        self.ConnectionCard.setObjectName(u"ConnectionCard")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConnectionCard.sizePolicy().hasHeightForWidth())
        self.ConnectionCard.setSizePolicy(sizePolicy)
        self.ConnectionCard.setMinimumSize(QSize(400, 350))
        self.ConnectionCard.setMaximumSize(QSize(400, 350))
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
        self.HorizontalSpacerSelectCOuntry_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.HorizontalSpacerSelectCOuntry_5)

        self.CountryIcon = IconWidget(self.ConnectionCard)
        self.CountryIcon.setObjectName(u"CountryIcon")
        self.CountryIcon.setMinimumSize(QSize(20, 20))
        self.CountryIcon.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/images/alarms.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CountryIcon.setProperty("icon", icon)

        self.horizontalLayout_2.addWidget(self.CountryIcon)

        self.CurrentCountryText = BodyLabel(self.ConnectionCard)
        self.CurrentCountryText.setObjectName(u"CurrentCountryText")
        self.CurrentCountryText.setFont(font)
        self.CurrentCountryText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CurrentCountryText.setWordWrap(True)
        self.CurrentCountryText.setMargin(0)
        self.CurrentCountryText.setProperty("lightColor", QColor(96, 96, 96))
        self.CurrentCountryText.setProperty("darkColor", QColor(206, 206, 206))

        self.horizontalLayout_2.addWidget(self.CurrentCountryText)

        self.ChooseServerButton = TransparentToolButton(self.ConnectionCard)
        self.ChooseServerButton.setObjectName(u"ChooseServerButton")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(20)
        font1.setItalic(False)
        font1.setKerning(True)
        self.ChooseServerButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.ChooseServerButton)

        self.HorizontalSpacerSelectCOuntry_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.HorizontalSpacerSelectCOuntry_6)


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

        self.ChangeIpBtn = PrimaryPushButton(self.ConnectionCard)
        self.ChangeIpBtn.setObjectName(u"ChangeIpBtn")
        self.ChangeIpBtn.setFont(font2)
        self.ChangeIpBtn.setAutoDefault(True)

        self.horizontalLayout_3.addWidget(self.ChangeIpBtn)

        self.HorizontalSpacerSelectCOuntry_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.HorizontalSpacerSelectCOuntry_9)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.progressBar = IndeterminateProgressBar(self.ConnectionCard)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setTextVisible(False)

        self.horizontalLayout_4.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.TopVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.TopVerticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, -1, -1, -1)
        self.IncomingIcon = IconWidget(self.ConnectionCard)
        self.IncomingIcon.setObjectName(u"IncomingIcon")
        self.IncomingIcon.setMinimumSize(QSize(18, 18))
        self.IncomingIcon.setMaximumSize(QSize(20, 20))
        self.IncomingIcon.setProperty("icon", icon)

        self.horizontalLayout_5.addWidget(self.IncomingIcon)

        self.IncomingText = BodyLabel(self.ConnectionCard)
        self.IncomingText.setObjectName(u"IncomingText")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(18)
        self.IncomingText.setFont(font3)
        self.IncomingText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.IncomingText.setWordWrap(True)
        self.IncomingText.setMargin(0)
        self.IncomingText.setProperty("lightColor", QColor(96, 96, 96))
        self.IncomingText.setProperty("darkColor", QColor(206, 206, 206))

        self.horizontalLayout_5.addWidget(self.IncomingText)

        self.HorizontalSpacerSelectCOuntry_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.HorizontalSpacerSelectCOuntry_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, -1, -1, -1)
        self.UpcomingIcon = IconWidget(self.ConnectionCard)
        self.UpcomingIcon.setObjectName(u"UpcomingIcon")
        self.UpcomingIcon.setMinimumSize(QSize(18, 18))
        self.UpcomingIcon.setMaximumSize(QSize(20, 20))
        self.UpcomingIcon.setProperty("icon", icon)

        self.horizontalLayout_6.addWidget(self.UpcomingIcon)

        self.UpcomingText = BodyLabel(self.ConnectionCard)
        self.UpcomingText.setObjectName(u"UpcomingText")
        self.UpcomingText.setFont(font3)
        self.UpcomingText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.UpcomingText.setWordWrap(True)
        self.UpcomingText.setMargin(0)
        self.UpcomingText.setProperty("lightColor", QColor(96, 96, 96))
        self.UpcomingText.setProperty("darkColor", QColor(206, 206, 206))

        self.horizontalLayout_6.addWidget(self.UpcomingText)

        self.HorizontalSpacerSelectCOuntry_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.HorizontalSpacerSelectCOuntry_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.ConnectionCard, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Form", None))
        self.CurrentCountryText.setText("")
        self.CurrentIPText.setText("")
        self.ConnectBtn.setText(QCoreApplication.translate("Home", u"Connect", None))
        self.ChangeIpBtn.setText(QCoreApplication.translate("Home", u"Change IP", None))
        self.IncomingText.setText("")
        self.UpcomingText.setText("")
    # retranslateUi

