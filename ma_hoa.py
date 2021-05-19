# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ma_hoa.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
import qt_lsb
import os
import backend
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = ".\\platform\\"

class Ui_ma_hoa(object):

    def showhome(self):
        self.window_back = QtWidgets.QMainWindow()
        self.ui = qt_lsb.Ui_nhom1()
        self.ui.setupUi(self.window_back)
        self.window_back.show()

    def setupUi(self, ma_hoa):
        ma_hoa.setObjectName("ma_hoa")
        ma_hoa.resize(537, 357)
        self.centralwidget = QtWidgets.QWidget(ma_hoa)
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 100, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 140, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 170, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        # Nhập file ảnh ############################################################################
        self.in_anh = QtWidgets.QLineEdit(self.centralwidget)
        self.in_anh.setGeometry(QtCore.QRect(190, 130, 201, 31))
        self.in_anh.setObjectName("in_anh")
        # Nhập file tin giấu ############################################################################
        self.in_file = QtWidgets.QLineEdit(self.centralwidget)
        self.in_file.setGeometry(QtCore.QRect(190, 170, 201, 31))
        self.in_file.setObjectName("in_file")
        # Bắt đầu ############################################################################
        self.bat_dau = QtWidgets.QPushButton(self.centralwidget)
        self.bat_dau.setGeometry(QtCore.QRect(310, 230, 75, 23))
        self.bat_dau.setObjectName("bat_dau")
        self.bat_dau.clicked.connect(self.backend_mahoa)
        # Quay lại ############################################################################
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(180, 230, 75, 23))
        self.back.setObjectName("back")
        self.back.clicked.connect(self.showhome)
        self.back.clicked.connect(ma_hoa.close)       

        ma_hoa.setCentralWidget(self.centralwidget)
        self.retranslateUi(ma_hoa)
        QtCore.QMetaObject.connectSlotsByName(ma_hoa)
    

###############################################################################################
    def backend_mahoa(self):
        print("Mã hóa")
        in_f=self.in_anh.text() # ảnh đầu vào 
        out_f= "anh_da_ma_hoa"# ảnh đầu ra 
        print(in_f)
        in_img = cv2.imread(in_f)
        steg = backend.LSBSteg(in_img)
        lossy_formats = ["jpeg", "jpg"]
        # cv2.imshow('Display Image', in_img)
        ###############################################################)

        out_f = out_f + ".png"
        print("Output file changed to ", out_f)
        #################################################################
        in_code= self.in_file.text()
        data = open(in_code, "rb").read()
        res = steg.encode_binary(data)
        cv2.imwrite(out_f, res)

        
###############################################################################################
    def retranslateUi(self, ma_hoa):
        _translate = QtCore.QCoreApplication.translate
        ma_hoa.setWindowTitle(_translate("ma_hoa", "Mã Hóa"))
        self.label.setText(_translate("ma_hoa", "GIẤU TIN TRONG ẢNH MÀU BẰNG LSB"))
        self.label_2.setText(_translate("ma_hoa", "Nhóm 1"))
        self.label_3.setText(_translate("ma_hoa", "MÃ HÓA"))
        self.label_4.setText(_translate("ma_hoa", "Ảnh"))
        self.label_5.setText(_translate("ma_hoa", "Tin giấu"))
        self.bat_dau.setText(_translate("ma_hoa", "Mã Hóa"))
        self.back.setText(_translate("ma_hoa", "Quay Lại"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ma_hoa = QtWidgets.QMainWindow()
    ui = Ui_ma_hoa()
    ui.setupUi(ma_hoa)
    ma_hoa.show()
    sys.exit(app.exec_())
