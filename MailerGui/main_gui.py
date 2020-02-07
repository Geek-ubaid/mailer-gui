import warnings
warnings.filterwarnings('ignore')

import os
import csv
import json


from dotenv import load_dotenv
import pandas as pd
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

#importing interface
from Screens import viewSummary
from Interface.login import Ui_loginwindow
from Interface.mainScreen import Ui_MainWindow 
from Interface import summaryScreen
from Interface import recipientScreen
from Screens.utils import mailto
from Screens.modelDataframe import PandasModel
from Interface import progressScreen
from Screens import test_send

load_dotenv()

LOGIN_NAME = os.getenv('LOGIN_NAME')
PASSKEY = os.getenv('PASSKEY')

print(LOGIN_NAME,PASSKEY)

YES = QtWidgets.QMessageBox.Yes
OK = QtWidgets.QMessageBox.Ok
CLOSE = QtWidgets.QMessageBox.Close


class Loginwindow(QtWidgets.QDialog,Ui_loginwindow):

    def __init__(self,parent=None):
        super(Loginwindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(r'gdg.png'))
        self.setWindowTitle("Developer Students Club")
        self.login.clicked.connect(self.login_check)
        self.reset.clicked.connect(self.reset_check)


    def login_check(self):
        
        passkey = self.pass1.text()
        username = self.user.text()
        
        if (username == LOGIN_NAME and passkey == PASSKEY):
            try:
                self.window = MainWindow()
                self.close()
                self.window.show()
            except:
                show_messagebox(2)
                self.reset_check()
                pass
        else:
            if(show_messagebox(1) == CLOSE):
                if(show_messagebox(4) == YES):
                    app.quit()
                else:
                    pass
                
    def reset_check(self):
        self.pass1.setText("")
        self.user.setText("")



def show_messagebox(x):
    
    """ This function is used to show the staus messages in the application"""
    
    message = QtWidgets.QMessageBox()
    message.setWindowTitle("Status Window")
    message.setIcon(QtWidgets.QMessageBox.Information)

    if x == 1:
        message.setText('Invalid Credentials')
        message.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close)
    elif x == 2:
        message.setText('Erorr in login!!')
        message.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 3:
        message.setText('Recipients added succesfully!')
        message.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 4:
        message.setText('Are you sure you wanna exit?')
        message.setIcon(QtWidgets.QMessageBox.Question)
        message.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    elif x == 5:
        message.setText('No File is selected!')
        message.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 6:
        message.setText('Size of file exceeded! Select another file')
        message.setIcon(QtWidgets.QMessageBox.Warning)
        message.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 7:
        message.setText('All Mail sent successfully')
        message.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 8:
        message.setText('Error reading recipients file!')
        message.setIcon(QtWidgets.QMessageBox.Warning)
        message.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 9:
        message.setText('No attachment is selected!')
        message.setIcon(QtWidgets.QMessageBox.Warning)
        message.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 10:
        message.setText('Template added succesfully!')
        message.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 11:
        message.setText('Tick the verify box before sending!!')
        message.setIcon(QtWidgets.QMessageBox.Warning)
        message.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif x == 12:
        message.setText('Test mail sent succesfully!')
        message.setStandardButtons(QtWidgets.QMessageBox.Ok)
    return message.exec_()
    


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        
        super(MainWindow, self).__init__(parent)
        self.recipient_file = ''
        self.attachment_file = ''
        self.template_file = ''
        self.subject = ''
        self.recipients_df = ''
        
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(r'gdg.png'))
        self.setWindowTitle("MailerGUI")
        self.recipients_label.setText(self.recipient_file)
        self.attachment_label.setText(self.attachment_file)
        self.lineEdit.setText(self.template_file)
        self.extract_button.clicked.connect(self.extract_recipients)
        self.attachment_button.clicked.connect(self.get_attachment_file)
        self.view_button.clicked.connect(self.show_recipients)
        self.add_template_button.clicked.connect(self.get_template_file)
        self.edit_button.clicked.connect(self.view_html_file)
        self.send_bulk_button.clicked.connect(self.show_summary)
        self.test_send_button.clicked.connect(self.send_test_mail)
        # self.send_email.clicked.connect(self.sendmail)
        
        finish = QtWidgets.QAction("Quit",self)
        finish.triggered.connect(self.close_window)

    def close_window(self, event):
        
        if show_messagebox(4) == YES :
            event.accept()         
        else:
            event.ignore()
            self.close()

    def view_html_file(self):
     
        self.web = QWebView()
        self.web.load(QUrl.fromLocalFile(self.template_file))
        self.web.show()
                    
    def show_summary(self):
        
        summary = viewSummary.GenerateSummary()
        total_recipient = summary.return_total_recipients(self.recipients_df)
        placeholders = summary.return_placeholder_text(self.placeholder_text.toPlainText())
        template_file = os.path.basename(self.template_file)
        subject = self.subject_text.text()
        attachment_file = os.path.basename(self.attachment_file)
        
        self.summary_window = SummaryScreen(template_file=template_file, \
                        placeholder=placeholders,\
                        total_recipient=total_recipient,\
                        subject=subject,\
                        attachment_file=attachment_file)
        self.summary_window.show()
        
            
    def show_recipients(self):
           
        self.recipient_window = RecipientWindow(self.recipients_df)
        self.recipient_window.exec_()
          
        
    def get_template_file(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.template_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, \
            "Select File to upload", "","HTML Files (*.html)", options=options)
                
        if (self.template_file.endswith('.html')):      
            file_name = os.path.basename(self.template_file)        
            show_messagebox(10)
            self.lineEdit.setText(file_name)
        else:
            show_messagebox(5)
        

    def get_attachment_file(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.attachment_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, \
            "Select File to upload", "","All Files (*)", options=options)
        if self.attachment_file:
            try:
                file_name = os.path.basename(self.attachment_file)
                file_size=os.path.getsize(self.attachment_file)
                if (file_size> 26214400):
                    show_messagebox(6)
                else:
                    self.attachment_label.setText(file_name)
            except:
                show_messagebox(9)
        else:
            show_messagebox(9)                


    def extract_recipients(self):
    
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.recipient_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, \
            "Select File to upload", "","CSV Files (*.csv)", options=options)
                
        if (self.recipient_file.endswith('.csv')):      
            file_name = os.path.basename(self.recipient_file)
            try:
                self.recipients_df = pd.read_csv(self.recipient_file)            
            except:
                show_messagebox(8)
            
            show_messagebox(3)
            self.recipients_label.setText(file_name)
        else:
            show_messagebox(5)
    
    def send_test_mail(self):
        
        to_mail = self.test_email_label.text() 
        message = open(self.template_file).read()
        res = test_send.send_complex_message(to_mail,"dscvitvellore@gmail.com",self.subject_text.text(),\
            message)
        
        if (res.status_code == 200):
            show_messagebox(12)
        
        

