# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 200)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.warning_no_A = QtWidgets.QLabel(Dialog)
        self.warning_no_A.setGeometry(QtCore.QRect(70, 30, 260, 60))
        font = QtGui.QFont()
        font.setFamily("张海山锐谐体")
        font.setPointSize(12)
        self.warning_no_A.setFont(font)
        self.warning_no_A.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_no_A.setObjectName("warning_correct")
        self.ok_Button = QtWidgets.QPushButton(Dialog)
        self.ok_Button.setGeometry(QtCore.QRect(150, 130, 100, 40))
        font = QtGui.QFont()
        font.setFamily("张海山锐谐体")
        font.setPointSize(12)
        self.ok_Button.setFont(font)
        self.ok_Button.setObjectName("ok_Button")

        self.retranslateUi(Dialog)
        self.ok_Button.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.warning_no_A.setText(_translate("Dialog", "等式已成立，请重新输入！"))
        self.ok_Button.setText(_translate("Dialog", "知道啦"))

