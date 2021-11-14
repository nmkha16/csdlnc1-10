
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from ui_danhsachhd import Ui_Form
from ui_chitiethoadon import Ui_Form

class DanhSachHD(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.selectedMaHD = 0
        # button event
        #######################
    def displayHD(self,hd):
        self.ui.table.setColumnCount(4)
        self.ui.table.setRowCount(len(hd))

        # set column headers name for table "Danh sách hoá đơn"
        #['MaHD','MaKH','NgayLap','TongTien']
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("MaHD"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("MaKH"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("NgayLap"))
        self.ui.table.setHorizontalHeaderItem(3,QTableWidgetItem("TongTien"))

        for i in range (len(hd)):
            for j in range(len(hd[0])):
                item = QTableWidgetItem(str(hd[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.table.setItem(i,j,item)


class CTHoaDon(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def displayCT(self,hd):
        self.ui.table.setColumnCount(6)
        self.ui.table.setRowCount(len(hd))

        # set column headers name for table "chi tiết hoá đơn"
        #['MaHD','MaSP','SoLuong','GiaBan','GiaGiam','TongTien']
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("MaHD"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("MaSP"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("SoLuong"))
        self.ui.table.setHorizontalHeaderItem(3,QTableWidgetItem("GiaBan"))
        self.ui.table.setHorizontalHeaderItem(4,QTableWidgetItem("GiaGiam"))
        self.ui.table.setHorizontalHeaderItem(5,QTableWidgetItem("ThanhTien"))


        for i in range (len(hd)):
            for j in range(len(hd[0])):
                item = QTableWidgetItem(str(hd[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.table.setItem(i,j,item)

