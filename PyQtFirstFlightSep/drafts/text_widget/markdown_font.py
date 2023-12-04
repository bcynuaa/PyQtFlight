from PySide2.QtWidgets import QApplication, QMainWindow, QTextBrowser
from PySide2.QtGui import QTextOption, QFont
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # create a QTextBrowser widget
        self.text_browser = QTextBrowser(self)

        # set the markdown text of the QTextBrowser
        self.text_browser.setMarkdown("## Hello, world!")

        # set the font size of the QTextBrowser
        font = QFont()
        font.setPointSize(50)
        self.text_browser.setFont(font)

        # add the QTextBrowser to the main window
        self.setCentralWidget(self.text_browser)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())