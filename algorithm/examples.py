import json

def getUczelnie():
    data = """{
    "inputDataAddress": {
        "code": "92221",
        "city": "Łódź",
        "street": "NOWOGRODZKA",
        "building_number": "17"
    },
    "size": "500",
    "nearestPOI": {
        "D_EDUKACJA_WYZSZE_SZKOLY_PUBLICZNE": 810
    }
    }"""
    res = json.loads(data)["nearestPOI"]["D_EDUKACJA_WYZSZE_SZKOLY_PUBLICZNE"]
    if res < 500:
        return 3, res
    elif res < 1000:
        return 2, res
    elif res < 1500:
        return 1, res
    else:
        return 0, res

def getSzkolyPodstawowe():
    data = """{
    "inputDataAddress": {
        "code": "92221",
        "city": "Łódź",
        "street": "NOWOGRODZKA",
        "building_number": "17"
    },
    "size": "500",
    "nearestPOI": {
        "D_EDUKACJA_SZKOLY_PODSTAWOWE": 700
    }
    }"""
    res = json.loads(data)["nearestPOI"]["D_EDUKACJA_SZKOLY_PODSTAWOWE"]
    if res < 500:
        return 3, res
    elif res < 1000:
        return 2, res
    elif res < 1500:
        return 1, res
    else:
        return 0, res

def getPrzedszkola():
    data = """{
    "inputDataAddress": {
        "code": "92221",
        "city": "Łódź",
        "street": "NOWOGRODZKA",
        "building_number": "17"
    },
    "size": "500",
    "nearestPOI": {
        "D_EDUKACJA_PRZEDSZKOLA_I_PUNKTY_PRZEDSZKOLNE": 480
    }
    }"""
    res = json.loads(data)["nearestPOI"]["D_EDUKACJA_PRZEDSZKOLA_I_PUNKTY_PRZEDSZKOLNE"]
    if res < 500:
        return 3, res
    elif res < 1000:
        return 2, res
    elif res < 1500:
        return 1, res
    else:
        return 0, res

def getKawiarnie():
    data = """{
    "inputDataAddress": {
        "code": "92221",
        "city": "Łódź",
        "street": "NOWOGRODZKA",
        "building_number": "17"
    },
    "size": "500",
    "nearestPOI": {
        "D_HORECA_KAWIARNIA": 1160
    }
    }"""
    res = json.loads(data)["nearestPOI"]["D_HORECA_KAWIARNIA"]
    if res < 500:
        return 3, res
    elif res < 1000:
        return 2, res
    elif res < 1500:
        return 1, res
    else:
        return 0, res

def getRestauracje():
    data =  """{
    "inputDataAddress": {
        "code": "92221",
        "city": "Łódź",
        "street": "NOWOGRODZKA",
        "building_number": "17"
    },
    "size": "100",
    "nearestPOI": {
        "D_HORECA_RESTAURACJA": 890
    }
    }"""
    res = json.loads(data)["nearestPOI"]["D_HORECA_RESTAURACJA"]
    if res < 500:
        return 3, res
    elif res < 1000:
        return 2, res
    elif res < 1500:
        return 1, res
    else:
        return 0, res
    

def getPoczta():
    data =  """{
    "inputDataAddress": {
        "code": "92221",
        "city": "Łódź",
        "street": "NOWOGRODZKA",
        "building_number": "17"
    },
    "size": "100",
    "nearestPOI": {
        "D_POCZTA": 1720
    }
    }"""
    res = json.loads(data)["nearestPOI"]["D_POCZTA"]
    if res < 500:
        return 3, res
    elif res < 1000:
        return 2, res
    elif res < 1500:
        return 1, res
    else:
        return 0, res

def getPaczkomat():
    data =  """{
    "inputDataAddress": {
        "code": "92221",
        "city": "Łódź",
        "street": "NOWOGRODZKA",
        "building_number": "17"
    },
    "size": "100",
    "nearestPOI": {
        "D_PRZESYLKI_PACZKOMAT": 430
    }
    }
    """
    res = json.loads(data)["nearestPOI"]["D_PRZESYLKI_PACZKOMAT"]
    if res < 500:
        return 3, res
    elif res < 1000:
        return 2, res
    elif res < 1500:
        return 1, res
    else:
        return 0, res


