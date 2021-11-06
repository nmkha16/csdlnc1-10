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
        # button event
        self.ui.themhd_btn.clicked.connect(self.themHoaDonWidget)   # nút thêm hoá đơn
        self.ui.xemhd_btn.clicked.connect(self.xemHDWidget)             # nút xem hoá đơn
        self.ui.tkdt_btn.clicked.connect(self.doanhThuWidget)             # nút doanh thu


    ################s
    # Methods
    # Mở window mới cho Thêm hoá đơn
    def themHoaDonWidget(self):
        self.themHoaDon = ThemHoaDon()
        self.themHoaDon.show()

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