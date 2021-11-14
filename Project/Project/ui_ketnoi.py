# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ketnoiiIvQuh.ui'
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
        Form.resize(271, 132)
        Form.setStyleSheet(u"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.tendb_lnedit = QLineEdit(self.frame)
        self.tendb_lnedit.setObjectName(u"tendb_lnedit")
        self.tendb_lnedit.setStyleSheet(u"QLineEdit{\n"
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
        self.tendb_lnedit.setReadOnly(False)

        self.gridLayout.addWidget(self.tendb_lnedit, 1, 1, 1, 2)

        self.tensv_lnedit = QLineEdit(self.frame)
        self.tensv_lnedit.setObjectName(u"tensv_lnedit")
        self.tensv_lnedit.setStyleSheet(u"QLineEdit{\n"
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
        self.tensv_lnedit.setReadOnly(False)

        self.gridLayout.addWidget(self.tensv_lnedit, 0, 1, 1, 2)

        self.ok_btn_2 = QPushButton(self.frame)
        self.ok_btn_2.setObjectName(u"ok_btn_2")
        self.ok_btn_2.setStyleSheet(u"QPushButton\n"
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

        self.gridLayout.addWidget(self.ok_btn_2, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"K\u1ebft n\u1ed1i", None))
        self.label.setText(QCoreApplication.translate("Form", u"T\u00ean server", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"T\u00ean database", None))
        self.ok_btn_2.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi

