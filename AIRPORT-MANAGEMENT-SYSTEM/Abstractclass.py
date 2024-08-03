#Absrtact class for airport management system

from abc import ABC, abstractmethod

class AbstractAirport(ABC):
    def __init__(self, name, uniqueId):
        self._name = name
        self._uniqueId = uniqueId
    
    @property
    def getName(self):
        return self._name
    
    @property
    def getUniqueId(self):
        return self._uniqueId
    
    @abstractmethod
    def displayName_UniqueId(self):
        pass    
    