"""
 简单计算器，旨在练习pyqt5界面编程，故采用了最简单的计算方式，即遇到一个运算符就计算一次结果，不采用逆波兰式，栈等计算方式。
 Create By xiaoyuu
 xandcosmos@gmail.com
"""
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from calculator.caculator_ui import Ui_MainWindow

numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
operator = '='
operator_stack = []
number_stack = [0, ]
last_clicked = 'number'


def operate_two_numbers(a, b, op):
    if op == 'add':
        return a + b
    elif op == 'sub':
        return a - b
    elif op == 'multiply':
        return a * b
    elif op == 'divide':
        return a / b


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        # 0-9 点击事件绑定
        self.zero.clicked.connect(self.on_clicked_number)
        self.one.clicked.connect(self.on_clicked_number)
        self.two.clicked.connect(self.on_clicked_number)
        self.three.clicked.connect(self.on_clicked_number)
        self.four.clicked.connect(self.on_clicked_number)
        self.five.clicked.connect(self.on_clicked_number)
        self.six.clicked.connect(self.on_clicked_number)
        self.seven.clicked.connect(self.on_clicked_number)
        self.eight.clicked.connect(self.on_clicked_number)
        self.nine.clicked.connect(self.on_clicked_number)

        # clear 点击事件绑定
        self.clear.clicked.connect(self.on_clicked_clear)

        # 运算符点击事件绑定
        self.equal.clicked.connect(self.on_clicked_operator)
        self.add.clicked.connect(self.on_clicked_operator)
        self.sub.clicked.connect(self.on_clicked_operator)
        self.multiply.clicked.connect(self.on_clicked_operator)
        self.divide.clicked.connect(self.on_clicked_operator)

    def on_clicked_clear(self):
        global number_stack, operator_stack, last_clicked
        number_stack = [0, ]
        operator_stack = []
        self.result.setText(str(0))
        last_clicked = 'number'

    def on_clicked_operator(self):
        global last_clicked
        last_clicked = 'operator'
        new_op = str(self.sender().objectName())
        right_number = 0
        if len(number_stack) != 0:
            right_number = number_stack.pop()
        left_number = 0
        if len(number_stack) != 0:
            left_number = number_stack.pop()

        old_op = 'equal'
        if len(operator_stack) != 0:
            old_op = operator_stack.pop()

        if new_op == 'equal':
            if old_op == 'equal':
                self.result.setText(str(right_number))
                number_stack.append(right_number)
            else:
                answer = operate_two_numbers(left_number, right_number, old_op)
                self.result.setText(str(answer))
                number_stack.append(answer)

        elif new_op == 'add' or new_op == 'sub':
            operator_stack.append(new_op)
            if old_op != 'equal':
                answer = operate_two_numbers(left_number, right_number, old_op)
                self.result.setText(str(answer))
                number_stack.append(answer)
            else:
                number_stack.append(right_number)
        else:
            # 乘除
            operator_stack.append(new_op)
            if old_op == 'equal':
                self.result.setText(str(right_number))
                number_stack.append(right_number)
            elif old_op == 'multiply' or old_op == 'divide':
                answer = operate_two_numbers(left_number, right_number, old_op)
                self.result.setText(str(answer))
                number_stack.append(answer)
            else:
                self.result.setText(str(right_number))
                number_stack.append(left_number)
                number_stack.append(right_number)
                operator_stack.append(old_op)

    """
        响应点击数字
    """

    def on_clicked_number(self):
        global last_clicked

        number = numbers[str(self.sender().objectName())]
        if last_clicked == 'operator':
            number_stack.append(number)
            self.result.setText(str(number))
        else:
            right_number = number_stack.pop() * 10 + number
            number_stack.append(right_number)
            self.result.setText(str(right_number))
        last_clicked = 'number'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