class RecipientWindow(recipientScreen.Ui_Dialog,QtWidgets.QDialog):
    
    def __init__(self,dataframe):
        
        super(RecipientWindow,self).__init__()
        self.setupUi(self)
        model = PandasModel(dataframe)
        self.recipients_view_box.setModel(model)
        finish = QtWidgets.QAction("Quit",self)
        finish.triggered.connect(self.close_window)
        
    def close_window(self):
        
        self.close()
        window = MainWindow()
        window.show()
    
class SummaryScreen(QtWidgets.QDialog,summaryScreen.Ui_Dialog):
    
    def __init__(self,**kwargs):
        
        super(SummaryScreen,self).__init__()
        self.setupUi(self)
        self.items = kwargs
        self.set_table_items()
        self.send_mail_button.clicked.connect(self.send_mail_bulk)
        
    def set_table_items(self):
            
        self.attachment_file = self.items['attachment_file']
        self.subject = self.items['subject']
        self.template_file = self.items ['template_file']
        self.placeholder = self.items['placeholder']
        self.total_recipient = self.items['total_recipient']
        
        item = QtWidgets.QTableWidgetItem(str(self.template_file)) 
        self.summary_table.setItem(0,1,item)
        item = QtWidgets.QTableWidgetItem(str(self.placeholder))
        self.summary_table.setItem(1,1,item)
        item = QtWidgets.QTableWidgetItem(str(self.total_recipient))
        self.summary_table.setItem(2,1,item)
        item = QtWidgets.QTableWidgetItem(str(self.subject))
        self.summary_table.setItem(3,1,item)
        item = QtWidgets.QTableWidgetItem(str(self.attachment_file))
        self.summary_table.setItem(4,1,item)
    
    def send_mail_bulk(self):
        
        if self.verify_box.isChecked():
            print('starting')
            
        else:
            show_messagebox(11)
        
        
        

if __name__ == '__main__':
    
    import sys
    global app
    app = QtWidgets.QApplication(sys.argv)
    window= Loginwindow()
    window.show()
    sys.exit(app.exec_())
