'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-04 20:39:46
 # @ description: test for utils.FileMonitorOnThread
 '''

from src.utils.FileMonitorOnQThread import FileMonitorOnQThread

import sys

from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

class MainWindow(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.resize(400, 400)
        pass
    
    def setup(self) -> None:
        self.label: QLabel = QLabel("Watching...")
        self.button: QPushButton = QPushButton("Stop")
        
        self.layout: QVBoxLayout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        
        self.file_monitor_on_thread: FileMonitorOnQThread = FileMonitorOnQThread()
        self.file_monitor_on_thread.setMonitorPath(".")
        self.file_monitor_on_thread.setModifiedCallback(self.changeLabelText)
        
        self.button.clicked.connect(self.file_monitor_on_thread.stop)
        pass
    
    def changeLabelText(self, text: str) -> None:
        self.label.setText(text)
        print(text)
        pass
    
    pass

if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    main_window: MainWindow = MainWindow()
    main_window.setup()
    main_window.show()
    main_window.file_monitor_on_thread.start()
    sys.exit(app.exec_())
    pass