#customer class
class Customer:
    def __init__(self, name, customer_id, listOfRentedVehicles):
        self._name = name
        self._customer_id = customer_id
        self._listOfRentedVehicles = listOfRentedVehicles
    
    @property
    def get_name(self):
        return self._name
    
    @property
    def get_customer_id(self):
        return self._customer
    
    @property
    def get_listOfRentedVehicles(self):
        return self._listOfRentedVehicles
    
    def __str__(self):
        return f"Customer Information and Vehicle Rented:\n Customer Name: {self._name}\n Customer Id: {self._customer_id}\n Rented Vehicle: {self._listOfRentedVehicles}"
        
            