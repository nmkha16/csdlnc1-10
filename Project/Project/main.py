import pyodbc
import random
from datetime import date
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from ui_main import Ui_MainWindow
from themhoadon import ThemHoaDon
from danhsachhd import DanhSachHD, CTHoaDon
from doanhthu import DoanhThu
from ui_ketnoi import Ui_Form


status = ""
indexHD = 0

class gui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # button event
        self.ui.themhd_btn.clicked.connect(self.themHoaDonWidget)   # nút thêm hoá đơn
        self.ui.xemhd_btn.clicked.connect(self.xemHDWidget)             # nút xem hoá đơn
        self.ui.tkdt_btn.clicked.connect(self.doanhThuWidget)             # nút doanh thu
        self.ui.pushButton.clicked.connect(self.ketNoiWidget)           # nút kết nối server

    
        
        #
    ################s
    # Methods
    # Mở window mới cho Thêm hoá đơn
    def themHoaDonWidget(self):
        if (status == "OK"):
            self.themHoaDon = ThemHoaDon()
            self.themHoaDon.show()

            
            self.ketNoi.query.execute("select TOP 2000 * from SanPham ")
            row = self.ketNoi.query.fetchall()
            strg = queryToList(row)         
            self.themHoaDon.displaySanPham(strg)

            self.themHoaDon.ui.ok_btn.clicked.connect(self.themHD)
    

    def themHD(self):
        self.ui.messBox = QMessageBox()
        self.ui.messBox.setWindowTitle("Thông báo")
        
        global indexHD
        indexHD+=1
        
        today = date.today().isoformat()
        try:
            #identity_insert on
            _str = "SET IDENTITY_INSERT HoaDon ON"
            self.ketNoi.query.execute(_str)
            #create a query for HOADON
            _str = "INSERT INTO HoaDon (MaHD,MaKH,NgayLap) VALUES (" + str(indexHD)+","
            _str+=self.themHoaDon.ui.makh_lnedit.text() +",'"
            _str+=today+"')"
            #print(_str)
            self.ketNoi.query.execute(_str)
            #identity_insert off
            _str = "SET IDENTITY_INSERT HoaDon OFF"
            self.ketNoi.query.execute(_str)
            self.ketNoi.query.commit()
            #create a qery for CT_HoaDon
            product = []
            for key,value in self.themHoaDon.productName_ID.items():
                tmp = []    
                tmp.append(value) #MaSP
                tmp.append(self.themHoaDon.productID_Amount[value]) # amount
                tmp.append(self.themHoaDon.productID_Price[value]) # price
                product.append(tmp)
        
            #create query for CT_HOADON
            _str = "INSERT INTO CT_HoaDon(MaHD,MaSP,SoLuong,GiaBan,GiaGiam) VALUES (" + str(indexHD)+","
        
            #product ['MaSP','SoLuong','GiaBan']
            for p in product:
                _str1 = _str
                _str1+= p[0]+","
                _str1+=p[1]+","
                _str1+=p[2]+","
                _str1+= str(random.randint(1000,30000))+")"
                print(_str1)
                self.ketNoi.query.execute(_str1)
            self.ketNoi.query.commit()
            self.ui.messBox.setText("Truy vấn thành công")

        except:
            self.ui.messBox.setText("Truy vấn thất bại")
            
        self.ui.messBox.show()

    # Mở window mới cho xem danh sách hoá đơn
    def xemHDWidget(self):
        if (status == "OK"):
            self.xemHD = DanhSachHD()
            self.xemHD.show()

            self.ketNoi.query.execute("Select top 2000 * from HoaDon")
            row = self.ketNoi.query.fetchall()
            strg = queryToList(row)
            
            self.xemHD.displayHD(strg)

            self.xemHD.ui.table.cellDoubleClicked.connect(self.displayCTHD)

    def displayCTHD(self):
        row = self.xemHD.ui.table.currentRow()
        self.xemHD.selectedMaHD = int(self.xemHD.ui.table.item(int(row),0).text())

        self.xemHD.CTHD = CTHoaDon()
        self.xemHD.CTHD.show()   
        #Create query
        _str = "Select top 2000* from CT_HoaDon where MaHD = " + str(self.xemHD.selectedMaHD)
        self.ketNoi.query.execute(_str)
        row = self.ketNoi.query.fetchall()
        strg = queryToList(row)

        self.xemHD.CTHD.displayCT(strg)
        


    # Mở window mới cho doanh thu
    def doanhThuWidget(self):
        if (status == "OK"):
            self.doanhThu = DoanhThu()
            self.doanhThu.ui.ok_btn.clicked.connect(self.displayDT)
            self.doanhThu.show()
            

    def displayDT(self):
        self.doanhThu.ui.table.setRowCount(0) #clear previous record
        self.doanhThu._year = self.doanhThu.ui.nam_lnedit.text()
        #create query
        for i in range(12):
            _str = "select * from HoaDon where year(NgayLap) = " +self.doanhThu._year + " and month(NgayLap) = " + str(i+1)
            self.ketNoi.query.execute(_str)
            row = self.ketNoi.query.fetchall()
            strg = queryToList(row)
            #store total of Hoa Don and Total of money
            #['Thang','SoLuongHoaDon','TongDoanhThu']
            DT =[]
            DT.append(str(i+1))
            #calculate total of HoaDon and total of money
            sum1=  0
            sum2= 0
            for x in strg:
                sum1+= 1
                try:
                    sum2+= x[3]
                except:
                    pass
            DT.append(str(sum1))
            DT.append(str(sum2))

            self.doanhThu.populateTable(DT)


    #Mở window kết nối
    def ketNoiWidget(self):
        self.ketNoi = KetNoi()
        self.ketNoi.show()


class KetNoi(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # button event
        self.ui.ok_btn_2.clicked.connect(self.connect)


    def connect(self):
        global status

        #self.sv = "NMKHA"
        #self.db = "DA1"

        self.sv = str(self.ui.tensv_lnedit.text())
        self.db = str(self.ui.tendb_lnedit.text())

        self.ui.messBox = QMessageBox()
        self.ui.messBox.setWindowTitle("Thông báo")
        self.ui.messBox.show()
        _str = (('Driver={0};'
                                'Server={1};'
                                'Database={2};'
                                'Trusted_Connection=yes;').format("SQL SERVER",self.sv,self.db))
        try:
            conn = pyodbc.connect(_str)
            
            self.query = conn.cursor()
        except:
            self.ui.messBox.setText("Kết nối không thành công")
            status =""
            return

        self.close()
        status = "OK"
        self.ui.messBox.setText("Kết nối thành công")
        global indexHD
        self.query.execute("SELECT TOP 1 (MaHD) FROM HoaDon ORDER BY MaHD DESC")
        row = self.query.fetchone()
        indexHD = row[0]


def queryToList(row):
    strg = []
    for i in row:
        tmp = []
        for j in i:
            tmp.append(j)
        strg.append(tmp) 
    return strg

if __name__=="__main__":
    app = QApplication()
    window = gui()
    window.show()
    exit(app.exec_())
