import warnings
warnings.filterwarnings('ignore')

import os
import sys
import csv
import json
import logging
import datetime

import qdarkstyle
import pandas as pd
import jinja2schema
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebKit import *
from PyQt5.QtWidgets import *
from dotenv import load_dotenv
from jinja2 import Environment, BaseLoader 
from PyQt5.QtWebKitWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

#importing interface
from Interface.login import Ui_loginwindow
from Interface.mainScreen import Ui_MainWindow 
from Interface import summaryScreen
from Interface import recipientScreen
from Interface import progressScreen
from Interface import settingScreen
from Interface import beginScreen
from Screens import viewSummary
from Screens import Send_test
from Screens.utils import mailto
from Screens.Model_dataframe import PandasModel
from Screens.Store_credentials import StoreCredentials

load_dotenv()

YES = QtWidgets.QMessageBox.Yes
OK = QtWidgets.QMessageBox.Ok
NO = QtWidgets.QMessageBox.No

def show_warning_message(message_text):
    
    """ This function to show warning message dialog box"""
    
    message = QtWidgets.QMessageBox()
    message.setWindowTitle("Status Window")
    message.setText(str(message_text))
    message.setIcon(QtWidgets.QMessageBox.Warning)
    message.setStandardButtons(QtWidgets.QMessageBox.Ok)
    return message.exec_()

def show_information_message(message_text):
    
    """ This function to show information message dialog box"""

    message = QtWidgets.QMessageBox()
    message.setWindowTitle("Status Window")
    message.setIcon(QtWidgets.QMessageBox.Information)
    message.setText(str(message_text))
    message.setStandardButtons(QtWidgets.QMessageBox.Ok)
    return message.exec_()

def show_question_message(message_text):
    
    """ This function to show question message dialog box"""

    message = QtWidgets.QMessageBox()
    message.setWindowTitle("Status Window")
    message.setText(str(message_text))
    message.setIcon(QtWidgets.QMessageBox.Question)
    message.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    return message.exec_()

class SetupWindow(QtWidgets.QDialog,beginScreen.Ui_Dialog):
    
    """ This class if for changing the settings of the mailer """
    
    def __init__(self):
        super(SetupWindow,self).__init__(parent=None)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(r'Assets\Icons\logo-mailer.png'))
        self.setWindowTitle("Welcome to MailerGUI")
        self.start_button.clicked.connect(self.check_settings_button)
        finish = QtWidgets.QAction("Quit",self)
        finish.triggered.connect(self.close_window)
    
    def show_settings(self):
        details = {'fromemail' : self.from_username.text()}
        setting_window = SettingScreen(0, details)
        self.close()
        setting_window.exec_()
        
    def check_settings_button(self):
        if self.start_button.objectName() == "start_button":
            self.change_frame()
        else:
            self.show_settings()
    
    def change_frame(self):
        
        self.start_button.setText("Finish Up Settings")
        self.start_button.setObjectName('Settings_button')
        self.create_from_username()
    
    def create_from_username(self):
        
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setContentsMargins(100, -1, 100, -1)
        self.gridLayout_7.setHorizontalSpacing(71)
        self.gridLayout_7.setObjectName("gridLayout_4")
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_4")
        self.label_3.setText("Enter Organization Mail")
        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)
        self.from_username = QLineEdit(self.frame_2)
        self.from_username.setObjectName("from_username")
        self.from_username.setPlaceholderText("Enter email")
        self.gridLayout_7.addWidget(self.from_username, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_7, 0, 0, 1, 1)
       
    
    def close_window(self):
        global app
        sys.exit(app.exec_())
        
