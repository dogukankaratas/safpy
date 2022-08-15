class Project:

    def __init__(self) -> None:
        pass

    def getProjectInfo(self):

        return self.projectDict

    def addProjectInfo(self, 
                       projectName: str = '', 
                       projectDesc: str = '', 
                       projectNr: str = '', 
                       projectCreated: str = '',
                       projectLastUpdate: str = '', 
                       projectType: str = '',
                       projectKind: str = '', 
                       projectBuildingType: str = '', 
                       projectStatus: str = '', 
                       projectLocation: str = ''):

        self.projectName = projectName
        self.projectDesc = projectDesc
        self.projectNr = projectNr
        self.projectCreated = projectCreated
        self.projectLastUpdate = projectLastUpdate
        self.projectType = projectType
        self.projectKind = projectKind
        self.projectBuildingType = projectBuildingType
        self.projectStatus = projectStatus
        self.projectLocation = projectLocation

        self.projectDict['responses'][0]=(self.projectName)
        self.projectDict['responses'][1]=(self.projectDesc)
        self.projectDict['responses'][2]=(self.projectNr)
        self.projectDict['responses'][3]=(self.projectCreated)
        self.projectDict['responses'][4]=(self.projectLastUpdate)
        self.projectDict['responses'][5]=(self.projectType)
        self.projectDict['responses'][6]=(self.projectKind)
        self.projectDict['responses'][7]=(self.projectBuildingType)
        self.projectDict['responses'][8]=(self.projectStatus)
        self.projectDict['responses'][9]=(self.projectLocation)
    