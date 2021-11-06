
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QIntValidator)
from PySide2.QtWidgets import *

from ui_doanhthu import Ui_Form

class DoanhThu(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #########################
        ### chỉ cho phép nhập chữ số của năm
        self.onlyInt = QIntValidator()
        self.ui.nam_lnedit.setValidator(self.onlyInt)
        #########################
        # button event

        #######################
