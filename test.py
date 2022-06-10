from python.Database import Database
from python.PlayerTracker import PlayerTracker
from python.keys import STEAM_API_KEY


testUsers = ["https://steamcommunity.com/profiles/76561198352086380/","76561199089429877","76561198090921449"]

myDatabase = Database()
myPlayerTracker = PlayerTracker(STEAM_API_KEY=STEAM_API_KEY)
for user in testUsers:

    player = myPlayerTracker.getPlayer(user)
    playerBan = myPlayerTracker.getPlayerBan(user)
    if player != None:

        myDatabase.addPlayer(player)
    if playerBan != None:

        myDatabase.addPlayerBan(playerBan)
        
        
    

