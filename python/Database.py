import sqlite3 as sql

#Model
from .Model.PlayerBan import PlayerBan
from .Model.Player import Player


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
    createdTime REAL
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
        self.db.commit()
        
        self.db.close()
    
    def addPlayer(self, player:Player):
        
        if (self.getPlayerWithSteamID(player.getSteamID()) != None):
            print("Player already in database")
            return False
        
        self.openDB()
        
        KEY = f"steamid,communityvisibilitystate,profilestate,personaname,profileurl,avatar,avatarmedium,avatarfull,avatarhash,commentpermission,personastate,primaryclanid,timecreated,personastateflags,createdTime"
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
        '{player.getCreatedTime()}'
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
        id, steamid, communityvisibilitystate, profilestate, personaname, profileurl, avatar, avatarmedium, avatarfull, avatarhash, commentpermission, personastate, primaryclanid, timecreated, personastateflags, createdTime = result
        myPlayer = Player(id,steamid,communityvisibilitystate,profilestate,personaname,profileurl,avatar,avatarmedium,avatarfull,avatarhash,commentpermission,personastate,primaryclanid,timecreated,personastateflags,createdTime)
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
        myPlayerBan = PlayerBan(id,steamid,communitybanned,VACbanned,numberofVACBans,daysSinceLastBan,numberofGameBans,economyban,createdtime)
        return myPlayerBan
