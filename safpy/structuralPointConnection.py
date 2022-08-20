class StructuralPointConnection:

    def __init__(self) -> None:
        pass

    def getPointInfo(self):

        return self.pointDict

    def addPoint(self, 
                pointName: str = "", 
                pointX: float = None, 
                pointY: float = None, 
                pointZ: float = None, 
                pointId: int = None):

        self.pointName = pointName
        self.pointX = pointX
        self.pointY = pointY
        self.pointZ = pointZ
        self.pointId = pointId

        self.pointDict['Name'].append(self.pointName)
        self.pointDict['Coordinate X [m]'].append(self.pointX)
        self.pointDict['Coordinate Y [m]'].append(self.pointY)
        self.pointDict['Coordinate Z [m]'].append(self.pointZ)
        self.pointDict['Id'].append(self.pointId)