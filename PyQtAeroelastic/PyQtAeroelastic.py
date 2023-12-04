# coding = "utf-8"
# author: bcynuaa
# date  : 2023/05/04

####################################################################################################

import sys
import os
os.environ["QT_API"] = "pyside2"

from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
from src.Logic_MainWindow import *

QtGui.QFont().setFamily('times new roman')
QtGui.QFont().setPointSize(18)

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) # add support for high dpi
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    pass


####################################################################################################