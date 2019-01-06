import os
class Configuration(object):
    __instance=None
    __secret_key=None
    __directoryPath=None
    __dbdirectory=None
    __databasedirpath=None
    def __new__(cls, *args, **kwargs):
        if Configuration.__instance==None:
            Configuration.__instance=object.__new__(cls)
            Configuration.__instance.__init__(*args,**kwargs)
            return Configuration.__instance
        else:
            return Configuration.__instance
    def __init__(self,secret_key,dbdirectory,dbName):
        self.__secret_key=secret_key
        self.__directoryPath=os.path.abspath(os.path.dirname(__name__))
        self.__dbdirectory=dbdirectory
        self.__databasedirpath=os.path.join(self.__directoryPath,self.__dbdirectory)
        self.__dbName=dbName
        self.__connectionString="sqlite:///"+os.path.join(self.__databasedirpath,self.__dbName)
    def SetConnectionString(self,value):
        self.__connectionString=value
    def SetSecretKey(self,value):
        self.__secret_key=value
    def GetSecretKey(self):
        return self.__secret_key
    def GetConnectionString(self):
        return self.__connectionString
    SecretKey=property(GetSecretKey,SetSecretKey)
    ConnectionString=property(GetConnectionString,SetConnectionString)
    def __repr__(self):
        return f'<class {__name__}.Configuration>:"secret_key":{self.__secret_key},directoryPath:"{self.__directoryPath},dbdirectory:{self.__dbdirectory},ConnectionString:{self.__connectionString}"'
