# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginwindow(object):


    def setupUi(self, loginwindow):
        loginwindow.setObjectName("loginwindow")
        loginwindow.resize(802, 391)
        self.title = QtWidgets.QLabel(loginwindow)
        self.title.setGeometry(QtCore.QRect(240, 60, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.username = QtWidgets.QLabel(loginwindow)
        self.username.setGeometry(QtCore.QRect(150, 160, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(loginwindow)
        self.password.setGeometry(QtCore.QRect(150, 230, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(loginwindow)
        self.login.setGeometry(QtCore.QRect(350, 310, 75, 23))
        self.login.setObjectName("login")
        self.reset = QtWidgets.QPushButton(loginwindow)
        self.reset.setGeometry(QtCore.QRect(470, 310, 75, 23))
        self.reset.setObjectName("reset")
        self.user = QtWidgets.QLineEdit(loginwindow)
        self.user.setGeometry(QtCore.QRect(380, 150, 151, 31))
        self.user.setObjectName("user")
        self.pass1 = QtWidgets.QLineEdit(loginwindow)
        self.pass1.setGeometry(QtCore.QRect(380, 220, 151, 31))
        self.pass1.setObjectName("pass1")
        self.pass1.setEchoMode(QtWidgets.QLineEdit.Password)


        self.retranslateUi(loginwindow)
        QtCore.QMetaObject.connectSlotsByName(loginwindow)

    def retranslateUi(self, loginwindow):
        _translate = QtCore.QCoreApplication.translate
        loginwindow.setWindowTitle(_translate("loginwindow", "Dialog"))
        self.title.setText(_translate("loginwindow", " LOGIN"))
        self.username.setText(_translate("loginwindow", "USERNAME"))
        self.password.setText(_translate("loginwindow", "PASSWORD"))
        self.login.setText(_translate("loginwindow", "OK"))
        self.reset.setText(_translate("loginwindow", "RESET"))





