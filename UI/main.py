##########################
#       Created By       #
#          SBR           #
##########################
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from qfluentwidgets import setTheme, Theme
from PySide6.QtGui import QIcon
from qframelesswindow import FramelessWindow
##########################

##########################


import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Второе окно")
        self.setGeometry(100, 100, 400, 300)
        label = QLabel("Это второе окно", self)
        layout = QVBoxLayout()
        layout.addWidget(label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Первое окно")
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton("Открыть второе окно", self)
        self.button.clicked.connect(self.open_second_window)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

