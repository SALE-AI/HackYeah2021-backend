from helper import requestBIK

def getDemographic(street, buildingNumber, postalCode):
    url = "bik-api-4/dane-demograficzne-adres"
    response = requestBIK(street, buildingNumber, postalCode, url)
    return response.json()["demographicData"]

def getUczelnie(street, buildingNumber, postalCode):
    url = "bik-api-4/liczba-poi-adres"
    response = requestBIK(street, buildingNumber, postalCode, url).json()
    return response.json()[""]

print(getDemographic("Astronautów", "7", "93533"))