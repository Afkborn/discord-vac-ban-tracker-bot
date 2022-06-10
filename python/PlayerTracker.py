from xmlrpc.client import Boolean
from matplotlib.style import use
from steamwebapi.api import ISteamUser, IPlayerService, ISteamUserStats

#Model
from .Model.PlayerBan import PlayerBan
from .Model.Player import Player
#time
from time import time

class PlayerTracker:
    def __init__(self, STEAM_API_KEY:str) -> None:
        self.steamuserinfo = ISteamUser(steam_api_key=STEAM_API_KEY)
        
    def checkSteamID(self,steamid:str) -> Boolean:

        if ("https" in steamid):
            steamid = steamid.split("/")[-2]
            if (steamid.isdigit()):
                return True
            return False

        if steamid.isdigit():
            return True
        
        return False
        
    
    def getPlayer(self, steamid: str) -> Player:
        if not (self.checkSteamID(steamid)):
            #ERROR: steamid is not a valid steamid
            print("Error: SteamID is not valid")
            return None
        playerinfo = self.steamuserinfo.get_player_summaries(steamIDS=steamid)['response']['players']
        if len(playerinfo) == 0:
            return None
        elif len(playerinfo) == 1:
            print(playerinfo)
            playerinfo = playerinfo[0]
            steamID = playerinfo['steamid']
            communityvisibilitystate = playerinfo['communityvisibilitystate']
            profilestate = playerinfo['profilestate']
            personaname = playerinfo['personaname']
            if 'commentpermission' in playerinfo:
                commentpermission = playerinfo['commentpermission']
            else:
                commentpermission = 0
                

            #TODO loccountrycode
                
            profileurl = playerinfo['profileurl']
            avatar = playerinfo['avatar']
            avatarmedium = playerinfo['avatarmedium']
            avatarfull = playerinfo['avatarfull']
            avatarhash = playerinfo['avatarhash']
            personastate = playerinfo['personastate']
            primaryclanid = playerinfo['primaryclanid']
            timecreated = playerinfo['timecreated']
            personastateflags = playerinfo['personastateflags']
            myPlayer = Player(steamID=steamID,communityVisibilityState=communityvisibilitystate,profileState=profilestate,personaName=personaname,commentpermission=commentpermission,profileURL=profileurl,avatar=avatar,avatarMedium=avatarmedium,avatarFull=avatarfull,avatarHash=avatarhash,personaState=personastate,primaryClanID=primaryclanid,timeCreated=timecreated,personaStateFlags=personastateflags,createdTime=time())
            return myPlayer
        else:
            print(f"Error: Multiple users returned")
            return None
    
    def getPlayerBan(self, steamid: str) -> PlayerBan:
        if not (self.checkSteamID(steamid)):
            #ERROR: steamid is not a valid steamid
            print("Error: SteamID is not valid")
            return None
        userban = self.steamuserinfo.get_player_bans(steamIDS=steamid)['players']
        if len(userban) == 0:
            return None
        elif len(userban) == 1:
            steamID, communityBanned, VACBanned, NumberOfVACBans, DaysSinceLastBan, NumberOfGameBans, EconomyBan = userban[0].values()
            myPlayerBan = PlayerBan(steamID=steamID, communityBanned=communityBanned, VACBanned=VACBanned, NumberOfVACBans=NumberOfVACBans, DaysSinceLastBan=DaysSinceLastBan, NumberOfGameBans=NumberOfGameBans, EconomyBan=EconomyBan,CreatedTime=time())
            return myPlayerBan
        else:
            print("Error: Multiple users returned")
            return None