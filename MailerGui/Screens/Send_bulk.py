
import os
import sys
import json
import argparse

import requests
import pandas as pd
import base64
import sendgrid
from sendgrid.helpers.mail import *
from dotenv import load_dotenv

load_dotenv()

EXTENSION_TO_TYPE = {'pdf':'document/pdf', 'jpg':'image/jpg', 'png':'image/png', \
    'jpeg':'image/jpeg', 'docx':'document/docx'}

def sendgrid_with_attachment(from_email,to_mail,subject,message,attachment):
    
    try:
        to_email = Email(to_mail)
        from_email = Email(from_email)
        content = Content("text/html",message)
        mail = Mail(from_email, subject, to_email, content)
        mail.add_attachment(attachment)
        response = sg.client.mail.send.post(request_body=mail.get())
        print_format("mail sent to " + to_mail)
        print_format(attach)
        print_format(response.status_code)
    except:
        print_format("mail not sent to " +  to_mail)
        pass
    
def sendgrid_without_attachment(from_email,to_mail,subject,message):
    
    try:
        to_email = Email(to_mail)
        from_email = Email(from_email)
        content = Content("text/html",message)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print_format("mail sent to" + to_mail)
        print_format(response.status_code)
    except:
        print_format("mail not sent to " +  to_mail)
        pass

def mailgun_with_attachment(from_mail,to_mail,subject,message,attachment):
    
    response = requests.post(
                        "https://api.eu.mailgun.net/v3/{0}/messages".format(os.getenv('DOMAIN_MAIL')),
                        auth=("api", os.getenv('API_KEY')),
                        files=[("attachment", ("attach" + attachment[0] , attachment[1], attachment[3]))],
                        data={"from": from_mail,
                            "to": to_mail,
                            "subject": subject,
                            "html": message},
                        )
    
    print_format(response)
    
def mailgun_without_attachment(from_mail,to_mail,subject,message):
    
    response = requests.post(
                        "https://api.eu.mailgun.net/v3/{0}/messages".format(os.getenv('DOMAIN_MAIL')),
                        auth=("api", os.getenv('API_KEY')),
                        data={"from": from_mail,
                            "to": to_mail,
                            "subject": subject,
                            "html": message},
                        )
    print_format(response)

