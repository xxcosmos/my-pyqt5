import sys
import cv2
from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, qApp
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

        self.originText.setFocus(True)
        self.translatedText = QTranslator()
        self.actiondestination_language = 'zh-CN'
        self.actionlanguage = 0
        self.isRealTimeTranslation = False
        self.isPaperMode = False
        self.connectSlots()

    # 右键菜单
    def contextMenuEvent(self, event):
        # 右键菜单
        cmenu = QMenu(self)
        cmenu.addAction("new")
        cmenu.addAction("open")
        quitAct = cmenu.addAction("quit")
        # 使用 exec_()显示菜单，从鼠标右键事件对象中获得当前坐标，mapToGlobal()  把当前组件的相对坐标转换为窗口的绝对坐标
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp.quit()

    def connectSlots(self):
        pass


# self.isWindowTop.clicked.connect(self.windowTopFunction)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    # clipboard = QApplication.clipboard()
    # clipboard.dataChanged.connect(window.onClipboardChanged)
    sys.exit(app.exec_())
