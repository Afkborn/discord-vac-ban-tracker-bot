class Track:
    def __init__(self,
                id : int = None,
                ownerDiscordID : int = None,
                steamID : int = None,
                time : float = None,
                channel_id : int = None,
                is_banned : bool = None,
                banned_time : float = None
                ) -> None:
        self.__id = id
        self.__ownerDiscordID = ownerDiscordID
        self.__steamID = steamID
        self.__time = time
        self.__channelID = channel_id
        self.__is_banned= is_banned
        self.__banned_time = banned_time
        
    def getID(self) -> int:
        return self.__id
    def getOwnerDiscordID(self) -> int:
        return self.__ownerDiscordID
    def getSteamID(self) -> int:
        return self.__steamID
    def getTime(self) -> float:
        return self.__time
    def getChannelID(self) -> int:
        return self.__channelID
    def getIsBanned(self) -> bool:
        if self.__is_banned == None:
            return False
        return self.__is_banned
    def getBannedTime(self) -> float:
        if self.__banned_time == None:
            return 0
        return self.__banned_time
    
    def setID(self, id : int) -> None:
        self.__id = id
    def setOwnerDiscordID(self, ownerDiscordID : int) -> None:
        self.__ownerDiscordID = ownerDiscordID
    def setSteamID(self, steamID : int) -> None:
        self.__steamID = steamID
    def setTime(self, time : float) -> None:
        self.__time = time
    def setChannelID(self, channel_id : int) -> None:
        self.__channelID = channel_id
    def setIsBanned(self, is_banned : bool) -> None:
        self.__is_banned = is_banned
    def setBannedTime(self, banned_time : float) -> None:
        self.__banned_time = banned_time
    
    def getURL(self) -> str:
        #https://steamcommunity.com/profiles/ID/
        return f"https://steamcommunity.com/profiles/{self.getSteamID()}"
        