def send_mailgun_bulk_mail(to_mail,from_mail,subject,message,placeholder,attach=False):
    
    """ Sending bulk email function using mailgun api"""
    
    if attach:
        
        ## for mails with attachment
        
        attach_file_name = os.path.basename(attach).split('.')[-1]
        attach_type = EXTENSION_TO_TYPE[str(attach_file_name.split('.')[-1]).lower()]
        attach_content = open(attach,'rb').read()
        
        if placeholder:
            
            ## for placeholder values
            
            if len(placeholder['const_placeholders']) > 0 and len(placeholder['excel_placeholder']) == 0:
                
                ## for mails with constant placeholders and no dynamic placeholders
                
                for i in placeholder['çonst_placeholders']:
                    message = set_placeholder_values(message,i[0], i[1])
                for index in range(len(to_mail)):
                    to_mail_address = to_mail.iloc[index]['Email']
                    mailgun_with_attachment(from_mail, to_mail_address, subject, message,\
                         (attach_file_name, attach_content, attach_type))
                    
                    
            elif len(placeholder['excel_placeholder']) > 0 and len(placeholder['const_placeholders']) == 0:
               
                ## for mails with dynmaic placeholders and no constant placeholders
               
                for index in range(len(to_mail)):
                    for place in placeholder['excel_placeholder']:
                        message = set_placeholder_values(message, place[0], to_mail.iloc[index][place[1]])
                    print_format(message)
                    to_mail_address = to_mail.iloc[index]['Email']
                    mailgun_with_attachment(from_mail, to_mail_address, subject, message,\
                         (attach_file_name, attach_content, attach_type))
                    
                    
            elif len(placeholder['excel_placeholder']) > 0 and len(placeholder['const_placeholders']) > 0:
                
                ## for both constant and dynamic placeholders
                
                for index in placeholder['const_placeholder']:
                    message = set_placeholder_values(message, index[0], index[1])
                    
                for index in range(len(to_mail)):
                    for place in placeholder['excel_placeholder']:
                        message = set_placeholder_values(message, place[0], to_mail.iloc[index][place[1]])
                    print_format(message)
                    to_mail_address = to_mail.iloc[index]['Email']
                    mailgun_with_attachment(from_mail, to_mail_address, subject, message,\
                         (attach_file_name, attach_content, attach_type))
                    
        else:
            
            ## for no placeholder values
            
            for index in range(len(to_mail)):
                to_mail_address = to_mail.iloc[index]
                mailgun_with_attachment(from_mail, to_mail_address, subject, message,\
                         (attach_file_name, attach_content, attach_type))
                    
                
    else:
      
        ## for mails without attachment
        
        if placeholder:
           
            ## for placeholder values
           
            if len(placeholder['const_placeholders']) > 0 and len(placeholder['excel_placeholder']) == 0:
           
                ## for mails with constant placeholders and no dynamic placeholders
           
                for i in placeholder['çonst_placeholders']:
                    message = set_placeholder_values(message,i[0], i[1])
                for index in range(len(to_mail)):
                    to_mail_address = to_mail.iloc[index]['Email']
                    mailgun_without_attachment(from_mail, to_mail_address, subject, message)
                    
                    
            elif len(placeholder['excel_placeholder']) > 0 and len(placeholder['const_placeholders']) == 0:
               
                ## for mails with dynmaic placeholders and no constant placeholders
               
                for index in range(len(to_mail)):
                    for place in placeholder['excel_placeholder']:
                        message = set_placeholder_values(message, place[0], to_mail.iloc[index][place[1]])
                    print_format(message)
                    to_mail_address = to_mail.iloc[index]['Email']
                    mailgun_without_attachment(from_mail, to_mail_address, subject, message)                    
            
            elif len(placeholder['excel_placeholder']) > 0 and len(placeholder['const_placeholders']) > 0:
                
                ## for both constant and dynamic placeholders
                
                for index in placeholder['const_placeholder']:
                    message = set_placeholder_values(message, index[0], index[1])
                    
                for index in range(len(to_mail)):
                    for place in placeholder['excel_placeholder']:
                        message = set_placeholder_values(message, place[0], to_mail.iloc[index][place[1]])
                    print_format(message)
                    to_mail_address = to_mail.iloc[index]['Email']
                    mailgun_without_attachment(from_mail, to_mail_address, subject, message)
                    
        else:
            
            ## for no placeholder values
            
            for index in range(len(to_mail)):
                to_mail_address = to_mail[index]
                mailgun_without_attachment(from_mail, to_mail_address, subject, message)
        
            
