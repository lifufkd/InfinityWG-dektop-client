# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerLyMmXZ.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, HyperlinkButton, LineEdit)
import resource_rc

class Ui_Registration(object):
    def setupUi(self, Registration):
        if not Registration.objectName():
            Registration.setObjectName(u"Registration")
        Registration.resize(1235, 839)
        Registration.setMinimumSize(QSize(700, 500))
        self.gridLayout = QGridLayout(Registration)
        self.gridLayout.setObjectName(u"gridLayout")
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
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.horizontalLayout_1.setContentsMargins(5, -1, -1, -1)
        self.HorizontalSpacerSelectCOuntry_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_1.addItem(self.HorizontalSpacerSelectCOuntry_2)

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

        self.horizontalLayout_1.addWidget(self.Logo)

        self.HorizontalSpacerSelectCOuntry = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_1.addItem(self.HorizontalSpacerSelectCOuntry)


        self.verticalLayout.addLayout(self.horizontalLayout_1)

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

        self.RepeatPasswordlineEdit_2 = LineEdit(self.widget)
        self.RepeatPasswordlineEdit_2.setObjectName(u"RepeatPasswordlineEdit_2")
        self.RepeatPasswordlineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.RepeatPasswordlineEdit_2.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.RepeatPasswordlineEdit_2)

        self.label_8 = BodyLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.FioLineEdit_3 = LineEdit(self.widget)
        self.FioLineEdit_3.setObjectName(u"FioLineEdit_3")
        self.FioLineEdit_3.setEchoMode(QLineEdit.EchoMode.Password)
        self.FioLineEdit_3.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.FioLineEdit_3)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.RegisterpushButton = HyperlinkButton(self.widget)
        self.RegisterpushButton.setObjectName(u"RegisterpushButton")

        self.verticalLayout.addWidget(self.RegisterpushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.LoginImage = QLabel(Registration)
        self.LoginImage.setObjectName(u"LoginImage")
        self.LoginImage.setFrameShape(QFrame.Shape.NoFrame)
        self.LoginImage.setPixmap(QPixmap(u":/login/resources/images/register_background.jpg"))
        self.LoginImage.setScaledContents(True)

        self.gridLayout.addWidget(self.LoginImage, 0, 1, 1, 1)


        self.retranslateUi(Registration)

        QMetaObject.connectSlotsByName(Registration)
    # setupUi

    def retranslateUi(self, Registration):
        Registration.setWindowTitle(QCoreApplication.translate("Registration", u"Form", None))
        self.Logo.setText("")
        self.label_5.setText(QCoreApplication.translate("Registration", u"Login", None))
        self.LoginlineEdit.setPlaceholderText(QCoreApplication.translate("Registration", u"example@example.com", None))
        self.label_6.setText(QCoreApplication.translate("Registration", u"Password", None))
        self.PasswordlineEdit.setPlaceholderText(QCoreApplication.translate("Registration", u"\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.label_7.setText(QCoreApplication.translate("Registration", u"Repeat Password", None))
        self.RepeatPasswordlineEdit_2.setPlaceholderText(QCoreApplication.translate("Registration", u"\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.label_8.setText(QCoreApplication.translate("Registration", u"Your name", None))
        self.FioLineEdit_3.setPlaceholderText(QCoreApplication.translate("Registration", u"Alex Sure", None))
        self.RegisterpushButton.setText(QCoreApplication.translate("Registration", u"Register", None))
        self.LoginImage.setText("")
    # retranslateUi

