from time import sleep, time
from xmlrpc.client import Boolean

from python.Model.PlayerBan import PlayerBan
from python.globalVariables import DISCORD_API_KEY
from .BotDatabase import Database
from .SteamAPI_Service import SteamAPI_Service
from .Model.Track import Track
import json
import requests
from .Timer import *

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
                steamPlayer = self.db.getPlayerWithSteamID(track.getSteamID())
                discordUser = self.db.getDiscordUserWithDiscordID(track.getOwnerDiscordID())
                last_steam_ban_status = self.db.getLastPlayerBan(track.getSteamID())
                new_ban_status = self.steamAPI.getPlayerBan(str(track.getSteamID()))
                print(f" {get_time_command()} | Checking {steamPlayer.getPersonaName()} for {discordUser.getName()}")
                if (self.compareVacBan(last_steam_ban_status, new_ban_status)):
                    message = f"{discordUser.getName()} i have new message for you, {steamPlayer.getPersonaName()} is now vac banned. {type(last_steam_ban_status.getVACBanned())} {type(new_ban_status.getVACBanned())}"
                    self.sendMessageViaHTPP(message, track.getChannelID())
                    self.db.addPlayerBan(new_ban_status)
                if (self.compareEconomyBan(last_steam_ban_status, new_ban_status)):
                    message = f"{discordUser.getName()} i have new message for you, {steamPlayer.getPersonaName()} is now economy banned. {type(last_steam_ban_status.getEconomyBan())} {type(new_ban_status.getEconomyBan())}"
                    self.sendMessageViaHTPP(message, track.getChannelID())
                    self.db.addPlayerBan(new_ban_status)
                if (self.compareNumberOfGameBan(last_steam_ban_status, new_ban_status)):
                    message = f"{discordUser.getName()} i have new message for you, {steamPlayer.getPersonaName()} is now game banned. {type(last_steam_ban_status.getNumberOfGameBans())} {type(new_ban_status.getNumberOfGameBans())}"
                    self.sendMessageViaHTPP(message, track.getChannelID())
                    self.db.addPlayerBan(new_ban_status)
                if (self.compareCommunityBan(last_steam_ban_status, new_ban_status)):
                    message = f"{discordUser.getName()} i have new message for you, {steamPlayer.getPersonaName()} is now community banned. {type(last_steam_ban_status.getcommunityBanned())} {type(new_ban_status.getcommunityBanned())}"
                    self.sendMessageViaHTPP(message, track.getChannelID())
                    self.db.addPlayerBan(new_ban_status)
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
        return False
    def compareEconomyBan(self,playerBan1 : PlayerBan, playerBan2 : PlayerBan):
        if (playerBan1.getEconomyBan() != playerBan2.getEconomyBan()):
            return True
        return False
    def compareNumberOfGameBan(self,playerBan1 : PlayerBan, playerBan2 : PlayerBan):
        if (playerBan1.getNumberOfGameBans() != playerBan2.getNumberOfGameBans()):
            return True
        return False
    def compareCommunityBan(self,playerBan1 : PlayerBan, playerBan2 : PlayerBan):
        if (playerBan1.getcommunityBanned() != playerBan2.getcommunityBanned()):
            return True
        return False
        
    def sendMessageViaHTPP(self,message, channel_id) -> Boolean:
        baseURL = f"https://discordapp.com/api/channels/{channel_id}/messages"
        headers = { "Authorization":"Bot {}".format(DISCORD_API_KEY),
                    "User-Agent":"myBotThing (http://some.url, v0.1)",
                    "Content-Type":"application/json", }
        POSTedJSON =  json.dumps ( {"content":message} )
        r = requests.post(baseURL, headers = headers, data = POSTedJSON)
        if r.status_code == 200:
            return True
        else:
            return False
