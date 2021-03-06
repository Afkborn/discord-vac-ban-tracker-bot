
# 'steamid': '76561199089429877',
# 'communityvisibilitystate': 3,
# 'profilestate': 1,
# 'personaname': 'Bepantol',
# 'profileurl': 'https://steamcommunity.com/profiles/76561199089429877/',
# 'avatar': 'https://avatars.akamai.steamstatic.com/9221e2ff17cff04f8f87794fe16a0fae199df68d.jpg',
# 'avatarmedium': 'https://avatars.akamai.steamstatic.com/9221e2ff17cff04f8f87794fe16a0fae199df68d_medium.jpg'e': 1,
# 'primaryclanid': '103582791429521408',
# 'timecreated': 1599678945,
# 'personastateflags': 0
## loccountrycode, locstatecode, loccityid, realname her zaman yok hesap public ise oluyor
from time import time
from ..Timer import *
class Player():

    def __init__(self,
        ID : int = None,
        steamID : str = None,
        communityVisibilityState : int = None,
        profileState : int = None,
        personaName : str = None,
        commentpermission : int = None,
        profileURL : str = None,
        avatar : str = None,
        avatarMedium : str = None,
        avatarFull : str = None,
        avatarHash : str = None,
        personaState : int = None,
        primaryClanID : str = None,
        timeCreated : int = None,
        personaStateFlags : int = None,
        createdTime : float = None,
        lastlogoff : int = None,
        loccountrycode : str = None,
        locstatecode : str = None,
        loccityid : int = None,
        realname : str = None,
        gameid : str = None,
        gameextrainfo : str = None,
        gameserverip : str = None,
        ) -> None:
        if (ID == None):
            self.__ID = None
        else:
            self.__ID =int(ID) 
        self.__steamID = int(steamID)
        self.__communityVisibilityState = int(communityVisibilityState)
        self.__profileState = int(profileState)
        self.__personaName = str(personaName)
        self.__profileURL = str(profileURL)
        self.__avatar = str(avatar)
        self.__avatarMedium = str(avatarMedium)
        self.__avatarFull = str(avatarFull)
        self.__avatarHash = str(avatarHash)
        self.__commentPermission = int(commentpermission)
        self.__personaState = int(personaState)
        self.__primaryClanID = int(primaryClanID)
        self.__timeCreated = int(timeCreated)
        self.__personaStateFlags = int(personaStateFlags)
        self.__createdTime = float(createdTime)
        
        
        #private variables
        self.__lastlogoff = lastlogoff
        self.__realName = realname
        self.__locCountryCode = loccountrycode
        self.__locStateCode = locstatecode
        self.__locCityID =  loccityid
        
        #not in db
        self.__gameid = gameid
        self.__gameextrainfo = gameextrainfo
        self.__gameserverip = gameserverip
        
    def getID(self) -> int:
        if (self.__ID == None):
            return 0
        return self.__ID
    def getSteamID(self) -> str:
        return self.__steamID
    def getCommunityVisibilityState(self) -> int:
        return self.__communityVisibilityState
    def getProfileState(self) -> int:
        if (self.__profileState == None):
            return 0
        return self.__profileState
    def getPersonaName(self) -> str:
        return self.__personaName
    def getProfileURL(self) -> str:
        return self.__profileURL
    def getAvatar(self) -> str:
        return self.__avatar
    def getAvatarMedium(self) -> str:
        return self.__avatarMedium
    def getAvatarFull(self) -> str:
        return self.__avatarFull
    def getAvatarHash(self) -> str:
        return self.__avatarHash
    def getCommentPermission(self) -> int:
        if (self.__commentPermission == None):
            return 0
        return self.__commentPermission
    def getPersonaState(self) -> int:
        if (self.__personaState == None):
            return 0
        return self.__personaState
    def getPrimaryClanID(self) -> str:
        return self.__primaryClanID
    def getTimeCreated(self) -> int:
        if (self.__timeCreated == None):
            return 0
        return self.__timeCreated
    def getPersonaStateFlags(self) -> int:
        if (self.__personaStateFlags == None):
            return 0
        return self.__personaStateFlags
    def getCreatedTime(self) -> float:
        return self.__createdTime
    def getLastlogoff(self) -> int:
        if (self.__lastlogoff == None):
            return 0
        return self.__lastlogoff
    def getLocCountryCode(self) -> str:
        return self.__locCountryCode
    def getLocStateCode(self) -> str:
        return self.__locStateCode
    def getLocCityID(self) -> int:
        if (self.__locCityID == None):
            return 0
        return self.__locCityID
    def getRealName(self) -> str:
        return self.__realName
    def getGameID(self) -> str:
        return self.__gameid
    def getGameExtraInfo(self) -> str:
        return self.__gameextrainfo
    def getGameServerIP(self) -> str:
        return self.__gameserverip
    
        
    
    def setID(self, ID : int) -> None:
        self.__ID = ID
    def setSteamID(self, steamID : str) -> None:
        self.__steamID = steamID
    def setCommunityVisibilityState(self, communityVisibilityState : int) -> None:
        self.__communityVisibilityState = communityVisibilityState
    def setProfileState(self, profileState : int) -> None:
        self.__profileState = profileState
    def setPersonaName(self, personaName : str) -> None:
        self.__personaName = personaName
    def setProfileURL(self, profileURL : str) -> None:
        self.__profileURL = profileURL
    def setAvatar(self, avatar : str) -> None:
        self.__avatar = avatar
    def setAvatarMedium(self, avatarMedium : str) -> None:
        self.__avatarMedium = avatarMedium
    def setAvatarFull(self, avatarFull : str) -> None:
        self.__avatarFull = avatarFull
    def setAvatarHash(self, avatarHash : str) -> None:
        self.__avatarHash = avatarHash
    def setCommentPermission(self, commentPermission : int) -> None:
        self.__commentPermission = commentPermission
    def setPersonaState(self, personaState : int) -> None:
        self.__personaState = personaState
    def setPrimaryClanID(self, primaryClanID : str) -> None:
        self.__primaryClanID = primaryClanID
    def setTimeCreated(self, timeCreated : int) -> None:
        self.__timeCreated = timeCreated
    def setPersonaStateFlags(self, personaStateFlags : int) -> None:
        self.__personaStateFlags = personaStateFlags
    def setCreatedTime(self, createdTime : float) -> None:
        self.__createdTime = createdTime
    def setLastlogoff(self, lastlogoff : int) -> None:
        self.__lastlogoff = lastlogoff
    def setLocCountryCode(self, locCountryCode : str) -> None:
        self.__locCountryCode = locCountryCode
    def setLocStateCode(self, locStateCode : str) -> None:
        self.__locStateCode = locStateCode
    def setLocCityID(self, locCityID : int) -> None:
        self.__locCityID = locCityID
    def setRealName(self, realName : str) -> None:
        self.__realName = realName
    def setGameID(self, gameID : str) -> None:
        self.__gameid = gameID
    def setGameExtraInfo(self, gameExtraInfo : str) -> None:
        self.__gameextrainfo = gameExtraInfo
    def setGameServerIP(self, gameServerIP : str) -> None:
        self.__gameserverip = gameServerIP
        
    
    def __str__(self) -> str:
        return f"Player(id={self.__ID}, steamID={self.__steamID}, communityVisibilityState={self.__communityVisibilityState}, profileState={self.__profileState}, personaName={self.__personaName}, profileURL={self.__profileURL}, avatar={self.__avatar}, avatarMedium={self.__avatarMedium}, avatarFull={self.__avatarFull}, avatarHash={self.__avatarHash}, commentPermission={self.__commentPermission}, personaState={self.__personaState}, primaryClanID={self.__primaryClanID}, timeCreated={self.__timeCreated}, personaStateFlags={self.__personaStateFlags}, createdTime={self.__createdTime}, lastLogOff={self.__lastlogoff}, locCountryCode={self.__locCountryCode}, locStateCode={self.__locStateCode}, locCityID={self.__locCityID}, realName={self.__realName}, gameid={self.__gameid}, gameextrainfo={self.__gameextrainfo}, gameserverip={self.__gameserverip})"        
    
    def getVariableType(self) -> str:
        return f"Player(id={type(self.__ID)}, steamID={type(self.__steamID)}, communityVisibilityState={type(self.__communityVisibilityState)}, profileState={type(self.__profileState)}, personaName={type(self.__personaName)}, profileURL={type(self.__profileURL)}, avatar={type(self.__avatar)}, avatarMedium={type(self.__avatarMedium)}, avatarFull={type(self.__avatarFull)}, avatarHash={type(self.__avatarHash)}, commentPermission={type(self.__commentPermission)}, personaState={type(self.__personaState)}, primaryClanID={type(self.__primaryClanID)}, timeCreated={type(self.__timeCreated)}, personaStateFlags={type(self.__personaStateFlags)}, createdTime={type(self.__createdTime)}, lastLogOff={type(self.__lastlogoff)}, locCountryCode={type(self.__locCountryCode)}, locStateCode={type(self.__locStateCode)}, locCityID={type(self.__locCityID)}, realName={type(self.__realName)}, gameid={type(self.__gameid)}, gameextrainfo={type(self.__gameextrainfo)}, gameserverip={type(self.__gameserverip)})"
    
    def getYearsTimeCreated(self) -> int:
        if self.__timeCreated == 0:
            return 0
        return get_relevant_time_created(self.__timeCreated)
        
    
    def getLastOnlineDate(self) -> str:
        if self.__lastlogoff == None:
            return ""
        return get_relevant_last_online_date(self.__lastlogoff)

    
    def getPersonaStateText(self) -> str:
        fullText = ""
        if (self.__personaState == 0):
            fullText += f"Offline\nLast Online: {self.getLastOnlineDate()}"
        elif (self.__personaState == 1):
            fullText += "Online\n"
        elif (self.__personaState == 2):
            fullText += "Busy\n"
        elif (self.__personaState == 3):
            fullText += "Away\n"
        elif (self.__personaState == 4):
            fullText += "Snooze(zZz!)\n"
        elif (self.__personaState == 5):
            fullText += "Looking to trade\n"
        elif (self.__personaState == 6):
            fullText += "Looking to play\n"
        
        if (self.__gameextrainfo != None):
            fullText += f"Game: {self.__gameextrainfo} (Detail $game {self.__gameid})"
        if (self.__gameserverip != None):
            fullText += f"Server: {self.__gameserverip}"
        return fullText