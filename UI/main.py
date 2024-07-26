##########################
#       Created By       #
#          SBR           #
##########################
import sys
from qfluentwidgets import FluentTranslator
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QApplication
from UI.pages.login.login import LoginWindow
from utilities.UI.config import cfg
from API.Requests import Authorization
##########################

##########################


def main() -> None:
    login = LoginWindow()
    login.show()


if __name__ == "__main__":
    authorization = Authorization(cfg)
    print(authorization.login("123455678", "12345567"))
    print(authorization.check_token())
    print(authorization.registration("wdfwefwefwefwef22", "qwdqefwefwefwefwef", "erherh"))
    app = QApplication(sys.argv)
    app.installTranslator(FluentTranslator(QLocale())) # TODO: Change to config load method
    print(cfg.get(cfg.host))
    main()
    sys.exit(app.exec())

