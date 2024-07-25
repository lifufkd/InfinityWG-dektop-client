# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainiOWGGH.ui'
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

from qfluentwidgets import (BodyLabel, CardWidget, IconWidget, PrimaryPushButton,
    PushButton, ToolButton, TransparentToolButton)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.setWindowModality(Qt.WindowModality.NonModal)
        Main.resize(874, 759)
        self.gridLayout = QGridLayout(Main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ConnectionCard = CardWidget(Main)
        self.ConnectionCard.setObjectName(u"ConnectionCard")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConnectionCard.sizePolicy().hasHeightForWidth())
        self.ConnectionCard.setSizePolicy(sizePolicy)
        self.ConnectionCard.setMinimumSize(QSize(380, 410))
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
        self.CountryIcon_2 = IconWidget(self.ConnectionCard)
        self.CountryIcon_2.setObjectName(u"CountryIcon_2")
        self.CountryIcon_2.setMinimumSize(QSize(20, 20))
        self.CountryIcon_2.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/images/alarms.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CountryIcon_2.setProperty("icon", icon)

        self.horizontalLayout_2.addWidget(self.CountryIcon_2)

        self.HorizontalSpacerSelectCOuntry_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.HorizontalSpacerSelectCOuntry_5)

        self.hintLabel_3 = BodyLabel(self.ConnectionCard)
        self.hintLabel_3.setObjectName(u"hintLabel_3")
        self.hintLabel_3.setFont(font)
        self.hintLabel_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hintLabel_3.setWordWrap(True)
        self.hintLabel_3.setMargin(0)
        self.hintLabel_3.setProperty("lightColor", QColor(96, 96, 96))
        self.hintLabel_3.setProperty("darkColor", QColor(206, 206, 206))

        self.horizontalLayout_2.addWidget(self.hintLabel_3)

        self.HorizontalSpacerSelectCOuntry_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.HorizontalSpacerSelectCOuntry_6)

        self.moreButton_3 = TransparentToolButton(self.ConnectionCard)
        self.moreButton_3.setObjectName(u"moreButton_3")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(20)
        font1.setItalic(False)
        font1.setKerning(True)
        self.moreButton_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.moreButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.horizontalLayout_1.setContentsMargins(5, -1, -1, -1)
        self.HorizontalSpacerSelectCOuntry_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_1.addItem(self.HorizontalSpacerSelectCOuntry_2)

        self.hintLabel_2 = BodyLabel(self.ConnectionCard)
        self.hintLabel_2.setObjectName(u"hintLabel_2")
        self.hintLabel_2.setFont(font)
        self.hintLabel_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hintLabel_2.setWordWrap(True)
        self.hintLabel_2.setMargin(0)
        self.hintLabel_2.setProperty("lightColor", QColor(96, 96, 96))
        self.hintLabel_2.setProperty("darkColor", QColor(206, 206, 206))

        self.horizontalLayout_1.addWidget(self.hintLabel_2)

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
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(14)
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


        self.gridLayout.addWidget(self.ConnectionCard, 0, 0, 1, 1)


        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Form", None))
        self.hintLabel_3.setText(QCoreApplication.translate("Main", u"Russia", None))
        self.hintLabel_2.setText(QCoreApplication.translate("Main", u"78.104.156.123", None))
        self.ConnectBtn.setText(QCoreApplication.translate("Main", u"Loading...", None))
        self.ChangeIpBtn.setText(QCoreApplication.translate("Main", u"change ip", None))
    # retranslateUi

