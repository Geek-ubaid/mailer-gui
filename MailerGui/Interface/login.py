# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginwindow(object):
    def setupUi(self, loginwindow):
        loginwindow.setObjectName("loginwindow")
        loginwindow.resize(828, 480)
        self.groupBox = QtWidgets.QGroupBox(loginwindow)
        self.groupBox.setGeometry(QtCore.QRect(90, 130, 611, 271))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.password_text = QtWidgets.QLineEdit(self.groupBox)
        self.password_text.setGeometry(QtCore.QRect(320, 110, 151, 31))
        self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_text.setObjectName("password_text")
        self.reset = QtWidgets.QPushButton(self.groupBox)
        self.reset.setGeometry(QtCore.QRect(410, 200, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reset.setFont(font)
        self.reset.setObjectName("reset")
        self.user = QtWidgets.QLineEdit(self.groupBox)
        self.user.setGeometry(QtCore.QRect(320, 40, 151, 31))
        self.user.setObjectName("user")
        self.login = QtWidgets.QPushButton(self.groupBox)
        self.login.setGeometry(QtCore.QRect(290, 200, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.username = QtWidgets.QLabel(self.groupBox)
        self.username.setGeometry(QtCore.QRect(90, 50, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(self.groupBox)
        self.password.setGeometry(QtCore.QRect(90, 120, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setObjectName("password_text")
        self.widget = QtWidgets.QWidget(loginwindow)
        self.widget.setGeometry(QtCore.QRect(240, 30, 371, 72))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(31, 0, 28, 0)
        self.gridLayout.setHorizontalSpacing(29)
        self.gridLayout.setVerticalSpacing(17)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Data/logo-mailer.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.retranslateUi(loginwindow)
        QtCore.QMetaObject.connectSlotsByName(loginwindow)

    def retranslateUi(self, loginwindow):
        _translate = QtCore.QCoreApplication.translate
        loginwindow.setWindowTitle(_translate("loginwindow", "Dialog"))
        self.groupBox.setTitle(_translate("loginwindow", "LOGIN"))
        self.reset.setText(_translate("loginwindow", "RESET"))
        self.login.setText(_translate("loginwindow", "OK"))
        self.username.setText(_translate("loginwindow", "USERNAME"))
        self.password.setText(_translate("loginwindow", "PASSWORD"))
        self.label_2.setText(_translate("loginwindow", "MailerGUI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginwindow = QtWidgets.QDialog()
    ui = Ui_loginwindow()
    ui.setupUi(loginwindow)
    loginwindow.show()
    sys.exit(app.exec_())
