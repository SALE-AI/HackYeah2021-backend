import json

from algorithm.request import requestBIK

BACKUP = 1

lower_break_point = 500
higher_break_point = 1500
min_crimeIndex = 15
max_crimeIndex = 70

def readAttr(attr):
    f = open("const/output.json", "r")
    data = json.load(f)[attr]
    f.close()
    return data

def getBody(attr, street, number):
    f = open("const/bodys.json", "r")
    data = json.load(f)[attr]
    data["address"]["street"] = street
    data["address"]["number"] = number
    f.close()
    return data

def getUczelnie(street, number):
    s = "studia"
    if BACKUP:
        data = readAttr(s)
    else:
        data = requestBIK(getBody(s, street, number), "bik-api-4/punkty-zainteresowania-adres")
    res = data['nearestPOI']['D_EDUKACJA_WYZSZE_SZKOLY_PUBLICZNE']
    if res < lower_break_point:
        return 1, res
    elif res < higher_break_point:
        return 1 - (higher_break_point - res)/(lower_break_point + higher_break_point), res
    else:
        return 0, res

def getSzkolyPodstawowe(street, number):
    s = "szkolaPodstawowa"
    if BACKUP:
        data = readAttr(s)
    else:
        data = requestBIK(getBody(s, street, number), "bik-api-4/punkty-zainteresowania-adres")
    res = data["nearestPOI"]["D_EDUKACJA_SZKOLY_PODSTAWOWE"]
    if res < lower_break_point:
        return 1, res
    elif res < higher_break_point:
        return 1 - (higher_break_point - res)/(lower_break_point + higher_break_point), res
    else:
        return 0, res

def getPrzedszkola(street, number):
    s = "przedszkole"
    if BACKUP:
        data = readAttr(s)
    else:
        data = requestBIK(getBody(s, street, number), "bik-api-4/punkty-zainteresowania-adres")
    res = data["nearestPOI"]["D_EDUKACJA_PRZEDSZKOLA_I_PUNKTY_PRZEDSZKOLNE"]
    if res < lower_break_point:
        return 1, res
    elif res < higher_break_point:
        return 1 - (higher_break_point - res)/(lower_break_point + higher_break_point), res
    else:
        return 0, res

def getKawiarnie(street, number):
    s = "kawiarnia"
    if BACKUP:
        data = readAttr(s)
    else:
        data = requestBIK(getBody(s, street, number), "bik-api-4/punkty-zainteresowania-adres")
    res = data["nearestPOI"]["D_HORECA_KAWIARNIA"]
    if res < lower_break_point:
        return 1, res
    elif res < higher_break_point:
        return 1 - (higher_break_point - res)/(lower_break_point + higher_break_point), res
    else:
        return 0, res

def getRestauracje(street, number):
    s = "restauracja"
    if BACKUP:
        data = readAttr(s)
    else:
        data = requestBIK(getBody(s, street, number), "bik-api-4/punkty-zainteresowania-adres")
    res = data["nearestPOI"]["D_HORECA_RESTAURACJA"]
    if res < lower_break_point:
        return 1, res
    elif res < higher_break_point:
        return 1 - (higher_break_point - res)/(lower_break_point + higher_break_point), res
    else:
        return 0, res
    

def getPoczta(street, number):
    s = "poczta"
    if BACKUP:
        data = readAttr(s)
    else:
        data = requestBIK(getBody(s, street, number), "bik-api-4/punkty-zainteresowania-adres")
    res = data["nearestPOI"]["D_POCZTA"]
    if res < lower_break_point:
        return 1, res
    elif res < higher_break_point:
        return 1 - (higher_break_point - res)/(lower_break_point + higher_break_point), res
    else:
        return 0, res

def getPaczkomat(street, number):
    s = "paczkomat"
    if BACKUP:
        data = readAttr(s)
    else:
        data = requestBIK(getBody(s, street, number), "bik-api-4/punkty-zainteresowania-adres")
    res = data["nearestPOI"]["D_PRZESYLKI_PACZKOMAT"]
    if res < lower_break_point:
        return 1, res
    elif res < higher_break_point:
        return 1 - (higher_break_point - res)/(lower_break_point + higher_break_point), res
    else:
        return 0, res


def getPrzystanki(street, number):
    s = "przystanek"
    if BACKUP:
        data = readAttr(s)
    else:
        data = requestBIK(getBody(s, street, number), "bik-api-4/punkty-zainteresowania-adres")
    res = data["nearestPOI"]["D_TRANSPORT_PRZYSTANEK_TRAMWAJOWY"]
    if res < lower_break_point:
        return 1, res
    elif res < higher_break_point:
        return 1 - (higher_break_point - res)/(lower_break_point + higher_break_point), res
    else:
        return 0, res

def getHipermarket(street, number):
    s = "hipermarket"
    if BACKUP:
        data = readAttr("hipermarket")
    else:
        data = requestBIK(getBody(s, street, number), "bik-api-4/punkty-zainteresowania-adres")
    res = data["nearestPOI"]["D_SKLEP_SIECIOWY_HIPERMARKET"]
    if res < lower_break_point:
        return 1, res
    elif res < higher_break_point:
        return 1 - (higher_break_point - res)/(lower_break_point + higher_break_point), res
    else:
        return 0, res

def getConvienience(street, number):
    s = "convenience"
    if BACKUP:
        data = readAttr(s)
    else:
        data = requestBIK(getBody(s, street, number), "bik-api-4/punkty-zainteresowania-adres")
    res = data["nearestPOI"]["D_SKLEP_SIECIOWY_CONVENIENCE"]
    if res < lower_break_point:
        return 1, res
    elif res < higher_break_point:
        return 1 - (higher_break_point - res)/(lower_break_point + higher_break_point), res
    else:
        return 0, res

def getMonopolowy(street, number):
    s = "monopolowy"
    if BACKUP:
        data = readAttr(s)
    else:
        data = requestBIK(getBody(s, street, number), "bik-api-4/punkty-zainteresowania-adres")
    res = data["nearestPOI"]["D_SKLEP_SIECIOWY_SKLEP_MONOPOLOWY"]
    if res < lower_break_point:
        return 1, res
    elif res < higher_break_point:
        return 1 - (higher_break_point - res)/(lower_break_point + higher_break_point), res
    else:
        return 0, res

def getCrimes(street, number):
    s = "crimes"
    if BACKUP:
        data = readAttr(s)
    else:
        data = requestBIK(getBody(s, street, number), "bik-api-3/bezpieczenstwo-adres")
    res = data
    crimeIndex = 0
    w = 3
    for e in res:
        crimeIndex += w*sum(e["details"][0]["details"].values())
        w -= 1
    if crimeIndex < min_crimeIndex:
        return 1, crimeIndex
    elif crimeIndex < max_crimeIndex:
        return 1 - (max_crimeIndex-crimeIndex) / (max_crimeIndex +min_crimeIndex), crimeIndex
    else:
        return 0, crimeIndex
