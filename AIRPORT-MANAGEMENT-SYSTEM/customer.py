#customer class
from Abstractclass import AbstractAirport



class Customer(AbstractAirport):
    
    def __init__(self, name, uniqueId):
        super().__init__(name, uniqueId)
        
    
    def displayName_UniqueId(self):
        
        print("\n\tCustomer Name and Unique Id...")
        print(f"\n\t Customer Name: {self._name}")
        print(f"\t Customer Id: {self._uniqueId}")
        
     