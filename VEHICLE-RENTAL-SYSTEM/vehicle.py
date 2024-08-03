#Vehhecle class

class Vehicle:
    def __init__(self, vehicle_id, type):
        self.vehicle_id = vehicle_id
        self.type = type
        self.status = True
    
    def __str__(self):
        return f"Vehicle Information:\n Vehicle Id: {self.vehicle_id}\n Type: {self.type}\n Status: {self.status}\n"     
        