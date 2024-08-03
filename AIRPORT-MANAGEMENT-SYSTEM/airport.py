#AIRPORT MANGEMENT SYSTEM

#airport class

class Airport:
    def __init__(self, unique_id, airline):
        self.__unique_id = unique_id
        self.__airline = airline
    
    @property
    def get_unique_id(self):
        return self.__unique_id
    
    @property
    def get_airline(self):
        return self.__airline
        
    