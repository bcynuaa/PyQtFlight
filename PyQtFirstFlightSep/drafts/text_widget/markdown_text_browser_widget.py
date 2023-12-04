from PySide2.QtWidgets import QApplication, QMainWindow, QTextBrowser
import sys

from qt_material import apply_stylesheet

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # create a QTextBrowser widget
        self.text_browser = QTextBrowser(self)

        # set the text of the QTextBrowser
        self.text_browser.setPlainText("Hello, world!")
        self.text_browser.setMarkdown("|    | parameters1       |    values1 | parameters2      |   values2 |\n \
|---:|:------------------|-----------:|:-----------------|----------:|\n \
|  0 | pressure altitude | 290.402    | CAS              |       917 |\n \
|  1 | mach              |   0.895698 | alpha            |         8 |\n \
|  2 | phi               |   5        | beta             |         5 |\n \
|  3 | left flaperon     |  -7        | right flaperon   |        -7 |\n \
|  4 | left horiz tail   |   6        | right horiz tail |        -3 |\n \
|  5 | left rudder       |   2        | right rudder     |         7 |")

        # add the QTextBrowser to the main window
        self.setCentralWidget(self.text_browser)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_teal.xml")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())