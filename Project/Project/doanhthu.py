
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
        self._year = 0
        #########################
        ### chỉ cho phép nhập chữ số của năm
        self.onlyInt = QIntValidator()
        self.ui.nam_lnedit.setValidator(self.onlyInt)
        #########################
        self.ui.table.setColumnCount(3)
        self.ui.table.setRowCount(0)
        # set column headers name for table "doanh thu"
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Thang"))        
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("So Luong Hoa Don"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("Doanh Thu"))
    def populateTable(self,hd):
        self.ui.table.insertRow(self.ui.table.rowCount())
        for i in range (len(hd)):           
            item = QTableWidgetItem(str(hd[i]))
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.table.setItem(self.ui.table.rowCount()-1,i,item)