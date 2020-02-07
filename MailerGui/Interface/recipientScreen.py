# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recipients.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 494)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(9, 9, 166, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.recipients_view_box = QtWidgets.QTableView(Dialog)
        self.recipients_view_box.setGeometry(QtCore.QRect(9, 39, 621, 441))
        self.recipients_view_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.recipients_view_box.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.recipients_view_box.setObjectName("recipients_view_box")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Recipients details"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
