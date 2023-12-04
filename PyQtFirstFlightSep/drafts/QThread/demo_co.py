from PySide2.QtCore import QFileSystemWatcher, QObject, Slot
from PySide2.QtWidgets import QMainWindow, QLabel, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel('File not modified')
        self.setCentralWidget(self.label)

        self.file_watcher = QFileSystemWatcher()
        self.file_watcher.addPath('.//drafts//QThread//demo_co.py')
        self.file_watcher.fileChanged.connect(self.on_file_changed)

    @Slot(str)
    def on_file_changed(self, path):
        self.label.setText("a")

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()