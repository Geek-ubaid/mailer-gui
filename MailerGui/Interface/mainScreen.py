# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 688)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(100, 10, 100, 10)
        self.gridLayout.setHorizontalSpacing(23)
        self.gridLayout.setObjectName("gridLayout")
        self.recipients_label = QtWidgets.QLineEdit(self.centralwidget)
        self.recipients_label.setMouseTracking(False)
        self.recipients_label.setReadOnly(True)
        self.recipients_label.setObjectName("recipients_label")
        self.gridLayout.addWidget(self.recipients_label, 0, 1, 1, 1)
        self.view_button = QtWidgets.QPushButton(self.centralwidget)
        self.view_button.setObjectName("view_button")
        self.gridLayout.addWidget(self.view_button, 0, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.extract_button = QtWidgets.QPushButton(self.centralwidget)
        self.extract_button.setObjectName("extract_button")
        self.gridLayout.addWidget(self.extract_button, 0, 2, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem, 18, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(100, 10, 100, 10)
        self.gridLayout_3.setHorizontalSpacing(23)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.reset_attachment_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_attachment_button.setObjectName("reset_attachment_button")
        self.gridLayout_3.addWidget(self.reset_attachment_button, 1, 3, 1, 1)
        self.attachment_label = QtWidgets.QLineEdit(self.centralwidget)
        self.attachment_label.setReadOnly(True)
        self.attachment_label.setObjectName("attachment_label")
        self.gridLayout_3.addWidget(self.attachment_label, 1, 1, 1, 1)
        self.attachment_button = QtWidgets.QPushButton(self.centralwidget)
        self.attachment_button.setObjectName("attachment_button")
        self.gridLayout_3.addWidget(self.attachment_button, 1, 2, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(100, 10, 100, 10)
        self.gridLayout_2.setHorizontalSpacing(40)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.subject_text = QtWidgets.QLineEdit(self.centralwidget)
        self.subject_text.setMaxLength(100000)
        self.subject_text.setObjectName("subject_text")
        self.gridLayout_2.addWidget(self.subject_text, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem1, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem2, 8, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem3, 14, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_7.setHorizontalSpacing(62)
        self.gridLayout_7.setVerticalSpacing(13)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.send_bulk_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.send_bulk_button.setFont(font)
        self.send_bulk_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send_bulk_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.send_bulk_button.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/logos/logo-mailer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_bulk_button.setIcon(icon)
        self.send_bulk_button.setObjectName("send_bulk_button")
        self.gridLayout_7.addWidget(self.send_bulk_button, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout_8.addLayout(self.gridLayout_7, 19, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem4, 20, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem5, 15, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox:title {\n"
"                 subcontrol-origin: margin;\n"
"                 subcontrol-position: top center;\n"
"                 padding-left: 10px;\n"
"                 padding-right: 10px; }")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setContentsMargins(100, 23, 100, 28)
        self.gridLayout_4.setHorizontalSpacing(23)
        self.gridLayout_4.setVerticalSpacing(42)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.test_email_label = QtWidgets.QLineEdit(self.groupBox)
        self.test_email_label.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.test_email_label.setObjectName("test_email_label")
        self.gridLayout_4.addWidget(self.test_email_label, 2, 0, 1, 1)
        self.test_send_button = QtWidgets.QPushButton(self.groupBox)
        self.test_send_button.setObjectName("test_send_button")
        self.gridLayout_4.addWidget(self.test_send_button, 2, 1, 1, 1)
        self.add_template_button = QtWidgets.QPushButton(self.groupBox)
        self.add_template_button.setObjectName("add_template_button")
        self.gridLayout_4.addWidget(self.add_template_button, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.edit_button = QtWidgets.QPushButton(self.groupBox)
        self.edit_button.setObjectName("edit_button")
        self.gridLayout_4.addWidget(self.edit_button, 1, 2, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox, 17, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setStyleSheet("QGroupBox:title {\n"
"                 subcontrol-origin: margin;\n"
"                 subcontrol-position: top center;\n"
"                 padding-left: 10px;\n"
"                 padding-right: 10px; }")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setContentsMargins(100, 22, 100, 22)
        self.gridLayout_5.setHorizontalSpacing(163)
        self.gridLayout_5.setVerticalSpacing(22)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.splitter_4 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setHandleWidth(11)
        self.splitter_4.setObjectName("splitter_4")
        self.label = QtWidgets.QLabel(self.splitter_4)
        self.label.setObjectName("label")
        self.placeholder_key = QtWidgets.QComboBox(self.splitter_4)
        self.placeholder_key.setStyleSheet("")
        self.placeholder_key.setObjectName("placeholder_key")
        self.placeholder_key.addItem("")
        self.gridLayout_5.addWidget(self.splitter_4, 0, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setHandleWidth(11)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(14)
        self.splitter.setObjectName("splitter")
        self.placeholder_value = QtWidgets.QComboBox(self.splitter)
        self.placeholder_value.setObjectName("placeholder_value")
        self.placeholder_value.addItem("")
        self.label_8 = QtWidgets.QLabel(self.splitter)
        self.label_8.setObjectName("label_8")
        self.custom_value = QtWidgets.QLineEdit(self.splitter)
        self.custom_value.setStyleSheet("")
        self.custom_value.setObjectName("custom_value")
        self.gridLayout_5.addWidget(self.splitter_2, 1, 0, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setHandleWidth(20)
        self.splitter_3.setObjectName("splitter_3")
        self.add_placeholder_button = QtWidgets.QPushButton(self.splitter_3)
        self.add_placeholder_button.setObjectName("add_placeholder_button")
        self.reset_placeholder_button = QtWidgets.QPushButton(self.splitter_3)
        self.reset_placeholder_button.setObjectName("reset_placeholder_button")
        self.gridLayout_5.addWidget(self.splitter_3, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.placeholder_view = QtWidgets.QListWidget(self.groupBox_2)
        self.placeholder_view.setStyleSheet("")
        self.placeholder_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.placeholder_view.setAlternatingRowColors(True)
        self.placeholder_view.setObjectName("placeholder_view")
        item = QtWidgets.QListWidgetItem()
        self.placeholder_view.addItem(item)
        self.gridLayout_5.addWidget(self.placeholder_view, 0, 1, 3, 1)
        self.gridLayout_8.addWidget(self.groupBox_2, 9, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 916, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuDownload = QtWidgets.QMenu(self.menuBar)
        self.menuDownload.setObjectName("menuDownload")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSample_Recipient = QtWidgets.QAction(MainWindow)
        self.actionSample_Recipient.setObjectName("actionSample_Recipient")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionLogs = QtWidgets.QAction(MainWindow)
        self.actionLogs.setObjectName("actionLogs")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionReset_Attachment = QtWidgets.QAction(MainWindow)
        self.actionReset_Attachment.setObjectName("actionReset_Attachment")
        self.actionReset_All = QtWidgets.QAction(MainWindow)
        self.actionReset_All.setObjectName("actionReset_All")
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionSettings)
        self.menuDownload.addSeparator()
        self.menuDownload.addAction(self.actionSample_Recipient)
        self.menuEdit.addAction(self.actionReset_Attachment)
        self.menuEdit.addAction(self.actionReset_All)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuDownload.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MailerGui"))
        self.recipients_label.setPlaceholderText(_translate("MainWindow", "File name will be displayed here"))
        self.view_button.setText(_translate("MainWindow", "View "))
        self.label_6.setText(_translate("MainWindow", "Add Recipients"))
        self.extract_button.setText(_translate("MainWindow", "Import"))
        self.label_7.setText(_translate("MainWindow", "Attachment     "))
        self.reset_attachment_button.setText(_translate("MainWindow", "Reset"))
        self.attachment_label.setPlaceholderText(_translate("MainWindow", "File name will be displayed here"))
        self.attachment_button.setText(_translate("MainWindow", "Attach"))
        self.subject_text.setPlaceholderText(_translate("MainWindow", "Add Subject here"))
        self.label_4.setText(_translate("MainWindow", "Add Subject"))
        self.send_bulk_button.setText(_translate("MainWindow", "Start Mailer"))
        self.groupBox.setTitle(_translate("MainWindow", "Template"))
        self.test_email_label.setPlaceholderText(_translate("MainWindow", "Add test email"))
        self.test_send_button.setText(_translate("MainWindow", "Send Test"))
        self.add_template_button.setText(_translate("MainWindow", "Add"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Template file name will be displayed here"))
        self.edit_button.setText(_translate("MainWindow", "View"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Placeholder"))
        self.label.setText(_translate("MainWindow", "Placeholder key"))
        self.placeholder_key.setItemText(0, _translate("MainWindow", "Select Key"))
        self.label_2.setText(_translate("MainWindow", "Placeholder value   "))
        self.placeholder_value.setItemText(0, _translate("MainWindow", "Select Value"))
        self.label_8.setText(_translate("MainWindow", "OR"))
        self.custom_value.setPlaceholderText(_translate("MainWindow", "Enter Custom Value"))
        self.add_placeholder_button.setText(_translate("MainWindow", "Add"))
        self.reset_placeholder_button.setText(_translate("MainWindow", "Reset"))
        __sortingEnabled = self.placeholder_view.isSortingEnabled()
        self.placeholder_view.setSortingEnabled(False)
        item = self.placeholder_view.item(0)
        item.setText(_translate("MainWindow", "None"))
        self.placeholder_view.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuDownload.setTitle(_translate("MainWindow", "Download"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionSample_Recipient.setText(_translate("MainWindow", "Sample Recipient"))
        self.actionSample_Recipient.setShortcut(_translate("MainWindow", "Ctrl+J"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionLogs.setText(_translate("MainWindow", "Logs"))
        self.actionLogs.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionSettings.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionReset_Attachment.setText(_translate("MainWindow", "Reset Attachment"))
        self.actionReset_Attachment.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionReset_All.setText(_translate("MainWindow", "Reset All"))
        self.actionReset_All.setShortcut(_translate("MainWindow", "Ctrl+R"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