def send_sendgrid_bulk_mail(to,sender,subject,message,placeholder,attach=False):
    
    """ Sending bulk email function using sendgrid api"""

    sg = sendgrid.SendGridAPIClient(apikey=os.getenv('API_KEY'))
    
    if(bool(attach)):
        
        ## for mail with attachment
        
        data = open(attach,'rb').read()
        attach_file_name = os.path.basename(attach) 
        encoded = base64.b64encode(data).decode()
        attachment = Attachment()
        attachment.content = encoded
        attachment.type = EXTENSION_TO_TYPE[str(attach_file_name.split('.')[-1]).lower()]  ## application/pdf for pdf attach and image/(.jpg,.jpeg,.png)
        attachment.filename = attach_file_name ## file name 
        attachment.disposition = 'attachment' # either inline or attachment
        attachment.content_id = '' ## any valid id
        
         
        if placeholder:
            
            ## for placeholder values
            
            if len(placeholder['const_placeholders']) > 0 and len(placeholder['excel_placeholder']) == 0:
                
                ## for mails with constant placeholders and no dynamic placeholders
                
                for i in placeholder['çonst_placeholders']:
                    message = set_placeholder_values(message,i[0], i[1])
                    
                for index in range(len(to)):
                    print_format(message)
                    to_email = to.iloc[index]['Email']
                    sendgrid_with_attachment(sender,to_email,subject,message,attachment)
                    
            elif len(placeholder['excel_placeholder']) > 0 and len(placeholder['const_placeholders']) == 0:
               
                ## for mails with dynmaic placeholders and no constant placeholders
               
                 for index in range(len(to)):
                    for place in placeholder['excel_placeholder']:
                        message = set_placeholder_values(message, place[0], to.iloc[index][place[1]])
                    print_format(message)
                    to_email = to.iloc[index]['Email']
                    sendgrid_with_attachment(sender,to_email,subject,message,attachment)
                    
            elif len(placeholder['excel_placeholder']) > 0 and len(placeholder['const_placeholders']) > 0:
                
                ## for both constant and dynamic placeholders
                
                for index in placeholder['const_placeholder']:
                    message = set_placeholder_values(message, index[0], index[1])
                    
                for index in range(len(to)):
                    for place in placeholder['excel_placeholder']:
                        message = set_placeholder_values(message, place[0], to.iloc[index][place[1]])
                    print_format(message)
                    to_email = to.iloc[index]['Email']
                    sendgrid_with_attachment(sender,to_email,subject,message,attachment)
        else:
            
            ## for no placeholder values
            for index in range(len(to)):
                to_email = to[index]
                sendgrid_with_attachment(sender,to_email,subject,message,attachment)

    else:
        
        ## for mail without attachment
        
        if placeholder:
            
            ## for placeholder values
            
            if len(placeholder['const_placeholders']) > 0 and len(placeholder['excel_placeholder']) == 0:
                
                ## for mails with constant placeholders and no dynamic placeholders
                
                for i in placeholder['çonst_placeholders']:
                    message = set_placeholder_values(message,i[0], i[1])
                    
                for index in range(len(to)):
                    print_format(message)
                    to_email = to.iloc[index]['Email']
                    sendgrid_without_attachment(sender,to_email,subject,message)
                    
            elif len(placeholder['excel_placeholder']) > 0 and len(placeholder['const_placeholders']) == 0:
               
                ## for mails with dynmaic placeholders and no constant placeholders
               
                 for index in range(len(to)):
                    for place in placeholder['excel_placeholder']:
                        message = set_placeholder_values(message, place[0], to.iloc[index][place[1]])
                    print_format(message)
                    to_email = to.iloc[index]['Email']
                    sendgrid_without_attachment(sender,to_email,subject,message)
                    
            elif len(placeholder['excel_placeholder']) > 0 and len(placeholder['const_placeholders']) > 0:
                
                ## for both constant and dynamic placeholders
                
                for index in placeholder['const_placeholder']:
                    message = set_placeholder_values(message, index[0], index[1])
                    
                for index in range(len(to)):
                    for place in placeholder['excel_placeholder']:
                        message = set_placeholder_values(message, place[0], to.iloc[index][place[1]])
                    print_format(message)
                    to_email = to.iloc[index]['Email']
                    sendgrid_without_attachment(sender,to_email,subject,message)
        else:
            
            ## for no placeholder values
            for index in range(len(to)):
                to_email = to[index]
                sendgrid_without_attachment(sender,to_email,subject,message)
        
            
def set_placeholder_values(message, actual_value, replace_value):
    """ For setting placeholder values in the message content """
    
    return message.replace(actual_value,replace_value)

def main(data):
    """fetching all the sending data"""
    
    recipient_file = data['recipient_file']
    template_file = data['template_file']
    subject = data['subject']
    
    if subject == '':
        subject = 'Undefined Subject'
    
    placeholder_values = data['placeholder_values']
    attach = data['attach_file']
    
    with open(template_file) as file:
        message = file.read()
        
    if 'key1' in list(placeholder_values.keys()):
        placeholder = False
        df = pd.read_csv(recipient_file)
        recipients = list(df['Email'].values)
    else:
        recipients = pd.read_csv(recipient_file)
        const_placeholders = []
        excel_placeholders = []
        for i in list(placeholder.items()):
            if i[1] in recipients.columns.tolist():
                excel_placeholders.append(i)
            else:
                const_placeholders.append(i)
        placeholder = {'const_placeholders' : const_placeholders,\
                        'excel_placeholders' : excel_placeholders}
    
    if os.getenv('SERVICE_PROVIDER') == 'Mailgun':
        if attach: 
            send_mailgun_bulk_mail(recipients, os.getenv('FROM_MAIL'), subject, message, placeholder, attach)
        else:
            send_mailgun_bulk_mail(recipients, os.getenv('FROM_MAIL'), subject, message, placeholder)
            
    elif os.getenv('SERVICE_PROVIDER') == 'Sendgrid':
        if attach: 
            send_sendgrid_bulk_mail(recipients, os.getenv('FROM_MAIL'), subject, message, placeholder, attach)
        else:
            send_sendgrid_bulk_mail(recipients, os.getenv('FROM_MAIL'), subject, message, placeholder)
    
    else:
        print_format("Service Provider not set!!")

def print_format(string, **kwargs): 
    """ This function is for flushing to the stdout"""
    
    if 'flush' in kwargs:
        print(string, **kwargs)
    else:
        print(string, flush = True, **kwargs)
        

if __name__ == "__main__":
    
    data = json.loads(sys.argv[1])
    main(data)