class Loginwindow(QtWidgets.QDialog,Ui_loginwindow):
    
    """ This Class is for login and authentication of user """

    def __init__(self,parent=None):
        super(Loginwindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(r'Assets\Icons\logo-mailer.png'))
        self.login.clicked.connect(self.login_check)
        self.reset.clicked.connect(self.reset_check)
        finish = QtWidgets.QAction("Quit",self)
        finish.triggered.connect(self.close_window)
        
    def check_for_settings(self):
        
        store_creds = StoreCredentials()
        response =  store_creds.check_for_creds_db()
        return response
            
    def check_for_saved_password(self):
        
        settings = QSettings()
        check_state = settings.value('settings/username','admin', type=str)
        return check_state
    
    def save_password_settings(self, username, password):
        
        settings = QSettings()
        settings.setValue('settings/username', username)
        settings.setValue('settings/password', password) 
        settings.sync()
    
    def login_check(self):
        
        if print(self.check_for_saved_password()):
            print('settings saveed!')
        
        LOGIN_NAME = os.getenv('LOGIN_NAME')
        PASSKEY = os.getenv('PASSKEY')
        passkey = self.password_text_box.text()
        username = self.username_text_box.text()
        print(passkey,username)
        if (username == LOGIN_NAME and passkey == PASSKEY):
            if self.forget_password.isChecked() == True:
                self.save_password_settings(username,passkey)
            try:
                self.window = MainWindow()
                self.close()
                self.window.show()
            except:
                show_warning_message('Erorr in login!!')
                self.reset_check()
                pass
        else:
            if(show_question_message('Invalid Credentials! Do you want to enter again?') == NO):
                if(show_question_message('Do you want to quit?') == YES):
                    app.quit()
                else:
                    pass
                
    def reset_check(self):
        self.password_text.setText("")
        self.user.setText("")
    
    def close_window(self):
        global app
        sys.exit()
   
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    """ This is the main interface for the sending bulk mail """ 

    def __init__(self,parent=None):
        
        super(MainWindow, self).__init__(parent)
        self.recipient_file = ''
        self.attachment_file = ''
        self.template_file = ''
        self.subject = ''
        self.recipients_df = ''
        self.dynamic_placeholder = []   
            
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(r'Assets\Icons\logo-mailer.png'))
        self.setWindowTitle("MailerGUI")
        self.recipients_label.setText(self.recipient_file)
        self.attachment_label.setText(self.attachment_file)
        self.lineEdit.setText(self.template_file)
        self.extract_button.clicked.connect(self.extract_recipients)
        self.attachment_button.clicked.connect(self.get_attachment_file)
        self.reset_attachment_button.clicked.connect(self.reset_attachment_file)
        self.view_button.clicked.connect(self.show_recipients)
        self.add_template_button.clicked.connect(self.get_template_file)
        self.edit_button.clicked.connect(self.view_html_file)
        self.send_bulk_button.clicked.connect(self.show_summary)
        self.test_send_button.clicked.connect(self.send_test_mail)
        self.actionSettings.triggered.connect(self.show_settings)
        self.actionQuit.triggered.connect(self.close_window)
        self.actionSample_Recipient.triggered.connect(self.show_sample_csv)
        self.actionReset_Attachment.triggered.connect(self.reset_attachment_file)
        self.actionReset_All.triggered.connect(self.reset_all)
        self.add_placeholder_button.setDisabled(True)
        self.reset_placeholder_button.setDisabled(True)
        self.add_placeholder_button.clicked.connect(self.add_placeholders)
        self.reset_placeholder_button.clicked.connect(self.reset_placeholder)
        
        finish = QtWidgets.QAction("Quit",self)
        finish.triggered.connect(self.close_window)

    def close_window(self, event):
        if show_question_message('Are you sure you wanna exit?') == YES :
            sys.exit()         
        else:
            pass
        
    def add_placeholders(self):
        if self.placeholder_key.currentText() == 'Select Key' or \
            self.placeholder_value.currentText() == 'Select Value':
                show_warning_message('Select proper key value for placeholder!')
        else:
            if self.placeholder_view.item(0).text() == 'None': 
                self.placeholder_view.clear() 
                self.placeholder_view.addItem(
                    self.placeholder_key.currentText() + " : " + self.placeholder_value.currentText()
                )
                self.dynamic_placeholder.append(
                        (self.placeholder_key.currentText(),self.placeholder_value.currentText())
                    )
            else:
                if (self.check_if_placeholder_exists(self.placeholder_key.currentText())):
                    show_warning_message("PLaceholder already present!")
                    
                else:
                    self.placeholder_view.addItem(
                        self.placeholder_key.currentText() + " : " + self.placeholder_value.currentText()
                    )
                    self.dynamic_placeholder.append(
                        (self.placeholder_key.currentText(),self.placeholder_value.currentText())
                    )
            self.placeholder_value.setCurrentIndex(0)
            self.placeholder_key.setCurrentIndex(0)
            
    def check_if_placeholder_exists(self,placeholder_key):
        for i in self.dynamic_placeholder:
            if i[0] == placeholder_key:
                return True
        return False        
    
    def reset_placeholder(self):
        self.placeholder_view.clear()
        self.placeholder_view.addItem('None')
    
    def set_add_reset_enable(self):
        if self.placeholder_key.count() > 1 and self.placeholder_value.count() > 1:
            self.add_placeholder_button.setDisabled(False)
            self.reset_placeholder_button.setDisabled(False)
        
    def reset_all(self):
        
        self.attachment_label.setText('')
        self.subject_text.setText('')
        self.lineEdit.setText('')
        self.test_email_label.setText('')
        self.recipients_label.setText('')
        self.placeholder_view.clear()
        self.placeholder_view.addItem('None') 
        self.placeholder_value.clear()
        self.placeholder_value.addItem('Select Value')
        self.placeholder_key.clear()
        self.placeholder_key.addItem('Select Key')
        self.recipient_file = ''
        self.attachment_file = ''
        self.template_file = ''
        self.subject = ''
    
    def show_settings(self):
        settings_window = SettingScreen(1)
        settings_window.exec_()

    def view_html_file(self):
        self.web = QWebView()
        self.web.load(QUrl.fromLocalFile(self.template_file))
        self.web.setWindowTitle(os.path.basename(self.template_file))
        self.web.show()
        
    def show_sample_csv(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        name = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File',
                                                     'Sample.csv',
                                                     'CSV (*.csv)', options=options)[0]
        if name:
            file = open(name,'w')
            writer = csv.writer(file)
            writer.writerow(["Name","Email","Phone No"])
            file.close()   
        else:
            pass       
         
    def show_summary(self):
        
        self.summary = viewSummary.GenerateSummary()
        
        if self.recipient_file:
            
            total_recipient = self.summary.return_total_recipients(self.recipients_df)
            recipient_file = self.recipient_file
            placeholders = self.summary.return_placeholder_text(self.dynamic_placeholder)
            placeholder_pairs = self.dynamic_placeholder
            template_file = self.template_file
            subject = self.subject_text.text()
            attachment_file = self.attachment_file
            
            self.summary_window = SummaryScreen(template_file=template_file, \
                            placeholder=placeholders,\
                            total_recipient=total_recipient,\
                            subject=subject,\
                            attachment_file=attachment_file,\
                            recipient_file=recipient_file,\
                            placeholder_pairs=placeholder_pairs)
            self.summary_window.show()
        else:
            show_warning_message("Select Recipients/Template before proceeding!")
        
            
    def show_recipients(self):
        if isinstance(self.recipients_df,str):
            show_warning_message("No file is selected!")
        else:
            self.recipient_window = RecipientWindow(self.recipients_df)
            self.recipient_window.exec_()
          
    def get_placeholder_values(self, template_file):
        with open(template_file) as file_:
            content = file_.read()
            placeholders = jinja2schema.infer(content).keys()
        return list(placeholders)
    
    def set_combo_box_items(self,items):
        for i in items:
            self.placeholder_key.addItem(i)
        
    def get_template_file(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.template_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, \
            "Select File to upload", "","HTML Files (*.html)", options=options)
        if (self.template_file.endswith('.html')):      
            file_name = os.path.basename(self.template_file)  
            combo_box_items = self.get_placeholder_values(self.template_file) 
            if len(combo_box_items) == 0:     
                show_information_message('Template added succesfully! No Placeholders Found!')
            else:
                self.set_combo_box_items(combo_box_items)
                self.set_add_reset_enable()
                show_information_message('Template added succesfully! Some Placeholders Found!')
            self.lineEdit.setText(file_name)
        else:
            show_information_message('No File is selected!')
        

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
                    show_warning_message('Size of file exceeded! Select another file')
                else:
                    self.attachment_label.setText(file_name)
            except:
                show_information_message('No attachment is selected!')
        else:
            show_information_message('No attachment is selected!')
                

    def reset_attachment_file(self):
        self.attachment_label.setText('')
        self.attachment_file = ''
        
    def set_placeholder_values(self,placeholder_values):
        for i in placeholder_values:
            self.placeholder_value.addItem(i)
    
    def extract_recipients(self):
    
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.recipient_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, \
            "Select File to upload", "","CSV Files (*.csv)", options=options)
                
        if (self.recipient_file.endswith('.csv')):      
            file_name = os.path.basename(self.recipient_file)
            try:
                self.recipients_df = pd.read_csv(self.recipient_file)
                self.set_placeholder_values(self.recipients_df.columns.tolist())
                self.set_add_reset_enable()           
            except:
                show_warning_message('Error reading recipients file!')
            
            show_information_message("Recipients added succesfully!")
            self.recipients_label.setText(file_name)
        else:
            show_information_message('No File is selected!')
    
    def send_test_mail(self):             
                        
        if self.template_file:
            if self.test_email_label.text():
                try:
                    summary = viewSummary.GenerateSummary()
                    data = {'recipient_file' : self.test_email_label.text(),\
                            'template_file' : self.template_file,\
                            'subject' : self.subject_text.text(),\
                            'placeholder_values' : self.dynamic_placeholder,\
                            'attach_file' : self.attachment_file}
                    data = json.dumps(data)
                    print('starting')
                    progWindow = ProgressWindow()
                    progWindow.setLabelText('Sending Mails....')
                    progWindow.show()
                    progWindow.callProgram('python',["Screens\Send_test.py", data])
                except:
                    show_information_message('Test Message Not sent!!')
                    self.test_email_label.clear()
            else:
                show_warning_message('Please enter test mail!!')
        else:
           show_warning_message('Please enter complete details before proceeding!!') 

