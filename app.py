from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QListWidget, QWidget, QLineEdit, QMessageBox


import socket_helper


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

        vbox.addWidget(self.listWidget)

        self.setLayout(vbox)

        button = QPushButton("Get list of servers", self)

        button.resize(button.sizeHint())

        button.clicked.connect(self.click)

        vbox.addWidget(button)

        self.le = QLineEdit(self)

        vbox.addWidget(self.le)

        wid = QWidget(self)

        self.setCentralWidget(wid)

        wid.setLayout(vbox)

    def click(self):
        self.listWidget.clear()

        socket_helper.update_list_servers(self.le.text())

        self.listWidget.addItems(socket_helper.target_list)


App = QApplication(sys.argv)


window = Window()


sys.exit(App.exec())
