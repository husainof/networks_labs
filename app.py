from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QListWidget, QWidget, QLineEdit, QMessageBox, QLabel


import socket_helper

from main import foundLinks, checkedLinks, btn_click

import sys  # Только для доступа к аргументам командной строки


class Window(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("LR 2")

        self.setGeometry(100, 100, 300, 200)

        self.UiComponents()

        self.show()

    def UiComponents(self):

        vbox = QVBoxLayout(self)

        self.listWidget = QListWidget()

        self.checked_urls = QListWidget()

        vbox.addWidget(self.listWidget)
        vbox.addWidget(self.checked_urls)

        self.setLayout(vbox)

        button = QPushButton("Get list of servers", self)

        button.resize(button.sizeHint())

        button.clicked.connect(self.click)

        vbox.addWidget(button)

        self.le = QLineEdit(self)
        self.le.setPlaceholderText("Введите проверяемый адрес")
        self.le_num = QLineEdit(self)
        self.le_num.setPlaceholderText(
            "Введите количество страниц")

        vbox.addWidget(self.le)
        vbox.addWidget(self.le_num)

        wid = QWidget(self)

        self.setCentralWidget(wid)

        wid.setLayout(vbox)

    def click(self):
        self.listWidget.clear()

        # socket_helper.update_list_servers(self.le.text())
        btn_click()
        self.listWidget.addItems(foundLinks)
        self.checked_urls.addItems(checkedLinks)

        self


App = QApplication(sys.argv)


window = Window()


sys.exit(App.exec())
