import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 退出按钮
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 50)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a QPushButton widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        # 等于 resize + move
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Hello QT5')
        self.setWindowIcon(QIcon('/Users/xiaoyuu/PycharmProjects/my-pyqt5/assets/image.jpg'))
        self.center()
        self.show()

    def center(self):
        # 获得主窗口所在的框架
        qr = self.frameGeometry()
        # 获取显示器的分辨率，然后得到屏幕中间点的位置
        cp = QDesktopWidget().availableGeometry().center()
        # 然后把主窗口框架的中心点放置到屏幕的中心位置。
        qr.moveCenter(cp)
        # 然后通过move函数把主窗口的左上角移动到其框架的左上角，这样就把窗口居中了
        self.move(qr.topLeft())

    def closeEvent(self, event):
        # 创建一个消息框，有俩按钮：Yes和No.标题栏，对话框，第三个参数是消息框的俩按钮，最后一个参数是默认按钮
        reply = QMessageBox.question(self, 'Message', 'are you sure to quit', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()

    '''
        新建一个Windows组件 改大小，位置，标题，展示
    '''
    # w = QWidget()
    # w.resize(250,150)
    # w.move(300,300)
    # w.setWindowTitle('Hello QT')
    # w.show()

    sys.exit(app.exec_())
