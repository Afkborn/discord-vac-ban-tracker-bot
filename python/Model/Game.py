class Game:
    def __init__(self,
        id : int = None,
        app_id : int = None,
        name : int = None) -> None:
        self.__id = id
        self.__app_id = app_id
        self.__name = name
        
    def getID(self) -> int:
        return self.__id
    
    def getAppID(self) -> int:
        return self.__app_id
    
    def getName(self) -> int:
        return self.__name
    def getClearName(self) -> str:
        clearName = self.__name.replace("'", "")
        clearName = clearName.replace("\"", "")
        clearName = clearName.replace("\\", "")
        clearName = clearName.replace("/", "")
        clearName = clearName.replace("*", "")
        clearName = clearName.replace("?", "")
        clearName = clearName.replace("<", "")
        clearName = clearName.replace(">", "")
        clearName = clearName.replace("|", "")
        return clearName