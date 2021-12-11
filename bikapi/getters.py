from helper import requestBIK

def getDemographic(street, buildingNumber):
    url = "bik-api-4/dane-demograficzne-adres"
    response = requestBIK(street, buildingNumber, url)
    return response.text

def getUczelnie(street, buildingNumber):
    url = "bik-api-4/liczba-poi-adres"
    response = requestBIK(street, buildingNumber, url)
    return response.json.text

print(getDemographic("Astronautów", "7", "93533"))