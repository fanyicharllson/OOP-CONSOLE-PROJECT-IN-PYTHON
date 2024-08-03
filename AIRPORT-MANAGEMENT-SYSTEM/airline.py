#Airline class

class Airline:
    def __init__(self, plane, pilots, staffMemeber):    
        self._plane = plane
        self._pilots = pilots
        self._staffmember = staffMemeber
        self._airlinePlanes = []  #each airline has plane
        self._airlinePilot = []  #each airline has plane with pilot
        self._airlineStaffmember = []  #each airline has staff member
        
        
    
    @property
    def plane(self):
        return self._plane
    
    @property
    def pilot(self):
        return self._pilots
    
    @property
    def staffmemeber(self):
        return self._staffmember
    
    
    def addingPlaneToAirline(self, plane):
        self._airlinePlanes.append(plane)
        self._airlinePlanes.append(self._plane) #adding plane attribute to the airline
        print(f"\n\tPlane Number '{plane.planeNumber}' is added to the Airline!")
    
    
    def  addiingPilotToAirline(self, pilot):
        self._airlinePilot.append(pilot)
        self._airlinePilot.append(self._pilots) #adding pilot attribute to the airlne
        print(f"\n\t'{pilot.name}' has been added to the airline!")
    
    def addingStaffMember(self, staffMember):
        self._airlineStaffmember.append(staffMember)
        self._airlineStaffmember.append(self._staffmember) #adding staff member attribute to the airline
        print(f"\n\tThis Staff Member '{staffMember.name}' has been added to the airline!")
        
        
    
    def __str__(self):
        return f"Plane: {self._plane}\n Staff Memeber: {self._staffmember}\n Pilot: {self._pilots}"
    
    
        
            