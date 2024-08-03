#pilot class ==========

from Abstractclass import AbstractAirport
class Pilot(AbstractAirport):
    
    def __init__(self, name, uniqueId, pilotLiceneNumber):
        super().__init__(name, uniqueId)
        self._pilotLiceneNumber = pilotLiceneNumber
    
    def displayName_UniqueId(self):
         print("\n\Pilot Name and Unique Id...")
         
         print(f"\n\t Pilot Name: {self._name}")
         print(f"\t Pilot Id: {self._uniqueId}")
         print(f"Pilot Licene Number: {self._pilotLiceneNumber}")
        
    