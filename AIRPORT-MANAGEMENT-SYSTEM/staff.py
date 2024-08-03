#staff class=========
from Abstractclass import AbstractAirport

class Staff(AbstractAirport):
    
    def __init__(self, name, uniqueId,employeenumber):
        
        super().__init__(name, uniqueId) 
        self._employeenumber = employeenumber
    
    @property
    def get_employeenumber(self):
        return self._employeenumber
    
    def displayName_UniqueId(self):
        print("\tStaff Information Below...")
        print(f"\n\tStaff Name: {self._name}")
        print(f"\tStaff Unique Id: {self._uniqueId}")
        print(f"\tStaff Employee Number: {self._employeenumber}")
        
        