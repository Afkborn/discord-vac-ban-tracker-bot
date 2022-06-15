from time import sleep, time

from python.Model.PlayerBan import PlayerBan
from python.globalVariables import DISCORD_API_KEY
from .BotDatabase import Database
from .SteamAPI_Service import SteamAPI_Service
from .Model.Track import Track
import json
import requests

class Tracker:
    TRACK_SLEEP_TIME = 60
    TRACK_CHECK_TIME = 60
    def __init__(self) -> None:
        self.db = Database()
        self.steamAPI = SteamAPI_Service()
    
    def getAllTrackObject(self):
        return self.db.getAllTrack()
    
    def getTrackableObject(self) -> list[Track]:
        trackableObject = []
        for track in self.getAllTrackObject():
            if (track.getTime() + self.getTrackCheckTime()) < time():
                trackableObject.append(track)
        return trackableObject
    
    def setTracker(self):
        while True:
            for track in self.getTrackableObject():
                #check ban status, if banned message to owner
                last_steam_ban_status = self.db.getLastPlayerBan(track.getSteamID())
                new_ban_status = self.steamAPI.getPlayerBan(str(track.getSteamID()))
                if (self.compareVacBan(last_steam_ban_status, new_ban_status)):
                    print("VAC Ban Changed")
                    self.sendMessageViaHTPP(f"{track.getSteamID()} VAC Ban Changed", track.getChannelID())
                if (self.compareEconomyBan(last_steam_ban_status, new_ban_status)):
                    print("Economy Ban Changed")
                if (self.compareNumberOfGameBan(last_steam_ban_status, new_ban_status)):
                    print("Number of Game Bans Changed")
                if (self.compareCommunityBan(last_steam_ban_status, new_ban_status)):
                    print("Community Ban Changed")
            sleep(self.TRACK_SLEEP_TIME)
    
    
    def setTrackSleepTime(self,sleepTime):
        self.TRACK_SLEEP_TIME = sleepTime
    def setTrackCheckTime(self,checkTime):
        self.TRACK_CHECK_TIME = checkTime
    def getTrackSleepTime(self):
        return self.TRACK_SLEEP_TIME
    def getTrackCheckTime(self):
        return self.TRACK_CHECK_TIME


    
    def compareVacBan(self,playerBan1 : PlayerBan, playerBan2 : PlayerBan):
        if (playerBan1.getVACBanned() != playerBan2.getVACBanned()):
            return True
    def compareEconomyBan(self,playerBan1 : PlayerBan, playerBan2 : PlayerBan):
        if (playerBan1.getEconomyBan() != playerBan2.getEconomyBan()):
            return True
    def compareNumberOfGameBan(self,playerBan1 : PlayerBan, playerBan2 : PlayerBan):
        if (playerBan1.getNumberOfGameBans() != playerBan2.getNumberOfGameBans()):
            return True
    def compareCommunityBan(self,playerBan1 : PlayerBan, playerBan2 : PlayerBan):
        if (playerBan1.getcommunityBanned() != playerBan2.getcommunityBanned()):
            return True
        
    def sendMessageViaHTPP(self,message, channel_id):
        baseURL = f"https://discordapp.com/api/channels/{channel_id}/messages"
        headers = { "Authorization":"Bot {}".format(DISCORD_API_KEY),
                    "User-Agent":"myBotThing (http://some.url, v0.1)",
                    "Content-Type":"application/json", }
        POSTedJSON =  json.dumps ( {"content":message} )
        r = requests.post(baseURL, headers = headers, data = POSTedJSON)