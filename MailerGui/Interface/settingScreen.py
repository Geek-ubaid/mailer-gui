# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(746, 512)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 701, 361))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.username_box = QtWidgets.QLineEdit(self.groupBox)
        self.username_box.setGeometry(QtCore.QRect(30, 40, 221, 31))
        self.username_box.setObjectName("username_box")
        self.password_box = QtWidgets.QLineEdit(self.groupBox)
        self.password_box.setGeometry(QtCore.QRect(340, 40, 221, 31))
        self.password_box.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password_box.setObjectName("password_box")
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.sendgrid_check = QtWidgets.QRadioButton(self.groupBox_2)
        self.sendgrid_check.setGeometry(QtCore.QRect(50, 50, 201, 31))
        self.sendgrid_check.setObjectName("sendgrid_check")
        self.mailgun_check = QtWidgets.QRadioButton(self.groupBox_2)
        self.mailgun_check.setGeometry(QtCore.QRect(350, 50, 201, 31))
        self.mailgun_check.setObjectName("mailgun_check")
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.apikey_box = QtWidgets.QLineEdit(self.groupBox_3)
        self.apikey_box.setGeometry(QtCore.QRect(30, 50, 221, 31))
        self.apikey_box.setObjectName("apikey_box")
        self.domain_box = QtWidgets.QLineEdit(self.groupBox_3)
        self.domain_box.setGeometry(QtCore.QRect(340, 50, 221, 31))
        self.domain_box.setObjectName("domain_box")
        self.verticalLayout.addWidget(self.groupBox_3)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(470, 470, 239, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.apply_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.apply_button.setObjectName("apply_button")
        self.gridLayout.addWidget(self.apply_button, 0, 2, 1, 1)
        self.ok_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.ok_button.setObjectName("ok_button")
        self.gridLayout.addWidget(self.ok_button, 0, 0, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.groupBox.setTitle(_translate("Dialog", "Login Credentials"))
        self.username_box.setPlaceholderText(_translate("Dialog", "Enter Username"))
        self.password_box.setPlaceholderText(_translate("Dialog", "Enter Password Here"))
        self.groupBox_2.setTitle(_translate("Dialog", "Choose Mail Provider"))
        self.sendgrid_check.setText(_translate("Dialog", "Sendgrid"))
        self.mailgun_check.setText(_translate("Dialog", "MailGun"))
        self.groupBox_3.setTitle(_translate("Dialog", "Mail Provider Credentials"))
        self.apikey_box.setPlaceholderText(_translate("Dialog", "Enter API Key"))
        self.domain_box.setPlaceholderText(_translate("Dialog", "Enter Mail Domain"))
        self.apply_button.setText(_translate("Dialog", "Apply"))
        self.ok_button.setText(_translate("Dialog", "OK"))
        self.cancel_button.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
