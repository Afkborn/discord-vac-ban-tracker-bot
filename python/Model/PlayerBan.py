
class PlayerBan():
    def __init__(self, 
        ID : int = None,
        steamID : str = None,
        communityBanned : bool = None,
        VACBanned : bool = None,
        NumberOfVACBans : int = None,
        DaysSinceLastBan : int = None,
        NumberOfGameBans : int = None,
        EconomyBan : str = None,
        CreatedTime : float = None,
        
        ) -> None:
        self.__ID = ID
        self.__steamID = steamID
        self.__communityBanned = communityBanned
        self.__VACBanned = VACBanned
        self.__numberOfVACBans = NumberOfVACBans
        self.__daysSinceLastBan = DaysSinceLastBan
        self.__numberOfGameBans = NumberOfGameBans
        
        if EconomyBan == "none":
            self.__economyBan = None
        else:
            self.__economyBan = EconomyBan
            
        self.__createdTime = CreatedTime
    
    def getID(self) -> int:
        return self.__ID
    def getsteamID(self) -> str:
        return self.__steamID
    def getcommunityBanned(self) -> bool:
        return self.__communityBanned
    def getVACBanned(self) -> bool:
        return self.__VACBanned
    def getNumberOfVACBans(self) -> int:
        return self.__numberOfVACBans
    def getDaysSinceLastBan(self) -> int:
        return self.__daysSinceLastBan
    def getNumberOfGameBans(self) -> int:
        return self.__numberOfGameBans
    def getEconomyBan(self) -> str:
        return self.__economyBan
    def getCreatedTime(self) -> float:
        return self.__createdTime
    

    def setID(self, ID : int) -> None:
        self.__ID = ID
    def setSteamID(self, steamID : str) -> None:
        self.__steamID = steamID
    def setcommunityBanned(self, communityBanned : bool) -> None:
        self.__communityBanned = communityBanned
    def setVACBanned(self, VACBanned : bool) -> None:
        self.__VACBanned = VACBanned
    def setNumberOfVACBans(self, NumberOfVACBans : int) -> None:
        self.__numberOfVACBans = NumberOfVACBans
    def setDaysSinceLastBan(self, DaysSinceLastBan : int) -> None:
        self.__daysSinceLastBan = DaysSinceLastBan
    def setNumberOfGameBans(self, NumberOfGameBans : int) -> None:
        self.__numberOfGameBans = NumberOfGameBans
    def setEconomyBan(self, EconomyBan : str) -> None:
        self.__economyBan = EconomyBan
    def setCreatedTime(self, CreatedTime : float) -> None:
        self.__createdTime = CreatedTime
        
    def __str__(self) -> str:
        return f"PlayerBan(id={self.__ID}, steamID={self.__steamID}, communityBanned={self.__communityBanned}, VACBanned={self.__VACBanned}, NumberOfVACBans={self.__numberOfVACBans}, DaysSinceLastBan={self.__daysSinceLastBan}, NumberOfGameBans={self.__numberOfGameBans}, EconomyBan={self.__economyBan}, CreatedTime={self.__createdTime})"
    
    def getVariableType(self) -> str:
        return f"PlayerBan(id={type(self.__ID)}, steamID={type(self.__steamID)}, communityBanned={type(self.__communityBanned)}, VACBanned={type(self.__VACBanned)}, NumberOfVACBans={type(self.__numberOfVACBans)}, DaysSinceLastBan={type(self.__daysSinceLastBan)}, NumberOfGameBans={type(self.__numberOfGameBans)}, EconomyBan={type(self.__economyBan)}, CreatedTime={type(self.__createdTime)})"
    
    def getVacBanEmoji(self) -> str:
        if self.__VACBanned:
            return ":white_check_mark:"
        else:
            return ":x:"
    
    def getCommunityBannedEmoji(self) -> str:
        if self.__communityBanned:
            return ":white_check_mark:"
        else:
            return ":x:"
    
    def getEconomyBanEmoji(self) -> str:
        if self.__economyBan == None:
            return ":x:"
        else:
            return ":white_check_mark:"

    

    
