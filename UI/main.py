##########################
#       Created By       #
#          SBR           #
##########################
import sys
from PySide6.QtWidgets import QApplication
from UI.pages.login.login import LoginWindow
##########################

##########################


def main() -> None:
    login = LoginWindow()
    login.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main()
    sys.exit(app.exec())

