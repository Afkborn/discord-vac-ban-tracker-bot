class Track:
    def __init__(self,
                id : int = None,
                ownerDiscordID : int = None,
                steamID : int = None,
                time : float = None,
                channel_id : int = None
                ) -> None:
        self.__id = id
        self.__ownerDiscordID = ownerDiscordID
        self.__steamID = steamID
        self.__time = time
        self.__channelID = channel_id
        
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
        