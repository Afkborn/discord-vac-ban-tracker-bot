from python.globalVariables import *
import json

def getCountryNameWithCode(countryCode : str):
    with open(STEAM_COUNTRIES_LOC) as f:
        data = json.load(f)
        return data[countryCode]['name']


def getCountryDetail(countryCode: str = None, locstatecode : str = None, loccityid : int = None):
    
    loccityid = str(loccityid)
    f = open(STEAM_COUNTRIES_LOC)
    data = json.load(f)
    if countryCode == None:
        return None, None, None
    countryName = data[countryCode]['name']
    if locstatecode == None:
        return countryName, None, None
    countryState = data[countryCode]['states'][locstatecode]
    countryStateName = countryState['name']
    if loccityid == 'None':
        return countryName, countryStateName, None
    countryStateCities = countryState['cities']
    countryStateCitiesName = countryStateCities[loccityid]['name']
    return (countryName, countryStateName, countryStateCitiesName)
    