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
        
    def getPlayer(self, steamid: str) -> Player:
        playerinfo = self.steamuserinfo.get_player_summaries(steamIDS=steamid)['response']['players']
        if len(playerinfo) == 0:
            return None
        elif len(playerinfo) == 1:
            steamID, communityvisibilitystate, profilestate, personaname, lastlogoff, profileurl, avatar, avatarmedium, avatarfull, personastate, primaryclanid, timecreated, personastateflags = playerinfo[0].values()
            myPlayer = Player(steamID=steamID, communityVisibilityState=communityvisibilitystate, profileState=profilestate, personaName=personaname, profileURL=profileurl, avatar=avatar, avatarMedium=avatarmedium, avatarFull=avatarfull, lastLogOff=lastlogoff, personaState=personastate, primaryClanID=primaryclanid, timeCreated=timecreated, personaStateFlags=personastateflags, createdTime=time())
            return myPlayer
        else:
            print(f"Error: Multiple users returned")
            return None
    
    def getPlayerBan(self, steamid: str) -> PlayerBan:
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