# https://blog.csdn.net/yurensan/article/details/121025642
import sys
from PySide2.QtWidgets import QPushButton,QLabel,QProgressDialog,QHBoxLayout,QVBoxLayout,QWidget,QApplication,QMainWindow
from PySide2.QtCore import *

class QProgressDialogDemo(QMainWindow):
    def __init__(self):
        super(QProgressDialogDemo, self).__init__()

        #设置窗口大小
        self.resize(400, 150)
        self.setWindowTitle("QProgressDialogDemo")

        btn = QPushButton("开始")
        btn.clicked.connect(self.btnClick)

        #创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(btn)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def btnClick(self):
        elapsed = 200000
        self.progressDialog = QProgressDialog('下载进度','取消',0,elapsed,self)
        self.progressDialog.setWindowTitle('QProgressDialog')
        self.progressDialog.show()
        for val in range(elapsed):
            self.progressDialog.setValue(val)
            QCoreApplication.processEvents()
            if self.progressDialog.wasCanceled():
                break
        self.progressDialog.setValue(elapsed)

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QProgressDialogDemo()
    main.show()
    sys.exit(app.exec_())

