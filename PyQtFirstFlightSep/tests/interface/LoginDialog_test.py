'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-09 01:53:59
 # @ description: test for interface.LoginDialog
 '''

import sys
from PySide2.QtWidgets import QApplication, QDialog

from src.interface.LoginDialog import LoginDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_dialog = LoginDialog()
    login_dialog.show()
    if login_dialog.exec_() == QDialog.Accepted:
        print("username: %s" % login_dialog.username_line_edit.text())
        print("password: %s" % login_dialog.password_line_edit.text())
        sys.exit(0)
        pass
    else:
        # exit the main program
        sys.exit(0)
        pass
    sys.exit(app.exec_())
    pass