import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from mwin import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        try:
            with open('style.qss') as f:
                style = f.read()
                self.setStyleSheet(style)
        except:
            print("open styleshet error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    # clipboard = QApplication.clipboard()
    # clipboard.dataChanged.connect(window.onClipboardChanged)
    sys.exit(app.exec_())
