#plane class

class Plane:
    def __init__(self, planeNumber, modelNumber):
        self._planeNumber = planeNumber
        self._modelNumber = modelNumber
    
    @property
    def planeNumber(self):
        return self._planeNumber
    
    @property
    def modelNumber(self):
        return self._modelNumber    
    
    def __str__(self):
        return f"\tPlane Information....\n Plane Number: {self._planeNumber} \n Model Number: {self._modelNumber} \n"    
    
    