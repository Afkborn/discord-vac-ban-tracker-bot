
from steamwebapi.api import ISteamUser

from python.globalVariables import CSGO_APP_ID, STEAM_API_KEY

#Model
from .Model.PlayerBan import PlayerBan
from .Model.Player import Player
#time
from time import time


import requests

class SteamAPI_Service:
    def __init__(self) -> None:
        self.steamuserinfo = ISteamUser(steam_api_key=STEAM_API_KEY)
        
    def checkSteamID(self,steamid:str) -> bool:
        if ("https" in steamid):
            if (steamid[-1] != "/"):
                steamid +=  "/"
            if ('profiles' in steamid):
                steamid = steamid.split("/")[-2]
                return steamid
            elif ('id' in steamid):
                steamid = steamid.split("/")[-2]
                result = self.getSteamIDFromVanityURL(steamid)
                if result == 0:
                    return False
                else:
                    return result
                
        if steamid.isdigit():
            return steamid
        if (steamid.startswith("STEAM_")):
            return self.steamid_to_64bit(steamid)
        
        result = self.getSteamIDFromVanityURL(steamid)
        if result != 0:
            return result
        return False

        
    
    def getPlayer(self, steamid: str) -> Player:
        if (type(steamid) == int):
            steamid = str(steamid)
        steamid = self.checkSteamID(steamid)
        if (steamid == False):
            print(" Error: SteamID is not valid")
            return None
        
        playerinfo = self.steamuserinfo.get_player_summaries(steamIDS=steamid)['response']['players']
        if len(playerinfo) == 0:
            return None
        elif len(playerinfo) == 1:
            playerinfo = playerinfo[0]
            steamID = playerinfo['steamid']
            communityvisibilitystate = playerinfo['communityvisibilitystate']
            if communityvisibilitystate == 2 or communityvisibilitystate == 1:
                timecreated = 0
                primaryclanid = 0
                personastateflags = 0
            elif communityvisibilitystate == 3:
                timecreated = playerinfo['timecreated']
                primaryclanid = playerinfo['primaryclanid']
                personastateflags = playerinfo['personastateflags']
                #private profile
                
            
            profilestate = playerinfo['profilestate']
            personaname = playerinfo['personaname']
            if 'commentpermission' in playerinfo:
                commentpermission = playerinfo['commentpermission']
            else:
                commentpermission = 0
                
            profileurl = playerinfo['profileurl']
            avatar = playerinfo['avatar']
            avatarmedium = playerinfo['avatarmedium']
            avatarfull = playerinfo['avatarfull']
            avatarhash = playerinfo['avatarhash']
            personastate = playerinfo['personastate']
            
            if 'loccountrycode' in playerinfo:
                loccountrycode = playerinfo['loccountrycode']
            else:
                loccountrycode = None
                
            if 'locstatecode' in playerinfo:
                locstatecode = playerinfo['locstatecode']
            else:
                locstatecode = None
            if 'loccityid' in playerinfo:
                loccityid = playerinfo['loccityid']
            else:
                loccityid = None
            if 'realname' in playerinfo:
                realname = playerinfo['realname']
            else:
                realname = None
            if 'gameid' in playerinfo:
                gameid = playerinfo['gameid']
                print(f"gameid: {gameid}")
            else:
                gameid = None
            if 'gameserverip' in playerinfo:
                gameserverip = playerinfo['gameserverip']
                print(f"gameserverip: {gameserverip}")
            else:
                gameserverip = None
            if 'gameextrainfo' in playerinfo:
                gameextrainfo = playerinfo['gameextrainfo']
            else:
                gameextrainfo  = None
            if 'lastlogoff' in playerinfo:
                lastlogoff = playerinfo['lastlogoff']
            else:
                lastlogoff = 0
            myPlayer = Player(steamID=steamID,
                              communityVisibilityState=communityvisibilitystate,
                              profileState=profilestate,
                              personaName=personaname,
                              commentpermission=commentpermission,
                              profileURL=profileurl,
                              avatar=avatar,
                              avatarMedium=avatarmedium,
                              avatarFull=avatarfull,
                              avatarHash=avatarhash,
                              personaState=personastate,
                              primaryClanID=primaryclanid,
                              timeCreated=timecreated,
                              personaStateFlags=personastateflags,
                              createdTime=time(),
                              loccountrycode=loccountrycode,
                              locstatecode=locstatecode,
                              loccityid=loccityid,
                              realname=realname,
                              gameid=gameid,
                              gameserverip=gameserverip,
                              gameextrainfo=gameextrainfo,
                              lastlogoff=lastlogoff
                              )
            return myPlayer
        else:
            print(f" Error: Multiple users returned")
            return None
    
    def getPlayerBan(self, steamid: str) -> PlayerBan:
        steamid = self.checkSteamID(steamid)
        if (steamid == False):
            print(" Error: SteamID is not valid")
            return None
        userban = self.steamuserinfo.get_player_bans(steamIDS=steamid)['players']
        if len(userban) == 0:
            return None
        elif len(userban) == 1:
            #[{'SteamId': '76561198090921449', 'CommunityBanned': False, 'VACBanned': True, 'NumberOfVACBans': 1, 'DaysSinceLastBan': 1112, 'NumberOfGameBans': 0, 'EconomyBan': 'none'}]
            steamID, communityBanned, VACBanned, NumberOfVACBans, DaysSinceLastBan, NumberOfGameBans, EconomyBan = userban[0].values()
            myPlayerBan = PlayerBan(steamID=steamID, communityBanned=communityBanned, VACBanned=VACBanned, NumberOfVACBans=NumberOfVACBans, DaysSinceLastBan=DaysSinceLastBan, NumberOfGameBans=NumberOfGameBans, EconomyBan=EconomyBan,CreatedTime=time())
            return myPlayerBan
        else:
            print(" Error: Multiple users returned")
            return None
        
    def getSteamLevel(self,steamid: str) -> int:
        steamid = self.checkSteamID(steamid)
        if (steamid == False):
            print(" Error: SteamID is not valid")
            return None
        try:
            response = requests.get(f"https://api.steampowered.com/IPlayerService/GetSteamLevel/v1/?key={STEAM_API_KEY}&steamid={steamid}")
            return response.json()['response']['player_level']
        except:
            print(" Error: Steam Level")
            return 0
        
    def getTotalTimePlayedCSGO(self, steamid:str) -> int:
        steamid = self.checkSteamID(steamid)
        if (steamid == False):
            print(" Error: SteamID is not valid")
            return None
        try:
            response = requests.get(f"https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v2/?appid={CSGO_APP_ID}&key={STEAM_API_KEY}&steamid={steamid}")
            return response.json()['playerstats']['stats'][2]['value']
        except:
            print(" Error: TotalTimePlayedCSGO")
            return None
        
    def getSteamIDFromVanityURL(self, vanityURL:str):
        try:
            response = requests.get(f"https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={STEAM_API_KEY}&vanityurl={vanityURL}")
            return response.json()['response']['steamid']
        except:
            print(" Error: SteamIDFromVanitryURL")
            return 0
        
    def steamid_to_64bit(self,steamid):
        steam64id = 76561197960265728 # I honestly don't know where
                                        # this came from, but it works...
        id_split = steamid.split(":")
        steam64id += int(id_split[2]) * 2 # again, not sure why multiplying by 2...
        if id_split[1] == "1":
            steam64id += 1
        return steam64id
    
    def getGameWithID(self,gameID: int):
        try: 
            response = requests.get(f"https://store.steampowered.com/api/appdetails?appids={gameID}")
            data = response.json()[str(gameID)]["data"]
            return data
        except:
            print(f" Error: Game with ID {gameID} not found")
    
    def isDLC(self,gameID: int):
        response = requests.get(f"https://store.steampowered.com/api/appdetails?appids={gameID}")
        data = response.json()[str(gameID)]["data"]['type']
        if data == "game":
            return False
        elif data == "dlc":
            return True
        else:
            print(data)
            return False

