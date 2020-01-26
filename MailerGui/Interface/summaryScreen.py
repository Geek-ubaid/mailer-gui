# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'summary.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 435)
        self.summary_table = QtWidgets.QTableWidget(Dialog)
        self.summary_table.setGeometry(QtCore.QRect(9, 9, 621, 421))
        self.summary_table.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.summary_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.summary_table.setFrameShape(QtWidgets.QFrame.Panel)
        self.summary_table.setAlternatingRowColors(True)
        self.summary_table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.summary_table.setGridStyle(QtCore.Qt.SolidLine)
        self.summary_table.setRowCount(5)
        self.summary_table.setColumnCount(2)
        self.summary_table.setObjectName("summary_table")
        item = QtWidgets.QTableWidgetItem()
        self.summary_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.summary_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.summary_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.summary_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.summary_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.summary_table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.summary_table.setItem(4, 0, item)
        self.summary_table.horizontalHeader().setVisible(False)
        self.summary_table.horizontalHeader().setCascadingSectionResizes(False)
        self.summary_table.horizontalHeader().setDefaultSectionSize(127)
        self.summary_table.horizontalHeader().setHighlightSections(False)
        self.summary_table.horizontalHeader().setSortIndicatorShown(False)
        self.summary_table.horizontalHeader().setStretchLastSection(True)
        self.summary_table.verticalHeader().setVisible(False)
        self.summary_table.verticalHeader().setCascadingSectionResizes(True)
        self.summary_table.verticalHeader().setDefaultSectionSize(82)
        self.summary_table.verticalHeader().setMinimumSectionSize(23)
        self.summary_table.verticalHeader().setSortIndicatorShown(False)
        self.summary_table.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.summary_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Entity"))
        item = self.summary_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Value"))
        __sortingEnabled = self.summary_table.isSortingEnabled()
        self.summary_table.setSortingEnabled(False)
        item = self.summary_table.item(0, 0)
        item.setText(_translate("Dialog", "Template"))
        item = self.summary_table.item(1, 0)
        item.setText(_translate("Dialog", "Placeholder"))
        item = self.summary_table.item(2, 0)
        item.setText(_translate("Dialog", "Total Recipients"))
        item = self.summary_table.item(3, 0)
        item.setText(_translate("Dialog", "Subject"))
        item = self.summary_table.item(4, 0)
        item.setText(_translate("Dialog", "Attachment"))
        self.summary_table.setSortingEnabled(__sortingEnabled)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
