from python.globalVariables import *
import json

from python.SteamAPI_Service import SteamAPI_Service
myTracker = SteamAPI_Service()

def getIDwithGameName(gameName:str, showDLC = False):
    gameName = gameName.lower()
    file = open(STEAM_GAMES_LOC,encoding="utf8")
    jsonData = json.load(file)
    appList = jsonData["applist"]["apps"]
    returnList = []
    for apps in appList:
        appName = apps["name"]
        appID = apps["appid"]
        appNameLower = appName.lower()
        if gameName in appNameLower:
            returnList.append((appID,appName))
    return returnList

def getGameNameWithID(appID:int):
    file = open(STEAM_GAMES_LOC,encoding="utf8")
    jsonData = json.load(file)
    appList = jsonData["applist"]["apps"]
    return None