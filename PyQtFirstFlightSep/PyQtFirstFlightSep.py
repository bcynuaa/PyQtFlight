'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-09 03:36:01
 # @ description: main entrance for PyQtFirstFlightSep
 '''

import os
import sys

from PySide2 import QtCore
from PySide2 import QtWidgets

from src.utils.KeyExaminer import KeyExaminer
from src.interface.LoginDialog import LoginDialog
from src.interface.MainWindowLogic import MainWindowLogic

os.environ["QT_API"] = "pyside2"

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    login_dialog: LoginDialog = LoginDialog()
    login_dialog.show()
    if login_dialog.exec_() == QtWidgets.QDialog.Accepted:
        key_examiner: KeyExaminer = KeyExaminer()
        key_examiner.setUsername(login_dialog.getUsername())
        key_examiner.setPassword(login_dialog.getPassword())
        if key_examiner.check() == True:
            window_logic: MainWindowLogic = MainWindowLogic()
            window_logic.show()
            pass
        else:
            print("Wrong username or password!")
            sys.exit(0)
            pass
        pass
    else:
        print("Login canceled!")
        sys.exit(0)
        pass
    sys.exit(app.exec_())
    pass