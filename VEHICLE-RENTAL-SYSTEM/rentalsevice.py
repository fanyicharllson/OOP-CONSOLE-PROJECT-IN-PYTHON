#Rental Service

class RentalService():
    def  __init__(self):
        self.vehicle_addition_database = []                                                                                                                                                      
        self.customer_registration_database = []
        self.customer_rented_vehicle_database = []
    
    
    #adding vehicle
    def addVehicle(self, vehicle):
        self.vehicle_addition_database.append(vehicle)
        print(f"\n\tVehicle added to database!")
    
    
    #displaying vehicle
    def displayVehicle(self):
        for vehicle in self.vehicle_addition_database:
            print(vehicle)    
            
            
    #customer registration
    def CustomerRegistration(self, objCustomer):
        self.customer_registration_database.append(objCustomer._name)
        print(f"\n\tCustomer registration added to database!")
        
    
    #displaying registered customer
    def DisplayRegisteredCustomer(self):
        print(f"\n\n\tRegistered Customer;")
        for registeredCustomer in self.customer_registration_database:
            print(registeredCustomer)
        
    
    
    #renting vehicle
    def RentingVehicle(self, typeOfVehicle, objVehicle, objcustomer):
        for vehicle in self.vehicle_addition_database:
            if vehicle.type == typeOfVehicle:
                self.customer_rented_vehicle_database.append(vehicle)
                print(f"\n\t{objVehicle.type} rented by {objcustomer._name}")
                return
            print(f"\n\t{objVehicle.type} not available!")    
                 
    
    #returning vehicle
    def returningVehicle(self, typeOfVehicle, objVehicle, objcustomer):
        for returnVehicle in self.customer_rented_vehicle_database:
            if returnVehicle.type == typeOfVehicle:
                self.customer_rented_vehicle_database.remove(returnVehicle)
                self.vehicle_addition_database.append(returnVehicle)
                print(f"\n{objcustomer._name} returned the vehicle {objVehicle.type}")
                return
            print(f"{objcustomer._name} did not rent the vehicle {objVehicle.type}")
                
       