class RecipientWindow(recipientScreen.Ui_Dialog,QtWidgets.QDialog):
    """ This class is for showing all the details of the recipients """
    
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
    """ This class is for showing the summary of the selctions for bulk mail campaigns """
    
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
        self.placeholder = self.items['placeholder_pairs']
        self.total_recipient = self.items['total_recipient']
        self.recipient_file = self.items['recipient_file']
        item = QtWidgets.QTableWidgetItem(str(os.path.basename(self.template_file))) 
        self.summary_table.setItem(0,1,item)
        item = QtWidgets.QTableWidgetItem(str(self.placeholder))
        self.summary_table.setItem(1,1,item)
        item = QtWidgets.QTableWidgetItem(str(self.total_recipient))
        self.summary_table.setItem(2,1,item)
        item = QtWidgets.QTableWidgetItem(str(self.subject))
        self.summary_table.setItem(3,1,item)
        item = QtWidgets.QTableWidgetItem(str(os.path.basename(self.attachment_file)))
        self.summary_table.setItem(4,1,item)
    
    def send_mail_bulk(self):
        
        if self.verify_box.isChecked():
            if(self.total_recipient and self.template_file):
                
                data = {'recipient_file' : self.recipient_file,\
                        'template_file' : self.template_file,\
                        'subject' : self.subject,\
                        'placeholder_values' : self.placeholder,\
                        'attach_file' : self.attachment_file,\
                        'recipients_count' : self.total_recipient}
                data = json.dumps(data)
                print('starting')
                progWindow = ProgressWindow()
                progWindow.setLabelText('Sending Mails....')
                self.close()
                progWindow.show()
                progWindow.callProgram('python',['Screens\Send_bulk.py', data])
                
            else:
                show_warning_message('Please enter complete details before proceeding!!')
                self.verify_box.setChecked(False) 
        else:
            show_warning_message('Tick the verify box before sending!!')
            
