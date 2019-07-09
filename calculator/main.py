import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from calculator.caculator_ui import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        # 0-9 点击事件绑定
        self.one.clicked.connect(self.onClickedNumber)
        self.zero.clicked.connect(self.onClickedZero)
        self.two.clicked.connect(self.onClickedTwo)
        self.three.clicked.connect(self.onClickedThree)
        self.four.clicked.connect(self.onClickedFour)
        self.five.clicked.connect(self.onClickedFive)
        self.six.clicked.connect(self.onClickedSix)
        self.seven.clicked.connect(self.onClickedSeven)
        self.eight.clicked.connect(self.onClickedEight)
        self.nine.clicked.connect(self.onClickedNine)
        # .点 点击事件绑定
        self.dot.clicked.connect(self.onClickedDot)
        # 运算符点击事件绑定
        self.equal.clicked.connect(self.onClickedEqual)
        self.add.clicked.connect(self.onClickedAdd)
        self.sub.clicked.connect(self.onClickedSub)
        self.mutiply.clicked.connect(self.onClickedMutiply)
        self.divide.clicked.connect(self.onClickedDivide)

    def onClickedNumber(self):
        number = str(self.sender().objectName())
        num = 0
        if number == 'zero':
            num = 0
        if number == 'one':
            num = 1
        if number == 'two':
            num = 2
        if number == 'three':
            num = 3
        if number == 'four':
            num = 4
        if number == 'five':
            num = 5
        if number == 'six':
            num = 6
        if number == 'seven':
            number = 7
        if number == 'eight':
            number = 8
        result = float(self.result.text())
        result *= 10
        result += 1
        self.result.setText()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
