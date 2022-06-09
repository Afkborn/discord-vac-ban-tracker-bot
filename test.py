from python.PlayerTracker import PlayerTracker
from python.keys import STEAM_API_KEY


testUsers = ["https://steamcommunity.com/profiles/76561198352086380/","76561199089429877","Afkborn","https://steamcommunity.com/id/Afkborn/"]


myPlayerTracker = PlayerTracker(STEAM_API_KEY=STEAM_API_KEY)
for user in testUsers:

    user = myPlayerTracker.getPlayer(user)
    # userBan = myPlayerTracker.getPlayerBan(user)
    print(user.getPersonaName())
    

