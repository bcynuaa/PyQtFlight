import sys
from PySide2 import QtWidgets
from PySide2.QtCore import QThread

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.output = QtWidgets.QTextBrowser()
        self.output.setFontFamily('times new roman')
        self.output.setFontPointSize(12)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.output)
        sys.stdout = self

    def write(self, text):
        self.output.insertPlainText(text)
        self.output.moveCursor(self.output.textCursor().End) 
        QtWidgets.QApplication.processEvents()

    def flush(self):
        pass
    
    pass


app = QtWidgets.QApplication([])
window = Window()
window.show()
print('Hello, World!')
app.exec_()