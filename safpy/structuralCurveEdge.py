class StructuralCurveEdge:

    def __init__(self) -> None:
        pass

    def getCurveEdgeInfo(self):

        return self.curveEdgeDict

    def addCurveEdge(self, 
                   curveEdgeName: str = "",
                   curveEdge2DMember: str = "",
                   curveEdgeNodes: str = "",
                   curveEdgeSegments: str = "",
                   curveEdgeId: str = ""):

        self.curveEdgeName = curveEdgeName
        self.curveEdge2DMember = curveEdge2DMember
        self.curveEdgeNodes = curveEdgeNodes
        self.curveEdgeSegments = curveEdgeSegments
        self.curveEdgeId = curveEdgeId

        self.curveEdgeDict['Name'].append(self.curveEdgeName)
        self.curveEdgeDict['2D Member'].append(self.curveEdge2DMember)
        self.curveEdgeDict['Nodes'].append(self.curveEdgeNodes)
        self.curveEdgeDict['Segments'].append(self.curveEdgeSegments)
        self.curveEdgeDict['Id'].append(self.curveEdgeId)

        
        