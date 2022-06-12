
from python.globalVariables import *
import json

from python.SteamTracker import SteamTracker
myTracker = SteamTracker(STEAM_API_KEY)



def downloadAllGameDetail():
    jsonList = {}
    file = open(STEAM_GAMES_LOC,encoding="utf8")
    jsonData = json.load(file)
    appList = jsonData["applist"]["apps"]
    appListLen = len(appList)
    for index, apps in enumerate(appList,start=1):
        appID = apps["appid"]
        data = myTracker.getGameWithID(appID)
        if(data != None):
            gameName = data["name"]
            dataJson = {appID : data}
            jsonList.update(dataJson)
            print(f"{gameName} {index}/{appListLen}")
    jsonList = json.dumps(jsonList)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonList)
    jsonFile.close()

    
    
    
    
downloadAllGameDetail()