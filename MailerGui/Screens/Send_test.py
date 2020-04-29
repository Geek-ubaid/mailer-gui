
import os
import sys
import json
import argparse

import requests
import pandas as pd
import base64
import sendgrid
from jinja2 import Environment, BaseLoader 
from sendgrid.helpers.mail import *
from dotenv import load_dotenv

load_dotenv()

EXTENSION_TO_TYPE = {'pdf':'document/pdf', 'jpg':'image/jpg', 'png':'image/png', \
    'jpeg':'image/jpeg', 'docx':'document/docx'}


def send_mailgun_bulk_mail(to_mail,from_mail,subject,message,attach=False):
    
    """ Sending test email function using mailgun api"""
    
    if attach:
        attach_file_name = os.path.basename(attach) 
        attach_type = EXTENSION_TO_TYPE[str(attach_file_name.split('.')[-1]).lower()]
        attach_content = open(attach,'rb').read()
        
        response = requests.post(
            "https://api.eu.mailgun.net/v3/{0}/messages".format(os.getenv('DOMAIN_MAIL')),
            auth=("api", os.getenv('API_KEY')),
            files=[("attachment", ("attach" + attach_file_name.split('.')[-1] , attach_content, attach_type))],
            data={"from": from_mail,
                "to": to_mail,
                "subject": subject,
                "html": message},
            )
        print_format(response)
        
    else:
        
        response = requests.post(
            "https://api.eu.mailgun.net/v3/{0}/messages".format(os.getenv('DOMAIN_MAIL')),
            auth=("api", os.getenv('API_KEY')),
            data={"from": from_mail,
                "to": to_mail,
                "subject": subject,
                "html": message},
            )
        print_format(response)
        
def send_sendgrid_bulk_mail(to,sender,subject,message,attach=False):
    
    """ Sending test email function using sendgrid api"""

    sg = sendgrid.SendGridAPIClient(apikey=os.getenv('API_KEY'))
    
    if(bool(attach)):
        
        data = open(attach,'rb').read()
        attach_file_name = os.path.basename(attach) 
        encoded = base64.b64encode(data).decode()
        attachment = Attachment()
        attachment.content = encoded
        attachment.type = EXTENSION_TO_TYPE[str(attach_file_name.split('.')[-1]).lower()]  ## application/pdf for pdf attach and image/(.jpg,.jpeg,.png)
        attachment.filename = attach_file_name ## file name 
        attachment.disposition = 'attachment' # either inline or attachment
        attachment.content_id = '' ## any valid id
        
        try:
            to_email = Email(to)
            from_email = Email(sender)
            content = Content("text/html",message)
            mail = Mail(from_email, subject, to_email, content)
            mail.add_attachment(attachment)
            response = sg.client.mail.send.post(request_body=mail.get())
            print_format("mail sent to " + to)
            print_format(attach_file_name)
            print_format(response.status_code)
        except:
            print_format("mail not sent to " + to)
            pass

    else:
        try:
            to_email = Email(to)
            from_email = Email('dscvitvellore@gmail.com')
            content = Content("text/html", message)
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print_format("mail sent to " + to)
            print_format(response.status_code)
        except:
            print_format("mail not sent to " + to)
            pass
        
def set_placeholder_values(message, data):
    """ For setting placeholder values in the message content """
    
    return message.render(data)
         

def get_format_template(template_dir):
    
    with open(template_dir) as file_:
        content = file_.read()
        template = Environment(loader = BaseLoader).from_string(content)
    return template

def main(data):
    
    """fetching all the sending data"""
    
    recipient = data['recipient_file']
    template_file = data['template_file']
    subject = data['subject']
    
    if subject == '':
        subject = 'Undefined Subject'
        
    placeholder_values = data['placeholder_values']
    attach = data['attach_file']


            
    if 'key1' not in list(placeholder_values.keys()):
        
        message = get_format_template(template_file)
        data = {}
        for i in placeholder_values.values():
            data[i[0]] =  i[1]
        message = set_placeholder_values(message, data)
    else:
        print_format('No placeholder Text assigned!!')
        with open(template_file) as file:
            message = file.read()

    if os.getenv('SERVICE_PROVIDER') == 'Mailgun':
        if attach: 
            send_mailgun_bulk_mail(recipient, os.getenv('FROM_MAIL'), subject, message, attach)
        else:
            send_mailgun_bulk_mail(recipient, os.getenv('FROM_MAIL'), subject, message)
            
    elif os.getenv('SERVICE_PROVIDER') == 'Sendgrid':
        if attach: 
            send_sendgrid_bulk_mail(recipient, os.getenv('FROM_MAIL'), subject, message, attach)
        else:
            send_sendgrid_bulk_mail(recipient, os.getenv('FROM_MAIL'), subject, message)
    
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