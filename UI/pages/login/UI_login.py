# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginGSZFTR.ui'
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

from qfluentwidgets import (BodyLabel, CheckBox, LineEdit, PrimaryPushButton,
    PushButton)
import resources.UI_resources

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(1269, 718)
        Login.setMinimumSize(QSize(700, 500))
        self.horizontalLayout = QHBoxLayout(Login)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(Login)
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
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 25, 9, 25)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

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

        self.verticalLayout_2.addWidget(self.Logo, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.label_5 = BodyLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.LoginlineEdit = LineEdit(self.widget)
        self.LoginlineEdit.setObjectName(u"LoginlineEdit")
        self.LoginlineEdit.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.LoginlineEdit)

        self.label_6 = BodyLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.PasswordlineEdit = LineEdit(self.widget)
        self.PasswordlineEdit.setObjectName(u"PasswordlineEdit")
        self.PasswordlineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.PasswordlineEdit.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.PasswordlineEdit)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.RememberMecheckBox = CheckBox(self.widget)
        self.RememberMecheckBox.setObjectName(u"RememberMecheckBox")
        self.RememberMecheckBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.RememberMecheckBox)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.LoginpushButton = PrimaryPushButton(self.widget)
        self.LoginpushButton.setObjectName(u"LoginpushButton")
        font = QFont()
        font.setFamilies([u"HoloLens MDL2 Assets"])
        font.setPointSize(16)
        self.LoginpushButton.setFont(font)

        self.verticalLayout_2.addWidget(self.LoginpushButton)

        self.verticalSpacer_6 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.RegistrationpushButton = PushButton(self.widget)
        self.RegistrationpushButton.setObjectName(u"RegistrationpushButton")
        self.RegistrationpushButton.setFont(font)

        self.verticalLayout_2.addWidget(self.RegistrationpushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget)

        self.LoginImage = QLabel(Login)
        self.LoginImage.setObjectName(u"LoginImage")
        self.LoginImage.setAutoFillBackground(False)
        self.LoginImage.setFrameShape(QFrame.Shape.NoFrame)
        self.LoginImage.setPixmap(QPixmap(u":/login/resources/images/login_background.jpg"))
        self.LoginImage.setScaledContents(True)
        self.LoginImage.setMargin(25)

        self.horizontalLayout.addWidget(self.LoginImage)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.Logo.setText("")
        self.label_5.setText(QCoreApplication.translate("Login", u"Login", None))
        self.LoginlineEdit.setPlaceholderText(QCoreApplication.translate("Login", u"WG-admin", None))
        self.label_6.setText(QCoreApplication.translate("Login", u"Password", None))
        self.PasswordlineEdit.setPlaceholderText(QCoreApplication.translate("Login", u"\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.RememberMecheckBox.setText(QCoreApplication.translate("Login", u"Remember me", None))
        self.LoginpushButton.setText(QCoreApplication.translate("Login", u"Login", None))
        self.RegistrationpushButton.setText(QCoreApplication.translate("Login", u"Registration", None))
        self.LoginImage.setText("")
    # retranslateUi

