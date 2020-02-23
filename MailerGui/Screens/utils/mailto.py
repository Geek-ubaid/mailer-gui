
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

import os

import base64
import sendgrid
from dotenv import load_dotenv
from sendgrid.helpers.mail import *

load_dotenv()

API_KEY = os.getenv('API_KEY')

def emailAll(sender,tos,message,subject,attach=False):
    sg = sendgrid.SendGridAPIClient(apikey='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')
    from_email = Email(sender)
    content = Content("text/html",message)
    if(bool(attach)):
        with open(attach,'rb') as f:
            data = f.read()
            f.close()
        encoded = base64.b64encode(data).decode()
        attachment = Attachment()
        attachment.content = encoded
        attachment.type = ''  ## application/pdf for pdf attach and image/(.jpg,.jpeg,.png)
        attachment.filename = '' ## file name 
        attachment.disposition = 'attachment' # either inline or attachment
        attachment.content_id = 'DSC' ## any valid id
        for to in tos:
            try:
                to_email = Email(to)
                mail = Mail(from_email, subject, to_email, content)
                mail.add_attachment(attachment)
                response = sg.client.mail.send.post(request_body=mail.get())
                print("mail sent to",to)
                print(attach)
                print(response.status_code)
            except:
                print("mail not sent to ", to)
                pass

def email(sender,to,message,subject,attach=False):
    sg = sendgrid.SendGridAPIClient(apikey='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')
    from_email = Email(sender)
    to_email = Email(to)
    content = Content("text/html",message)
    if(bool(attach)):
        with open(attach,'rb') as f:
            data = f.read()
            f.close()
        encoded = base64.b64encode(data).decode()
        attachment = Attachment()
        attachment.content = encoded
        attachment.type = ''  ## application/pdf for pdf attach and image/(.jpg,.jpeg,.png)
        attachment.filename = '' ## file name 
        attachment.disposition = 'attachment' # either inline or attachment
        attachment.content_id = 'DSC' ## any valid id
        try:
            mail = Mail(from_email, subject, to_email, content)
            mail.add_attachment(attachment)
            response = sg.client.mail.send.post(request_body=mail.get())
            print("mail sent to",to)
            print(attach)
            print(response.status_code)
        except:
            print("mail not sent to ", to)
            pass

    else:
        try:
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print("mail sent to",to)
            print(response.status_code)
        except:
            print("mail not sent to ", to)
        pass
        

if __name__  == "__main__":
     
    from_mail = "dscvitvellore@gmail.com"
    to_email = "ubaid.usmani2017@vitstudent.ac.in"
    subject = "test"
    message = open(r'C:\Users\HP\Downloads\WT Mailer (1).html').read() ## html for html content or text for text content
    attach = "" ## file path
    
    email(from_mail, to_email, message, subject) ## skip attach if attach is not available
    