class SettingScreen(QtWidgets.QDialog, settingScreen.Ui_Dialog):
    
    """This class is for changing the configuration or settings of the mail account"""
    def __init__(self, startmode, details):
        super(SettingScreen, self).__init__()
        self.setupUi(self)
        self.mail_provider = ''
        self.details = details
        self.start_mode = startmode
        
        self.apply_button.clicked.connect(self.set_env_variables)
        self.ok_button.clicked.connect(self.confirm_variables)
        if startmode == 0:
            self.cancel_button.setEnabled(False)
            self.groupBox.setChecked(True)
            self.groupBox_3.setChecked(False)
        else:
            self.saved_details = self.get_credentials()
            self.set_saved_values(self.saved_details)
            self.cancel_button.setEnabled(True)
            self.apply_button.setEnabled(False)
            
        self.cancel_button.clicked.connect(self.cancel_operation)
        self.sendgrid_check.clicked.connect(self.sendgrid_provider)
        self.mailgun_check.clicked.connect(self.mailgun_provider)
        self.username_box.textChanged.connect(self.enable_applybutton)
        self.password_box.textChanged.connect(self.enable_applybutton)
        self.domain_box.textChanged.connect(self.enable_applybutton)
        self.apikey_box.textChanged.connect(self.enable_applybutton)
    
    def sendgrid_provider(self):
        self.mail_provider = 'sendgrid'
        self.groupBox_3.setChecked(True)
        self.domain_box.setDisabled(True)
        show_information_message("""
                                 <html>
                                 <body>
                                    Get your API KEY for sendgrid from \
                                        <a href="https://sendgrid.com/partner/github-education">\
                                        here</a>
                                 </body>
                                 </html>
                """)
        self.apply_button.setEnabled(True)
        
    def mailgun_provider(self):
        self.mail_provider = 'mailgun'
        self.groupBox_3.setChecked(True)
        show_information_message("""
                                 <html>
                                 <body>
                                    Get your API KEY for mailgun from \
                                        <a href="https://www.mailgun.com/github-students/">here</a>
                                 </body>
                                 </html>
                """)
        self.apply_button.setEnabled(True)
        
    def enable_applybutton(self):
        self.apply_button.setEnabled(True)
        
    def get_credentials(self, params):
        payload = []
        for i in params:
            payload.append(i)
            
        store_creds = StoreCredentials()
        conn = store_creds.get_connection()
        verify = store_creds.check_valid_connection(conn)
        
        if verify:
            result = store_creds.get_credentials(conn, payload)
            if result!='Error':
                self.set_saved_values(result)
            else:
                pass
        else:
            show_warning_message("Some Error occured!") 
        
        del store_creds 
    
    def update_credentials(self,params,saved_params):
        
        filter_params = ('username', saved_params[1])
        payload = []
        for i in params.items:
            payload.append((i[0], i[1]))
            
        store_creds = StoreCredentials()
        conn = store_creds.get_connection()
        verify = store_creds.check_valid_connection(conn)
        if verify:
            result = store_creds.update_credentials(conn, filter_param, payload)
            if result == 'Success':
                show_information_message('Settings Saved!')
            else:
                show_warning_message('Settings saving Failed! Try Again!')
        else:
            show_warning_message("No data found!")

        del store_creds
        
    def create_credentials(self, params):
        payload = []
        for i in params.items():
            payload.append((i[0], i[1]))
        
        store_creds = StoreCredentials()
        conn = store_creds.get_connection()
        verify = store_creds.check_valid_connection(conn)
        if verify:
            res_table = store_creds.create_table(conn)
            result = store_creds.insert_credentials(conn, payload)
            if result == 'Success':
                show_information_message('Settings Applied!')
            else:
                show_warning_message('Settings saving Failed! Try Again!')
            
        else:
            show_warning_message("Credentials not saved try again!")
        
        del store_creds
        
    def cancel_operation(self):
        self.close()
        
    def set_saved_values(self, response):
        
        self.username_box.setText(response[1])
        self.password_box.setText(response[2])
        self.mail_provider = response[3]
        if self.mail_provider == 'sendgrid':
            self.sendgrid_check.setChecked(True)
            self.domain_box.setDisabled(True)
        else:
            self.mailgun_check.setChecked(True)
            self.domain_box.setText(response[5])
        self.apikey_box.setText(response[4])
            
    def confirm_variables(self):
        
        if self.start_mode == 0:
            login_window = Loginwindow()
            self.close()
            login_window.show()
        else:
            self.close()
    
    def set_env_variables(self):
        
        if self.start_mode == 0:
            
            if self.username_box.text():    
                self.details['username'] = self.username_box.text()
            else:
                show_warning_message('No username set. Cannot proceed !')
            
            if self.password_box.text():
                self.details['password'] = self.password_box.text()
            else:
                show_warning_message('No password set. Cannot proceed !')
            
            if self.mail_provider:
                self.details['mailprovider'] = self.mail_provider

                if self.apikey_box.text():
                    self.details['providerkey'] = self.apikey_box.text()
            else:
                pass
            
            if self.mail_provider == 'mailgun':
                if self.domain_box.text():
                    self.details['domainname'] = self.domain_box.text()
            else:
                pass
            
            response = self.create_credentials(self.details)       
        
        else:
                        
            if self.username_box.text():    
                self.details['username'] = self.username_box.text()
            else:
                show_warning_message('No username set. Cannot proceed !')
            
            if self.password_box.text():
                self.details['password'] = self.password_box.text()
            else:
                show_warning_message('No password set. Cannot proceed !')
            
            if self.mail_provider:
                self.details['mailprovider'] = self.mail_provider

                if self.apikey_box.text():
                    self.details['providerkey'] = self.apikey_box.text()
            else:
                pass
            
            if self.mail_provider == 'mailgun':
                if self.domain_box.text():
                    self.details['domainname'] = self.domain_box.text()
            else:
                pass
            
            response = self.update_credentials(self.details, self.saved_details)       
        

       
        
            
