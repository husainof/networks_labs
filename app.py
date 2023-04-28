import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QTextEdit, QMessageBox
from PyQt5.QtCore import Qt


class EmailClient(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем интерфейс
        self.from_email_label = QLabel('From:')
        self.from_email_edit = QLineEdit()
        self.to_email_label = QLabel('To:')
        self.to_email_edit = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.server_label = QLabel('SMTP Server:')
        self.server_edit = QLineEdit()
        self.port_label = QLabel('SMTP Port:')
        self.port_edit = QLineEdit()
        self.subject_label = QLabel('Subject:')
        self.subject_edit = QLineEdit()
        self.message_label = QLabel('Message:')
        self.message_edit = QTextEdit()
        self.attachments_label = QLabel('Attachments:')
        self.attachments_edit = QListWidget()
        self.attachments_button = QPushButton('Browse')
        self.send_button = QPushButton('Send')

        self.from_email_edit.setText('amatersu.oni@yandex.ru')
        self.to_email_edit.setText('amatersu.oni@yandex.ru')
        self.password_edit.setText('')
        self.server_edit.setText('smtp.yandex.ru')
        self.port_edit.setText('465')
        self.subject_edit.setText('')
        self.message_edit.setText('')

        # Располагаем элементы интерфейса
        layout = QVBoxLayout()
        layout.addWidget(self.from_email_label)
        layout.addWidget(self.from_email_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.to_email_label)
        layout.addWidget(self.to_email_edit)
        layout.addWidget(self.server_label)
        layout.addWidget(self.server_edit)
        layout.addWidget(self.port_label)
        layout.addWidget(self.port_edit)
        layout.addWidget(self.subject_label)
        layout.addWidget(self.subject_edit)
        layout.addWidget(self.message_label)
        layout.addWidget(self.message_edit)
        layout.addWidget(self.attachments_label)
        attachments_layout = QHBoxLayout()
        attachments_layout.addWidget(self.attachments_edit)
        attachments_layout.addWidget(self.attachments_button)
        layout.addLayout(attachments_layout)
        layout.addWidget(self.send_button)
        self.attachmts = []
        # Привязываем функцию-обработчик к нажатию на кнопку
        self.attachments_button.clicked.connect(self.browse_attachments)
        self.send_button.clicked.connect(self.send_email)

        # Устанавливаем компоновщик
        self.setLayout(layout)

    def browse_attachments(self):
        # Открываем диалоговое окно для выбора файла
        file_names, _ = QFileDialog.getOpenFileNames(
            self, 'Open File', '', 'All Files (*.*)')
        # Устанавливаем выбранный файл в поле вложений
        for file in file_names:
            self.attachments_edit.addItem(file)
            self.attachmts.append(file)

    def send_email(self):
        # Получаем значения полей формы
        sender_email = self.from_email_edit.text()
        recipient_email = self.to_email_edit.text()
        sender_password = self.password_edit.text()
        smtp_server = self.server_edit.text()
        smtp_port = int(self.port_edit.text())
        subject = self.subject_edit.text()
        message = self.message_edit.toPlainText()
        attachments = list(self.attachmts)
        recipients_email_list = recipient_email.split(',')

        # Создаем объект сообщения
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        # Добавляем вложения
        for attachment in attachments:
            if attachment != '':
                with open(attachment, 'rb') as f:
                    att = MIMEApplication(f.read(), _subtype='pdf')
                    att.add_header('Content-Disposition',
                                   'attachment', filename=attachment)
                    msg.attach(att)

        # Отправляем сообщение
        try:
            server = smtplib.SMTP_SSL(smtp_server, smtp_port)
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipients_email_list,
                            msg.as_string())
            QMessageBox.information(
                self, "Успешно", "Письмо успешно отправлено!")
        except Exception as e:
            QMessageBox.warning(
                self, "Ошибка", "Ошибка при отправке письма: " + str(e))

        # Очищаем поля формы
        self.from_email_edit.setText('amatersu.oni@yandex.ru')
        self.to_email_edit.setText('amatersu.oni@yandex.ru')
        self.password_edit.setText('')
        self.server_edit.setText('smtp.yandex.ru')
        self.port_edit.setText('465')
        self.subject_edit.setText('')
        self.message_edit.setText('')
        self.attachments_edit.clear()
        self.attachmts.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = EmailClient()
    client.show()
    sys.exit(app.exec_())
