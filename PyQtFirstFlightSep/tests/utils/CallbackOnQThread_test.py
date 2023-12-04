'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-08 03:11:36
 # @ description: test for utils.CallbackOnQThread
 '''

import sys
import time
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

from src.utils.CallbackOnQThread import CallbackOnQThread

def callback() -> None:
    for i in range(10):
        print(i)
        time.sleep(1)
        pass
    pass

def finished_callback() -> None:
    print("finished")
    pass

class MainWindow(QMainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.callback_thread = CallbackOnQThread()
        self.callback_thread.setParent(self)
        self.callback_thread.setCallback(callback)
        self.callback_thread.setFinishedCallback(finished_callback)
        self.resize(300, 300)
        self.button = QPushButton("test for CallbackOnQThread")
        self.setCentralWidget(self.button)
        self.button.clicked.connect(self.callback_thread.start)
        pass
    
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
    pass

# expected output:

# utils: CallbackOnQThread.py imported
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# finished