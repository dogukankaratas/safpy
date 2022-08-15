class Section:

    def __init__(self) -> None:
        pass

    def getSectionInfo(self):

        return self.sectionDict

    def addSection(self, 
                   sectionName: str = "", 
                   sectionMaterial: str = "",
                   sectionType: str = "",
                   sectionShape: str = "", 
                   sectionParameters: float = None, 
                   sectionProfile: str = "", 
                   sectionFormCode: str = "", 
                   sectionDescription: int = None, 
                   sectionArea: float = None, 
                   sectionIy: float = None, 
                   sectionIz: float = None, 
                   sectionIt: float = None, 
                   sectionIw: float = None, 
                   sectionWply: float = None, 
                   sectionWplz: float = None,
                   sectionId: int = None):

        self.sectionName = sectionName
        self.sectionMaterial = sectionMaterial
        self.sectionType = sectionType
        self.sectionShape = sectionShape
        self.sectionParameters = sectionParameters
        self.sectionProfile = sectionProfile
        self.sectionFormCode = sectionFormCode
        self.sectionDescription = sectionDescription
        self.sectionArea = sectionArea
        self.sectionIy = sectionIy
        self.sectionIz = sectionIz
        self.sectionIt = sectionIt
        self.sectionIw = sectionIw
        self.sectionWply = sectionWply
        self.sectionWplz = sectionWplz
        self.sectionId = sectionId

        self.sectionDict['Name'].append(self.sectionName)
        self.sectionDict['Material'].append(self.sectionMaterial)
        self.sectionDict['Cross-section type'].append(self.sectionType)
        self.sectionDict['Shape'].append(self.sectionShape)
        self.sectionDict['Parameters [mm]'].append(self.sectionParameters)
        self.sectionDict['Profile'].append(self.sectionProfile)
        self.sectionDict['Form code'].append(self.sectionFormCode)
        self.sectionDict['Description ID of the profile'].append(self.sectionDescription) 
        self.sectionDict['Iy [m4]'].append(self.sectionIy)
        self.sectionDict['Iz [m4]'].append(self.sectionIz) 
        self.sectionDict['It [m4]'].append(self.sectionIt) 
        self.sectionDict['Iw [m6]'].append(self.sectionIw) 
        self.sectionDict['Wply [m3]'].append(self.sectionWply)
        self.sectionDict['Wplz [m3]'].append(self.sectionWplz)
        self.sectionDict['Id'].append(self.sectionId)