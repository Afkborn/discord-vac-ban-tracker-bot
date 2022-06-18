class Friend:
    def __init__(self, 
                id : int = None,
                ownerSteamID : str = None,
                friendSteamID : str = None,
                relationship : str = None,
                friendSince : float = None,
    ) -> None:
        if id == None:
            self.__id = None
        else:
            self.__id = int(id)
        self.__ownerSteamID = ownerSteamID
        self.__friendSteamID = friendSteamID
        self.__relationship = relationship
        self.__friendSince = friendSince
        
    def getID(self) -> int:
        return self.__id
    def getOwnerSteamID(self) -> str:
        return self.__ownerSteamID
    def getFriendSteamID(self) -> str:
        return self.__friendSteamID
    def getRelationship(self) -> str:
        return self.__relationship
    def getFriendSince(self) -> float:
        return self.__friendSince
    
    def setID(self, id : int) -> None:
        self.__id = id
    def setOwnerSteamID(self, ownerSteamID : str) -> None:
        self.__ownerSteamID = ownerSteamID
    def setFriendSteamID(self, friendSteamID : str) -> None:
        self.__friendSteamID = friendSteamID
    def setRelationship(self, relationship : str) -> None:
        self.__relationship = relationship
    def setFriendSince(self, friendSince : float) -> None:
        self.__friendSince = friendSince