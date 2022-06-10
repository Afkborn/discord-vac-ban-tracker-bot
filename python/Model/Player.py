
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
from time import time
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
        ) -> None:
        self.__ID = ID
        self.__steamID = steamID
        self.__communityVisibilityState = communityVisibilityState
        self.__profileState = profileState
        self.__personaName = personaName
        self.__profileURL = profileURL
        self.__avatar = avatar
        self.__avatarMedium = avatarMedium
        self.__avatarFull = avatarFull
        self.__avatarHash = avatarHash
        self.__commentPermission = commentpermission
        self.__personaState = personaState
        self.__primaryClanID = primaryClanID
        self.__timeCreated = timeCreated
        self.__personaStateFlags = personaStateFlags
        self.__createdTime = createdTime
        
    def getID(self) -> int:
        return self.__ID
    def getSteamID(self) -> str:
        return self.__steamID
    def getCommunityVisibilityState(self) -> int:
        return self.__communityVisibilityState
    def getProfileState(self) -> int:
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
        return self.__commentPermission
    def getPersonaState(self) -> int:
        return self.__personaState
    def getPrimaryClanID(self) -> str:
        return self.__primaryClanID
    def getTimeCreated(self) -> int:
        return self.__timeCreated
    def getPersonaStateFlags(self) -> int:
        return self.__personaStateFlags
    def getCreatedTime(self) -> float:
        return self.__createdTime
    
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
    
    def __str__(self) -> str:
        return f"Player(id={self.__ID}, steamID={self.__steamID}, communityVisibilityState={self.__communityVisibilityState}, profileState={self.__profileState}, personaName={self.__personaName}, profileURL={self.__profileURL}, avatar={self.__avatar}, avatarMedium={self.__avatarMedium}, avatarFull={self.__avatarFull}, avatarHash={self.__avatarHash}, commentPermission={self.__commentPermission}, personaState={self.__personaState}, primaryClanID={self.__primaryClanID}, timeCreated={self.__timeCreated}, personaStateFlags={self.__personaStateFlags}, createdTime={self.__createdTime})"        
    
    def getVariableType(self) -> str:
        return f"Player(id={type(self.__ID)}, steamID={type(self.__steamID)}, communityVisibilityState={type(self.__communityVisibilityState)}, profileState={type(self.__profileState)}, personaName={type(self.__personaName)}, profileURL={type(self.__profileURL)}, avatar={type(self.__avatar)}, avatarMedium={type(self.__avatarMedium)}, avatarFull={type(self.__avatarFull)}, avatarHash={type(self.__avatarHash)}, commentPermission={type(self.__commentPermission)}, personaState={type(self.__personaState)}, primaryClanID={type(self.__primaryClanID)}, timeCreated={type(self.__timeCreated)}, personaStateFlags={type(self.__personaStateFlags)}, createdTime={type(self.__createdTime)})"        
    
    def getYearsTimeCreated(self) -> int:

        uyeOlmaTarihi = time()  - self.__timeCreated
        uyeOlmaTarihi = uyeOlmaTarihi / 31556926
        uyeOlmaTarihi = int(uyeOlmaTarihi)
        return uyeOlmaTarihi