#fleight class

class Fleight:
    def __init__(self, flieght_Id, Location, arrivalTime):
        self._fleightId = flieght_Id
        self._location = Location
        self._arrivalTime = arrivalTime
    
    @property
    def get_fleightId(self):
        return self._fleightId
    
    @property
    def get_location(self):
        return self._location
    
    @property
    def get_arrivalTime(self):
        return self._arrivalTime
    
    def __str__(self):
        return f"Fleight Enteries......\n Fleigt Id: {self._fleightId}\n, Location: {self._location}\n, Arrival Time: {self._arrivalTime}"    
    