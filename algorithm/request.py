import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

root = "https://gateway.oapi.bik.pl/"

def requestBIK(body, url):
    url = root + url
    
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    key = os.environ.get('BIK_OAPI_KEY')

    head = {"Content-Type": "application/json","Cache-Control": "no-cache", "BIK-OAPI-Key": key}
    r = requests.post(url, headers=head, json=body, cert=("cert.pem", "server.key"), verify=False)
    return r.json()