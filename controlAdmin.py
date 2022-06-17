from python.BotDatabase import Database
from python.SteamAPI_Service import SteamAPI_Service
myDb = Database()
mySteamAPI = SteamAPI_Service()

def updateAllSteamPlayers():
    allSteamIDs = myDb.getAllSteamIDs()
    for steamID in allSteamIDs:
        player = mySteamAPI.getPlayer(steamID)
        myDb.addPlayer(player)
    
    
updateAllSteamPlayers()