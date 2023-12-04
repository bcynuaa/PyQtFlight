'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-09 01:03:20
 # @ description: interface for LoginDialog
 '''

from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout
from PySide2.QtGui import QIcon

from src.config.interface.LoginDialogConfig import *

class LoginDialog(QDialog):
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super().__init__()
        self.__makeSettings()
        self.__makeWidgets()
        self.__makeLayout()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeSettings(self) -> None:
        self.resize(size[0], size[1])
        self.setWindowTitle(dialog_title)
        self.setWindowIcon(QIcon(dialog_icon))
        self.setStyleSheet(login_dialog_config_style)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeWidgets(self) -> None:
        # username
        self.username_label: QLabel = QLabel(username_label)
        self.username_line_edit: QLineEdit = QLineEdit()
        self.username_line_edit.setPlaceholderText(username_line_edit)
        # password
        self.password_label: QLabel = QLabel(password_label)
        self.password_line_edit: QLineEdit = QLineEdit()
        self.password_line_edit.setPlaceholderText(password_line_edit)
        self.password_line_edit.setEchoMode(QLineEdit.Password)
        # login button
        self.login_button: QPushButton = QPushButton(login_button)
        self.login_button.clicked.connect(self.accept)
        pass
    
    def __makeLayout(self) -> None:
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        # username layout
        self.username_horizontal_layout = QHBoxLayout()
        self.username_horizontal_layout.addWidget(self.username_label)
        self.username_horizontal_layout.addWidget(self.username_line_edit)
        # password layout
        self.password_horizontal_layout = QHBoxLayout()
        self.password_horizontal_layout.addWidget(self.password_label)
        self.password_horizontal_layout.addWidget(self.password_line_edit)
        # login button layout
        self.login_button_horizontal_layout = QHBoxLayout()
        self.login_button_horizontal_layout.addWidget(self.login_button)
        # add layouts
        self.main_layout.addLayout(self.username_horizontal_layout)
        self.main_layout.addLayout(self.password_horizontal_layout)
        self.main_layout.addLayout(self.login_button_horizontal_layout)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def getUsername(self) -> str:
        return self.username_line_edit.text()
        pass
    
    def getPassword(self) -> str:
        return self.password_line_edit.text()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("interface: LoginDialog.py is imported.")