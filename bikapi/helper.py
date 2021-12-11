import requests

root = "https://gateway.oapi.bik.pl/"

def requestBIK(street, buildingNumber, url):
    url = root + url
    head = {"Content-Type": "application/json","Cache-Control": "no-cache", "BIK-OAPI-Key": "876dc7308eda42958239852af8b1f2db"}
    body = {
        "size": "500",
        "address": {
            "city": "ŁÓDŹ",
            "street": f"{street}",
            "buildingNumber": f"{buildingNumber}"
        },
        "demographicData": "M16_POPT"
    }
    r = requests.post(url, headers=head, json=body, cert=("cert.pem", "server.key"), verify=False)
    return r