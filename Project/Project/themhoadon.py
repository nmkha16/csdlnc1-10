
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QStandardItemModel)
from PySide2.QtWidgets import *

from ui_themhoadon import Ui_Form

class ThemHoaDon(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.productID_Amount = {}
        self.productID_Price= {}
        self.productName_ID={}
        # button event
        self.ui.cancel_btn.clicked.connect(self._close)
        self.ui.listWidget.itemDoubleClicked.connect(self.removeItem)   # double click to remove
        self.ui.table.cellDoubleClicked.connect(self.chooseItem) #double click item to chose
        #######################

    def _close(self):
        self.close()

    def displaySanPham(self,sp):
        self.ui.table.setColumnCount(len(sp[0])-1)
        self.ui.table.setRowCount(len(sp))

        # set column headers name
        #['MaSP','TenSP','SoLuongTon','Mota','Gia']
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("MaSP"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("TenSP"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("SoLuongTon"))
        self.ui.table.setHorizontalHeaderItem(3,QTableWidgetItem("Gia"))
        for i in range (len(sp)):
            for j in range(len(sp[0])):
                if (j ==3):
                    continue
                if j == 4:
                    item = QTableWidgetItem(str(sp[i][j]))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.ui.table.setItem(i,j-1,item)
                    continue

                item = QTableWidgetItem(str(sp[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.table.setItem(i,j,item)
            
    def chooseItem(self):
        row = self.ui.table.currentRow()
        productID = self.ui.table.item(row,0).text()
        productName = self.ui.table.item(row,1).text()
        productPrice = self.ui.table.item(row,3).text()

        if (productID in self.productID_Amount):
            self.productID_Amount[productID] = str(int(self.productID_Amount.get(productID))+1)
            
        else:
            self.productID_Amount[productID] = '1'
            self.productID_Price[productID] = productPrice
            self.productName_ID[productName] = productID

        # add item to listWidget
        self.ui.listWidget.addItem(productName)

    def removeItem(self):
       row = self.ui.listWidget.currentRow()
       productName = self.ui.listWidget.item(row).text()
       self.ui.listWidget.takeItem(row)

       productID = self.productName_ID.get(productName)
       
       if (productID in self.productID_Amount):
           if (self.productID_Amount.get(productID) == '1'):
               self.productID_Amount.pop(productID,None)
               self.productID_Price.pop(productID,None)
               self.productName_ID.pop(productName,None)
           else:
               self.productID_Amount[productID] = str(int(self.productID_Amount.get(productID))-1)
