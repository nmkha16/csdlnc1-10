import pyodbc
import time
import threading
from os import _exit
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from ui_main import Ui_MainWindow
from themhoadon import ThemHoaDon
from danhsachhd import DanhSachHD
from doanhthu import DoanhThu

class gui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ### disable button
        self.ui.themhd_btn.setEnabled(False)
        self.ui.xemhd_btn.setEnabled(False)
        self.ui.tkdt_btn.setEnabled(False)
        # button event
        self.ui.themhd_btn.clicked.connect(self.themHoaDonWidget)   # nút thêm hoá đơn
        self.ui.xemhd_btn.clicked.connect(self.xemHDWidget)             # nút xem hoá đơn
        self.ui.tkdt_btn.clicked.connect(self.doanhThuWidget)             # nút doanh thu
        self.ui.pushButton.clicked.connect(self.connect)


    def connect(self):
        self.ui.messBox = QMessageBox()
        self.ui.messBox.setWindowTitle("Thông báo")
        self.ui.messBox.setWindowModality(Qt.NonModal)
        self.ui.messBox.show()

        conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=NMKHA;'
                         'Database=QLDT;'
                         'Trusted_Connection=yes;')
        self.query = conn.cursor() 
        self.ui.themhd_btn.setEnabled(True)
        self.ui.xemhd_btn.setEnabled(True)
        self.ui.tkdt_btn.setEnabled(True)   
        self.ui.pushButton.setEnabled(False)
        self.ui.messBox.setText("Kết nối thành công")
        
        #self.query.execute("SELECT * FROM GIAOVIEN WHERE PHAI = 'Nam'")
    ################s
    # Methods
    # Mở window mới cho Thêm hoá đơn
    def themHoaDonWidget(self):
        self.themHoaDon = ThemHoaDon()
        self.themHoaDon.show()

        self.connect()
        row = self.query.fetchone()
        list= [x for x in row]
        strg = ''.join(str(x) for x in list)
        #for i in self.query:
            #str+=i.cursor_description
        self.themHoaDon._print(strg)
    # Mở window mới cho xem danh sách hoá đơn
    def xemHDWidget(self):
        self.xemHD = DanhSachHD()
        self.xemHD.show()

    # Mở window mới cho doanh thu
    def doanhThuWidget(self):
        self.doanhThu = DoanhThu()
        self.doanhThu.show()
  


if __name__=="__main__":
    app = QApplication()
    window = gui()
    window.show()
    exit(app.exec_())