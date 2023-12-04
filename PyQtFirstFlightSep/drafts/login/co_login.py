from PySide2.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout

import sys

from PySide2.QtWidgets import QApplication

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # set the window title
        self.setWindowTitle("Login")

        # create the username and password labels and line edits
        self.username_label = QLabel("Username:")
        self.username_edit = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        # create the login button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.accept)

        # create the layout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.login_button)

        # set the layout
        self.setLayout(layout)

    def getUsername(self):
        return self.username_edit.text()

    def getPassword(self):
        return self.password_edit.text()
    
    
    
app = QApplication([])
dialog = LoginDialog()
if dialog.exec_() == QDialog.Accepted:
    username = dialog.getUsername()
    password = dialog.getPassword()
    print(username, password)
    # do something with the username and password
sys.exit(app.exec_())