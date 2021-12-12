import requests

root = "https://gateway.oapi.bik.pl/"

def requestBIK(body, url):
    url = root + url
    head = {"Content-Type": "application/json","Cache-Control": "no-cache", "BIK-OAPI-Key": "240f1bd2fb374ed2aa28b20315528bcc"}
    r = requests.post(url, headers=head, json=body, cert=("cert.pem", "server.key"), verify=False)
    return r.json()