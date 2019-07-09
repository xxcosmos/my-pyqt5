from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QIcon, QPixmap
import assets.demo


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label_2 = QLabel(self)
        label_2.setGeometry(0, 0, 61, 61)
        label_2.setPixmap(QPixmap("google-translator/google.png"))
        label_2.setScaledContents(True)
        # QAction是菜单栏、工具栏或者快捷键的动作的组合
        exit_act = QAction(QIcon('assets/image.jpg'), '&Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('退出程序')
        exit_act.triggered.connect(qApp.quit)

        self.statusBar().showMessage('Ready')
        # 拿到menuBar
        menubar = self.menuBar()
        view_menu = menubar.addMenu('View')

        # 新建行为菜单，可选中，默认选中
        view_stat_act = QAction('View statusbar', self, checkable=True)
        view_stat_act.setChecked(True)

        view_stat_act.setStatusTip('view statusbar')
        view_stat_act.triggered.connect(self.toggle_menu)
        view_menu.addAction(view_stat_act)

        # 在menuBar上添加子菜单
        file_menu = menubar.addMenu('File')
        # 新建QMenu
        imp_menu = QMenu('Import', self)
        # 新建动作
        imp_act = QAction('Import mail', self)
        new_act = QAction('New', self)
        # menu中添加动作
        imp_menu.addAction(imp_act)
        file_menu.addAction(new_act)

        file_menu.addMenu(imp_menu)

        # self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Hello')
        self.show()

    """
    :param state 状态
    """

    def toggle_menu(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    # ex = assets.Ui_Form()

    # main_window = QMainWindow()
    # ui = assets.demo.Ui_Form()
    # ui.setupUi(main_window)
    # main_window.show()
    sys.exit(app.exec_())
