
import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()

EXTENSION_TO_TYPE = {'pdf':'document/pdf', 'jpg':'image/jpg', 'png':'image/png', \
    'jpeg':'image/jpeg', 'docx':'document/docx'}

def send_test_mail(to_mail,from_mail,subject,message,attach=False):
    
    if attach:
        attach_file_name = os.path.basename(attach) 
        attach_type = EXTENSION_TO_TYPE[str(attach_file_name.split('.')[-1]).lower()]
        attach_content = open(attach,'rb').read()
    
        return requests.post(
            "https://api.eu.mailgun.net/v3/{0}/messages".format(os.getenv('DOMAIN_MAIL')),
            auth=("api", os.getenv('API_KEY')),
            files=[("attachment", ("attach" + attach_file_name.split('.')[-1] , attach_content, attach_type))],
            data={"from": from_mail,
                "to": to_mail,
                "subject": subject,
                "html": message},
            )
    else:
        return requests.post(
            "https://api.eu.mailgun.net/v3/{0}/messages".format(os.getenv('DOMAIN_MAIL')),
            auth=("api", os.getenv('API_KEY')),
            data={"from": from_mail,
                "to": to_mail,
                "subject": subject,
                "html": message},
            )