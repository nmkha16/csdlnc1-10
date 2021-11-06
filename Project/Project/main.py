from os import _exit
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from ui_main import Ui_MainWindow
from themhoadon import ThemHoaDon

class gui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # button event
        self.ui.themhd_btn.clicked.connect(self.themHoaDonWidget)
    ################
    # Methods
    def themHoaDonWidget(self):
        self.themHoaDon = ThemHoaDon()
        self.themHoaDon.show()


if __name__=="__main__":
    app = QApplication()
    window = gui()
    window.show()
    exit(app.exec_())