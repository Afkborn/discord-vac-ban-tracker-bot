
class DiscordUser():
    def __init__(self,
        id : int = None,
        discordID : int = None,
        name : str = None,
        avatar_url : str = None,
        joined_at : float = None,
        created_at : float = None,
        ) -> None:
        
        self.__id = id
        self.__discordID = discordID
        self.__name = name
        self.__avatar_url = avatar_url
        self.__joined_at = joined_at
        self.__created_at = created_at
    def getID(self) -> int:
        return self.__id
    def getDiscordID(self) -> int:
        return self.__discordID
    def getName(self) -> str:
        return self.__name
    def getAvatarURL(self) -> str:
        return self.__avatar_url
    def getJoinedAt(self) -> float:
        return self.__joined_at
    def getCreatedAt(self) -> float:
        return self.__created_at
    
    def setID(self, id : int) -> None:
        self.__id = id
    def setDiscordID(self, discordID : int) -> None:
        self.__discordID = discordID
    def setName(self, name : str) -> None:
        self.__name = name
    def setAvatarURL(self, avatar_url : str) -> None:
        self.__avatar_url = avatar_url
    def setJoinedAt(self, joined_at : float) -> None:
        self.__joined_at = joined_at
    def setCreatedAt(self, created_at : float) -> None:
        self.__created_at = created_at
        
        