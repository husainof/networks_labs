from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QPlainTextEdit, QWidget, QLineEdit, QMessageBox, QLabel

import sys

from ftp_tree import get_tree 


class Window(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("LR 3")

        self.setGeometry(100, 100, 300, 200)

        self.UiComponents()

        self.show()

    def UiComponents(self):

        vbox = QVBoxLayout(self)
        self.tree = QPlainTextEdit(self)
        

        vbox.addWidget(self.tree)

        self.setLayout(vbox)

        button = QPushButton("Get directory tree", self)

        button.resize(button.sizeHint())

        button.clicked.connect(self.click)

        vbox.addWidget(button)

        self.host = QLineEdit(self)
        self.host.setPlaceholderText("Введите ftp адрес")
        self.login = QLineEdit(self)
        self.login.setPlaceholderText(
            "Введите логин")
        self.password = QLineEdit(self)
        self.password.setPlaceholderText(
            "Введите пароль")
        self.host.setText('91.222.128.11')
        self.login.setText('testftp_guest')
        self.password.setText('12345')

        vbox.addWidget(self.host)
        vbox.addWidget(self.login)
        vbox.addWidget(self.password)


        wid = QWidget(self)

        self.setCentralWidget(wid)

        wid.setLayout(vbox)

    def click(self):
        tree = get_tree( self.host.text(), self.login.text(),self.password.text())
        self.tree.clear()
        self.tree.setPlainText(tree)


App = QApplication(sys.argv)


window = Window()


sys.exit(App.exec())
