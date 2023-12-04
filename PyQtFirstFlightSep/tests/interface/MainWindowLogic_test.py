'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-08 03:59:57
 # @ description: test for interface.MainWindowLogic
 '''

from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt

from src.interface.MainWindowLogic import MainWindowLogic

if __name__ == '__main__':
    # add support for high DPI display
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    main_window_logic: MainWindowLogic = MainWindowLogic()
    main_window_logic.show()
    app.exec_()
    pass