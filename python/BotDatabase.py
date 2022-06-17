from multiprocessing.sharedctypes import Value
import sqlite3 as sql
from sys import int_info


#Model
from .Model.PlayerBan import PlayerBan
from .Model.Player import Player
from .Model.DiscordUser import DiscordUser
from .Model.Game import Game
from .Model.Track import Track

        # self.__lastlogoff = lastlogoff int 
        # self.__realName = realname str
        # self.__locCountryCode = loccountrycode str
        # self.__locStateCode = locstatecode str
        # self.__locCityID =  loccityid int

CREATETABLE_PLAYER = """CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    steamid TEXT,
    communityvisibilitystate INTEGER,
    profilestate INTEGER,
    personaname TEXT,
    profileurl TEXT,
    avatar TEXT,
    avatarmedium TEXT,
    avatarfull TEXT,
    avatarHash TEXT,
    commentpermission INTEGER,
    personastate INTEGER,
    primaryclanid TEXT,
    timecreated INTEGER,
    personastateflags INTEGER,
    createdTime REAL,
    lastlogoff INTEGER,
    realname TEXT,
    loccountrycode TEXT,
    locstatecode TEXT,
    loccityid INTEGER
    );"""
    
    
CREATETABLE_PLAYERBAN = """CREATE TABLE IF NOT EXISTS playerbans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    steamid TEXT,
    communitybanned BOOL,
    VACbanned BOOL,
    numberofVACBans INTEGER,
    daysSinceLastBan INTEGER,
    numberofGameBans INTEGER,
    economyban TEXT,
    createdtime REAL
    );"""

CREATETABLE_DISCORDUSER = """CREATE TABLE IF NOT EXISTS discordusers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discordID INTEGER,
    name TEXT,
    avatar_url TEXT,
    joined_at REAL,
    created_at REAL
    );"""

CREATETABLE_GAME = """CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    steam_appid INTEGER,
    name TEXT
    );"""

CREATETABLE_TRACK = """CREATE TABLE IF NOT EXISTS tracks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ownerDiscordID INTEGER,
    steamID INTEGER,
    time REAL,
    channelID INTEGER
    );"""

