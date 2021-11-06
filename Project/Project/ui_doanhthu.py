# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doanhthuunNcNh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(463, 378)
        Form.setStyleSheet(u"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalFrame = QFrame(Form)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.gridLayout = QGridLayout(self.horizontalFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.horizontalFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.nam_lbl = QLabel(self.horizontalFrame)
        self.nam_lbl.setObjectName(u"nam_lbl")
        font1 = QFont()
        font1.setPointSize(12)
        self.nam_lbl.setFont(font1)

        self.gridLayout.addWidget(self.nam_lbl, 1, 0, 1, 1)

        self.nam_lnedit = QLineEdit(self.horizontalFrame)
        self.nam_lnedit.setObjectName(u"nam_lnedit")
        self.nam_lnedit.setFont(font1)
        self.nam_lnedit.setStyleSheet(u"QLineEdit{\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border-color: #cc8400\n"
"}")
        self.nam_lnedit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.nam_lnedit, 1, 1, 1, 1)

        self.ok_btn = QPushButton(self.horizontalFrame)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setStyleSheet(u"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-color: #cc8400\n"
"}")

        self.gridLayout.addWidget(self.ok_btn, 1, 2, 1, 1)

        self.table = QTableWidget(self.horizontalFrame)
        if (self.table.columnCount() < 2):
            self.table.setColumnCount(2)
        if (self.table.rowCount() < 3):
            self.table.setRowCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setItem(0, 0, __qtablewidgetitem)
        self.table.setObjectName(u"table")
        self.table.setStyleSheet(u"QTableWidget{\n"
"color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"}\n"
"\n"
"QTableWidget:item::pressed{\n"
"    border-color: #1e1e1e;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"     background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"}\n"
"QHeaderView, QHeaderView::section {\n"
"    background-color: rgba(128, 128, 128, 128);\n"
"}")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(False)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setGridStyle(Qt.SolidLine)
        self.table.setCornerButtonEnabled(True)
        self.table.setRowCount(3)
        self.table.setColumnCount(2)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.horizontalHeader().setStretchLastSection(False)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.table, 2, 0, 1, 3)


        self.verticalLayout_2.addWidget(self.horizontalFrame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Doanh thu theo th\u00e1ng", None))
        self.label.setText(QCoreApplication.translate("Form", u"Doanh thu", None))
        self.nam_lbl.setText(QCoreApplication.translate("Form", u"N\u0103m", None))
        self.nam_lnedit.setInputMask("")
        self.ok_btn.setText(QCoreApplication.translate("Form", u"OK", None))

        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        self.table.setSortingEnabled(__sortingEnabled)

    # retranslateUi