def getPrzystanki():
    data =  """{
    "inputDataAddress": {
        "code": "92221",
        "city": "Łódź",
        "street": "NOWOGRODZKA",
        "building_number": "17"
    },
    "size": "500",
    "nearestPOI": {
        "D_TRANSPORT_PRZYSTANEK_TRAMWAJOWY": 390
    }
    }"""
    res = json.loads(data)["nearestPOI"]["D_TRANSPORT_PRZYSTANEK_TRAMWAJOWY"]
    if res < 500:
        return 3, res
    elif res < 1000:
        return 2, res
    elif res < 1500:
        return 1, res
    else:
        return 0, res

def getHipermarket():
    data = """{
    "inputDataAddress": {
        "code": "92221",
        "city": "Łódź",
        "street": "NOWOGRODZKA",
        "building_number": "17"
    },
    "size": "500",
    "nearestPOI": {
        "D_SKLEP_SIECIOWY_HIPERMARKET": 1440
    }
    }"""
    res = json.loads(data)["nearestPOI"]["D_SKLEP_SIECIOWY_HIPERMARKET"]
    if res < 500:
        return 3, res
    elif res < 1000:
        return 2, res
    elif res < 1500:
        return 1, res
    else:
        return 0, res


def getConvienience():
    data = """{
    "inputDataAddress": {
        "code": "92221",
        "city": "Łódź",
        "street": "NOWOGRODZKA",
        "building_number": "17"
    },
    "size": "500",
    "nearestPOI": {
        "D_SKLEP_SIECIOWY_CONVENIENCE": 440
    }
    }"""
    res = json.loads(data)["nearestPOI"]["D_SKLEP_SIECIOWY_CONVENIENCE"]
    if res < 500:
        return 3, res
    elif res < 1000:
        return 2, res
    elif res < 1500:
        return 1, res
    else:
        return 0, res

def getMonopolowy():
    data = """{
    "inputDataAddress": {
        "code": "92221",
        "city": "Łódź",
        "street": "NOWOGRODZKA",
        "building_number": "17"
    },
    "size": "500",
    "nearestPOI": {
        "D_SKLEP_SIECIOWY_SKLEP_MONOPOLOWY": 4100
    }
    }"""
    res = json.loads(data)["nearestPOI"]["D_SKLEP_SIECIOWY_SKLEP_MONOPOLOWY"]
    if res < 500:
        return 3, res
    elif res < 1000:
        return 2, res
    elif res < 1500:
        return 1, res
    else:
        return 0, res

def getCrimes():
    data = """[
    {
        "grid": 100,
        "status": "ok",
        "details": [
            {
                "category": "crime",
                "status": "ok",
                "details": {
                    "assault_battery": 1,
                    "burglary": 0,
                    "theft": 1,
                    "other": 0
                }
            },
            {
                "category": "road_accident",
                "status": "ok",
                "details": {
                    "vehicle_collision": 0,
                    "hitting_a_pedestrian": 0,
                    "other_accident_type": 0
                }
            }
        ]
    },
    {
        "grid": 250,
        "status": "ok",
        "details": [
            {
                "category": "crime",
                "status": "ok",
                "details": {
                    "assault_battery": 1,
                    "burglary": 0,
                    "theft": 1,
                    "other": 0
                }
            },
            {
                "category": "road_accident",
                "status": "ok",
                "details": {
                    "vehicle_collision": 0,
                    "hitting_a_pedestrian": 0,
                    "other_accident_type": 1
                }
            }
        ]
    },
    {
        "grid": 500,
        "status": "ok",
        "details": [
            {
                "category": "crime",
                "status": "ok",
                "details": {
                    "assault_battery": 1,
                    "burglary": 0,
                    "theft": 1,
                    "other": 0
                }
            },
            {
                "category": "road_accident",
                "status": "ok",
                "details": {
                    "vehicle_collision": 5,
                    "hitting_a_pedestrian": 0,
                    "other_accident_type": 3
                }
            }
        ]
    }
    ]"""
    res = json.loads(data)
    crimeIndex = 0
    w = 3
    for e in res:
        crimeIndex += w*sum(e["details"][0]["details"].values())
        w -= 1
    if crimeIndex < 15:
        return 3, crimeIndex
    elif crimeIndex < 30:
        return 2, crimeIndex
    elif crimeIndex < 70:
        return 1, crimeIndex
    else:
        return 0, crimeIndex
