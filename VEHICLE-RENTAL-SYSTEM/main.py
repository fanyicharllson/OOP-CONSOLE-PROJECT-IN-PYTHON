#main.py=========
from customer import Customer
from vehicle import Vehicle
from rentalsevice import RentalService

#creating customer
customer1 = Customer("Paul", "C001", "TOYOTA")
customer2 = Customer("John", "C002", "Cadilac")
customer3 = Customer("Peter", "C003", "Truck")

#creating vehicle
vehicle1 = Vehicle("V001", "TOYOTA")
vehicle2 = Vehicle("V002", "Truck")
vehicle3 = Vehicle("V003", "Cadilac")
vehicle4 = Vehicle("V004", "Roys")


#adding vehicle to database
rentalService = RentalService() #rental service instance

rentalService.addVehicle(vehicle1)
rentalService.addVehicle(vehicle2)
rentalService.addVehicle(vehicle3)
rentalService.addVehicle(vehicle4)

#displaying vehicle
rentalService.displayVehicle()


#registring customer
rentalService.CustomerRegistration(customer1)
rentalService.CustomerRegistration(customer2)
rentalService.CustomerRegistration(customer3)

#displaying registered customer
rentalService.DisplayRegisteredCustomer()


#renting vehicle
rentalService.RentingVehicle("Truck", vehicle2, customer2)
rentalService.RentingVehicle("TOYOTA", vehicle1, customer1)


#returning vehicle
rentalService.returningVehicle("Truck", vehicle2, customer3)

