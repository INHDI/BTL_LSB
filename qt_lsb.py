# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_lsb.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import giai_ma
import ma_hoa
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = ".\\platform\\"

class Ui_nhom1(object):
 
    #show cửa số giả mã ######################################################################
    def Giai_ma(self):
        self.window_giai_ma = QtWidgets.QMainWindow()
        self.ui = giai_ma.Ui_giai_ma()
        self.ui.setupUi(self.window_giai_ma)
        self.window_giai_ma.show()

    #show cửa số mã hóa ######################################################################
    def Ma_hoa(self):
        self.window_ma_hoa = QtWidgets.QMainWindow()
        self.ui = ma_hoa.Ui_ma_hoa()
        self.ui.setupUi(self.window_ma_hoa)
        self.window_ma_hoa.show()

    def setupUi(self, nhom1):
        nhom1.setObjectName("nhom1")
        nhom1.resize(525, 282)
        self.centralwidget = QtWidgets.QWidget(nhom1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 491, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        #mã hóa ####################################################################################
        self.ma_hoa = QtWidgets.QPushButton(self.centralwidget)
        self.ma_hoa.setGeometry(QtCore.QRect(300, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ma_hoa.setFont(font)
        self.ma_hoa.setObjectName("ma_hoa")
        self.ma_hoa.clicked.connect(self.Ma_hoa)
        self.ma_hoa.clicked.connect(nhom1.close)
        #giải mã ####################################################################################
        self.giai_ma = QtWidgets.QPushButton(self.centralwidget)
        self.giai_ma.setGeometry(QtCore.QRect(100, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.giai_ma.setFont(font)
        self.giai_ma.setObjectName("giai_ma")
        self.giai_ma.clicked.connect(self.Giai_ma)
        self.giai_ma.clicked.connect(nhom1.close)

        nhom1.setCentralWidget(self.centralwidget)

        self.retranslateUi(nhom1)
        QtCore.QMetaObject.connectSlotsByName(nhom1)

    def retranslateUi(self, nhom1):
        _translate = QtCore.QCoreApplication.translate
        nhom1.setWindowTitle(_translate("nhom1", "Nhóm 1 LSB"))
        self.label.setText(_translate("nhom1", "GIẤU TIN TRONG ẢNH MÀU BẰNG LSB"))
        self.label_2.setText(_translate("nhom1", "Nhóm 1"))
        self.ma_hoa.setText(_translate("nhom1", "Mã Hóa"))
        self.giai_ma.setText(_translate("nhom1", "Giải Mã"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    nhom1 = QtWidgets.QMainWindow()
    ui = Ui_nhom1()
    ui.setupUi(nhom1)
    nhom1.show()
    sys.exit(app.exec_())
