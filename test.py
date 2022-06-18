from h11 import Data
from python.BotDatabase import Database
from python.SteamGames import getIDwithGameName
from python.SteamAPI_Service import SteamAPI_Service
from python.globalVariables import STEAM_API_KEY
from python.SteamCountries import *

# testUsers = ["https://steamcommunity.com/profiles/76561198304303022","765611990894298770000","76561199089429877","76561198090921449","https://steamcommunity.com/profiles/76561198352086380/"] #"

# myDatabase = Database()
# myPlayerTracker = PlayerTracker(STEAM_API_KEY=STEAM_API_KEY)
# for user in testUsers:

#     player = myPlayerTracker.getPlayer(user)
#     playerBan = myPlayerTracker.getPlayerBan(user)
#     if player != None:
#         myDatabase.addPlayer(player)
#     if playerBan != None:

#         myDatabase.addPlayerBan(playerBan)
#     print(myPlayerTracker.getSteamLevel(user))
        

    

# from python.SteamCountries import *

# print(getCountryDetail('TR','81',44758))



from python.TextFunction import *
# test()

# returnList = splitTextByLength(text, 500)
# print(returnList[0])

# print("\n\n\n")
# print(returnList[1])
# print(len(returnList))




# from python.BotDatabase import Database

# # myDb = Database()
# # print(myDb.getGameWithName("Valley"))
# # print(len(myDb.getGameWithName("Valley")))

# known_code_list = []
# from python.globalVariables import *
# api_service = SteamAPI_Service()
# result = None
# known_code = "CSGO-RRkXO-R8fEb-yjKXP-q6vUp-u2dOQ"
# known_code_list.append(known_code)
# while result != "n/a":
#     result = api_service.getCSGO_AccessMatchHistory(steamid="76561199089429877",steamid_key=AUTH_CODE,known_code=known_code)
#     print(result)
#     if result != "n/a":
#         known_code_list.append(result)
#     known_code = result
# print(known_code_list)








api_service = SteamAPI_Service()
friends_list = api_service.getFriends("76561199089429877")
print(friends_list)
print(len(friends_list))