class Database():
    dbName = "database.db"
    dbLoc = fr"db/{dbName}"
    
    def __init__(self) -> None:
        self.createDB()
    
    def openDB(self):
        self.db = sql.connect(self.dbLoc)
        self.im = self.db.cursor()
    

    
    def createDB(self):
        self.openDB()
        
        self.im.execute(CREATETABLE_PLAYER)
        self.im.execute(CREATETABLE_PLAYERBAN)
        self.im.execute(CREATETABLE_DISCORDUSER)
        self.im.execute(CREATETABLE_GAME)
        self.im.execute(CREATETABLE_TRACK)
        self.db.commit()
        
        self.db.close()
    
    def addPlayer(self, player:Player):
        
        if (self.getPlayerWithSteamID(player.getSteamID()) != None):
            print(" This player already exists, not adding, updating instead")
            self.updatePlayer(player)
            return False
        
        self.openDB()
        
        KEY = f"steamid,communityvisibilitystate,profilestate,personaname,profileurl,avatar,avatarmedium,avatarfull,avatarhash,commentpermission,personastate,primaryclanid,timecreated,personastateflags,createdTime,lastlogoff,realname,loccountrycode,locstatecode,loccityid"
        VALUES = f"""
        '{player.getSteamID()}',
        '{player.getCommunityVisibilityState()}',
        '{player.getProfileState()}',
        '{player.getPersonaName()}',
        '{player.getProfileURL()}',
        '{player.getAvatar()}',
        '{player.getAvatarMedium()}',
        '{player.getAvatarFull()}',
        '{player.getAvatarHash()}',
        '{player.getCommentPermission()}',
        '{player.getPersonaState()}',
        '{player.getPrimaryClanID()}',
        '{player.getTimeCreated()}',
        '{player.getPersonaStateFlags()}',
        '{player.getCreatedTime()}',
        '{player.getLastlogoff()}',
        '{player.getRealName()}',
        '{player.getLocCountryCode()}',
        '{player.getLocStateCode()}',
        '{player.getLocCityID()}'
        """
        self.im.execute(f"INSERT INTO players ({KEY}) VALUES ({VALUES})")
        self.db.commit()
        self.db.close()
    
    def getPlayerWithSteamID(self, steamID:str) -> Player:
        self.openDB()
        
        self.im.execute(f"SELECT * FROM players WHERE steamid='{steamID}'")
        result = self.im.fetchone()
        if result == None:
            return None
        id, steamid, communityvisibilitystate, profilestate, personaname, profileurl, avatar, avatarmedium, avatarfull, avatarhash, commentpermission, personastate, primaryclanid, timecreated, personastateflags, createdTime, lastlogoff, realname, loccountrycode, locstatecode, loccityid = result
        myPlayer = Player(ID=id,
                          steamID=steamid,
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
                          createdTime=createdTime,
                          lastlogoff=lastlogoff,
                          realname=realname,
                          loccountrycode=loccountrycode,
                          locstatecode=locstatecode,
                          loccityid=loccityid)
                          
        return myPlayer
    
    def addPlayerBan(self,playerBan : PlayerBan):
        
        self.openDB()
        
        KEY = f"steamid,communitybanned,VACbanned,numberofVACBans,daysSinceLastBan,numberofGameBans,economyban,createdtime"
        VALUES = f"""
        '{playerBan.getsteamID()}',
        '{playerBan.getcommunityBanned()}',
        '{playerBan.getVACBanned()}',
        '{playerBan.getNumberOfVACBans()}',
        '{playerBan.getDaysSinceLastBan()}',
        '{playerBan.getNumberOfGameBans()}',
        '{playerBan.getEconomyBan()}',
        '{playerBan.getCreatedTime()}'
        """
        self.im.execute(f"INSERT INTO playerbans ({KEY}) VALUES ({VALUES})")
        self.db.commit()
        self.db.close()
        
    def getLastPlayerBan(self, steamID:str) -> PlayerBan:
        self.openDB()
        self.im.execute(f"SELECT * FROM playerbans WHERE steamid='{steamID}' ORDER BY createdtime DESC LIMIT 1")
        result = self.im.fetchone()
        if result == None:
            return None
        id, steamid, communitybanned, VACbanned, numberofVACBans, daysSinceLastBan, numberofGameBans, economyban, createdtime = result
        myPlayerBan = PlayerBan(ID=id,
                                steamID=steamid,
                                communityBanned=communitybanned,
                                VACBanned=VACbanned,
                                NumberOfVACBans=numberofVACBans,
                                DaysSinceLastBan=daysSinceLastBan,
                                NumberOfGameBans=numberofGameBans,
                                EconomyBan=economyban,
                                CreatedTime=createdtime)
        return myPlayerBan

    def addDiscordUser(self, discordUser:DiscordUser) :
        if (self.getDiscordUserWithDiscordID(discordUser.getDiscordID()) != None):    
            return False
        
        self.openDB()
        
        KEY = f"discordID,name,avatar_url,joined_at,created_at"
        VALUES = f"""
        '{discordUser.getDiscordID()}',
        '{discordUser.getName()}',
        '{discordUser.getAvatarURL()}',
        '{discordUser.getJoinedAt()}',
        '{discordUser.getCreatedAt()}'
        """
        
        self.im.execute(f"INSERT INTO discordusers ({KEY}) VALUES ({VALUES})")
        self.db.commit()
        self.db.close()
        
    def getDiscordUserWithDiscordID(self, discordID:int):
        self.openDB()
        self.im.execute(f"SELECT * FROM discordusers WHERE discordID='{discordID}'")
        result = self.im.fetchone()
        self.db.close()
        if result == None:
            return None
        id, discordID, name, avatar_url, joined_at, created_at = result
        myDiscordUser = DiscordUser(id, discordID, name, avatar_url, joined_at, created_at)
        return myDiscordUser

    def addSteamGame(self, game :Game):
        if (self.getGameWithID(game.getAppID()) != None):
            print(f" Game {game.getAppID()} already exists")
            return False
        self.openDB()
        KEY = f"steam_appid, name"
        VALUES = f"""
        '{game.getAppID()}',
        '{game.getClearName()}'
        """
        self.im.execute(f"INSERT INTO games ({KEY}) VALUES ({VALUES})")
        self.db.commit()
        
        self.db.close()
        
    def getGameWithID(self, appID:int) -> Game:
        self.openDB()
        self.im.execute(f"SELECT * FROM games WHERE steam_appid='{appID}'")
        result = self.im.fetchone()
        if result == None:
            return None
        id, steam_appid, name = result
        myGame = Game(id, steam_appid, name)
        return myGame
    
    def getGameWithName(self, name:str) -> list[Game]:
        gameList = []
        self.openDB()
        # if contains results, add to list
        self.im.execute(f"SELECT * FROM games WHERE name LIKE '%{name}%'")
        all_result = self.im.fetchall()
        for result in all_result:
            id, steam_appid, name = result
            myGame = Game(id, steam_appid, name)
            gameList.append(myGame)
        return gameList

    def addTrack(self, track:Track):
        if (self.getTrackWithTrack(track) != None):
            return False        
        self.openDB()
        KEY = f"ownerDiscordID, steamID, time,channelID"
        VALUES = f"""
        '{track.getOwnerDiscordID()}',
        '{track.getSteamID()}',
        '{track.getTime()}',
        '{track.getChannelID()}'
        """
        self.im.execute(f"INSERT INTO tracks ({KEY}) VALUES ({VALUES})")
        self.db.commit()
        self.db.close()
    
    def getTrackWithTrack(self, track:Track) -> Track:
        self.openDB()
        self.im.execute(f"SELECT * FROM tracks WHERE ownerDiscordID={track.getOwnerDiscordID()} AND steamID={track.getSteamID()}")
        result = self.im.fetchone()
        self.db.close()
        if result == None:
            return None
        id, ownerDiscordID, steamID, time, channelID = result
        myTracker = Track(id, ownerDiscordID, steamID, time, channel_id=channelID)
        return myTracker
    
    def deleteTrack(self,steamID:int, ownerDiscordID:int):
        self.openDB()
        self.im.execute(f"DELETE FROM tracks WHERE steamID={steamID} AND ownerDiscordID={ownerDiscordID}")
        self.db.commit()
        self.db.close()
    
    def getTrackWithSteamID_DiscordID(self, steamID:int, ownerDiscordID : int) -> Track:
        self.openDB()
        self.im.execute(f"SELECT * FROM tracks WHERE ownerDiscordID={ownerDiscordID} AND steamID={steamID}")
        result = self.im.fetchone()
        self.db.close()
        if result == None:
            return None
        id, ownerDiscordID, steamID, time, channelID = result
        myTracker = Track(id, ownerDiscordID, steamID, time, channel_id=channelID)
        return myTracker
    
    def getAllTrack(self) -> list[Track]:
        self.openDB()
        trackList = []
        self.im.execute(f"SELECT * FROM tracks")
        results = self.im.fetchall()
        self.db.close()
        if results == None:
            return None
        for result in results:
            id ,ownerDiscordID, steamID, time, channelID = result
            myTracker = Track(id, ownerDiscordID, steamID, time, channel_id=channelID)
            trackList.append(myTracker)
        return trackList
    
    def getAllTrackWithDiscordID(self, discordID:int) -> list[Track]:
        self.openDB()
        trackList = []
        self.im.execute(f"SELECT * FROM tracks WHERE ownerDiscordID={discordID}")
        results = self.im.fetchall()
        self.db.close()
        if results == None:
            return None
        for result in results:
            id ,ownerDiscordID, steamID, time, channelID = result
            myTracker = Track(id, ownerDiscordID, steamID, time, channel_id=channelID)
            trackList.append(myTracker)
        return trackList
    
    def updatePlayer(self, player:Player):
        self.openDB()
        self.im.execute(f"""UPDATE players SET 
                        communityvisibilitystate={player.getCommunityVisibilityState()},
                        profilestate={player.getProfileState()},
                        personaname='{player.getPersonaName()}',
                        profileurl='{player.getProfileURL()}',
                        avatar='{player.getAvatar()}',
                        avatarmedium='{player.getAvatarMedium()}',
                        avatarfull='{player.getAvatarFull()}',
                        avatarHash='{player.getAvatarHash()}',
                        commentpermission={player.getCommentPermission()},
                        personastate={player.getPersonaState()},
                        primaryclanid='{player.getPrimaryClanID()}',
                        timecreated={player.getTimeCreated()},
                        personastateflags={player.getPersonaStateFlags()},
                        createdTime={player.getCreatedTime()},
                        lastlogoff={player.getLastlogoff()},
                        realname='{player.getRealName()}',
                        loccountrycode='{player.getLocCountryCode()}',
                        locstatecode='{player.getLocStateCode()}',
                        loccityid={player.getLocCityID()}
                        WHERE steamid='{player.getSteamID()}'""")
        self.db.commit()
        self.db.close()
        
    def getAllSteamPlayers(self) -> list[Player]:
        self.openDB()
        playerList = []
        self.im.execute(f"SELECT * FROM players")
        results = self.im.fetchall()
        self.db.close()
        if results == None:
            return None
        for result in results:
            id, steamid, communityvisibilitystate, profilestate, personaname, profileurl, avatar, avatarmedium, avatarfull, avatarhash, commentpermission, personastate, primaryclanid, timecreated, personastateflags, createdTime, lastlogoff, realname, loccountrycode, locstatecode, loccityid = result
            myPlayer = Player(ID=id,
                          steamID=steamid,
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
                          createdTime=createdTime,
                          lastlogoff=lastlogoff,
                          realname=realname,
                          loccountrycode=loccountrycode,
                          locstatecode=locstatecode,
                          loccityid=loccityid)
            playerList.append(myPlayer)
        return playerList
    
    def getAllSteamIDs(self) -> list[str]:
        self.openDB()
        steamIDList = []
        self.im.execute(f"SELECT steamid FROM players")
        results = self.im.fetchall()
        self.db.close()
        if results == None:
            return None
        for result in results:
            steamIDList.append(int(result[0]))
        return steamIDList
        