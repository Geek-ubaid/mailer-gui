
import os
import sys
import json
import argparse

import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

EXTENSION_TO_TYPE = {'pdf':'document/pdf', 'jpg':'image/jpg', 'png':'image/png', \
    'jpeg':'image/jpeg', 'docx':'document/docx'}

def send_bulk_mail(to_mail,from_mail,subject,message,attach=False):
    """ Sending bulk email function"""
    
    if attach:
        attach_file_name = os.path.basename(attach) 
        attach_type = EXTENSION_TO_TYPE[str(attach_file_name.split('.')[-1]).lower()]
        attach_content = open(attach,'rb').read()
        
        for i in range(len(to_mail)):
            response = requests.post(
                "https://api.eu.mailgun.net/v3/{0}/messages".format(os.getenv('DOMAIN_MAIL')),
                auth=("api", os.getenv('API_KEY')),
                files=[("attachment", ("attach" + attach_file_name.split('.')[-1] , attach_content, attach_type))],
                data={"from": from_mail,
                    "to": to_mail[i],
                    "subject": subject,
                    "html": message},
                )
            print_format(response)
    else:
           
        for i in range(len(to_mail)):
            response = requests.post(
                "https://api.eu.mailgun.net/v3/{0}/messages".format(os.getenv('DOMAIN_MAIL')),
                auth=("api", os.getenv('API_KEY')),
                data={"from": from_mail,
                    "to": to_mail[i],
                    "subject": subject,
                    "html": message},
                )
            print_format(response)
        
def main(data):
    
    """fetching all the sending data"""
    
    recipient_file = data['recipient_file']
    template_file = data['template_file']
    subject = data['subject']
    placeholder_values = data['placeholder_values']
    attach = data['attach_file']
    with open(template_file) as file:
        message = file.read()
        
    df = pd.read_csv(recipient_file)
    recipients = list(df['email'].values)
    
    send_bulk_mail(recipients, os.getenv('FROM_MAIL'), subject, message)
        
def print_format(string, **kwargs): 
    if 'flush' in kwargs:
        print(string, **kwargs)
    else:
        print(string, flush = True, **kwargs)
        

if __name__ == "__main__":
    
    data = json.loads(sys.argv[1])
    main(data)