class ProgressWindow(QtWidgets.QMainWindow, progressScreen.Ui_MainWindow):
    
    """This class is for showing the progress of all the events happening in the interface"""
    
    def __init__(self):
        super(ProgressWindow, self).__init__()
        self.logs = []
        self.setupUi(self)
        # aboutToQuit.connect(self.stop_function)
        self.setWindowIcon(
            QtGui.QIcon(r'Data/googledev.png'))
        self.process = QtCore.QProcess(self)
        # QProcess emits `readyRead` when there is data to be read
        self.process.readyRead.connect(self.dataReady)
        self.process.started.connect(
            lambda: self.continue_button.setEnabled(False))
        self.process.finished.connect(
            lambda: self.continue_button.setEnabled(True))
        self.process.finished.connect(
            lambda: self.stop_button.setEnabled(False))
        self.process.finished.connect(self.onFinished)
        self.continue_button.clicked.connect(self.continue_function)
        self.stop_button.clicked.connect(self.stop_function)
    
        
    def continue_function(self):
        response = show_question_message('Do you want to save the logs?')
        if response == YES:
            now = datetime.datetime.now()
            date_time = now.strftime("logs-%m-%d-%Y") + '.txt'
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            name = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File',
                                                        date_time,
                                                        'Text (*.txt)', options=options)[0]
            if name:
                with open(name,'w') as log_file:
                    for i in self.logs:
                        log_file.write(i)
                        log_file.write('\n')    
            else:
                pass 
            
        self.close()
  
    def stop_function(self):
        response = show_question_message('Are you sure you wan to cancel the operation?')
        if response == YES:
            self.process.kill
            self.continue_function()
        else:
            pass
            
    def setLabelText(self, text):
        self.labelProgress.setText(text)

    def dataReady(self):   
        str_data = str(self.process.readAllStandardOutput(), 'utf-8') 
        cursor = self.logs_view.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(str_data)
        self.logs.append(str_data)
        # self.logs_view.ensureCursorVisible()
        
    def onStart(self,ver,processList):
        self.progressBar.setRange(0,0)
        self.process.start(ver,processList)
        
    def onFinished(self):
        self.progressBar.setRange(0,1)
        self.progressBar.setValue(1)
        self.setLabelText('Process Completed!!')

    def callProgram(self, ver, processList):
       self.onStart(ver,processList)


if __name__ == '__main__':
    
    global app
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Loginwindow()
    if not(window.check_for_settings()):
        begin_window = SetupWindow()
        begin_window.show()
    else:
        window.show()
        
    sys.exit(app.exec_())
