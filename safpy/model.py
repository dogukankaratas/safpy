class Model:

    def __init__(self) -> None:
        pass

    def getModelInfo(self):

        return self.modelDict

    def addModelInfo(self, 
                     modelName: str = "", 
                     modelDesc: str = "", 
                     modelDisp: str = "", 
                     modelDetail: str = "", 
                     modelStatus: str = "", 
                     modelOwner: str = "", 
                     modelRevNum: str = "", 
                     modelCreated: str = "", 
                     modelLastUpdate: str = "", 
                     modelSourceType: str = "", 
                     modelSourceApp: str = "", 
                     modelSourceCompany: str = "", 
                     modelGlobalCoords: str = "", 
                     modelLCS: str = "", 
                     modelUnits: str = "", 
                     modelSAFVersion: str = "", 
                     modelModuleVersion: str = "", 
                     modelIgnoredObjects: str = "", 
                     modelIgnoredGroups: str = "", 
                     modelID: str = ""):

        self.modelName = modelName
        self.modelDesc = modelDesc
        self.modelDisp = modelDisp
        self.modelDetail = modelDetail
        self.modelStatus = modelStatus
        self.modelOwner = modelOwner
        self.modelRevNum = modelRevNum
        self.modelCreated = modelCreated
        self.modelLastUpdate = modelLastUpdate
        self.modelSourceType = modelSourceType
        self.modelSourceApp = modelSourceApp
        self.modelSourceCompany = modelSourceCompany
        self.modelGlobalCoords = modelGlobalCoords
        self.modelLCS = modelLCS
        self.modelUnits = modelUnits
        self.modelSAFVersion = modelSAFVersion
        self.modelModuleVersion = modelModuleVersion
        self.modelIgnoredObjects = modelIgnoredObjects
        self.modelIgnoredGroups = modelIgnoredGroups
        self.modelID = modelID

        self.modelDict['responses'][0]=(self.modelName)
        self.modelDict['responses'][1]=(self.modelDesc)
        self.modelDict['responses'][2]=(self.modelDisp)
        self.modelDict['responses'][3]=(self.modelDetail)
        self.modelDict['responses'][4]=(self.modelStatus)
        self.modelDict['responses'][5]=(self.modelOwner)
        self.modelDict['responses'][6]=(self.modelRevNum)
        self.modelDict['responses'][7]=(self.modelCreated)
        self.modelDict['responses'][8]=(self.modelLastUpdate)
        self.modelDict['responses'][9]=(self.modelSourceType)
        self.modelDict['responses'][10]=(self.modelSourceApp)
        self.modelDict['responses'][11]=(self.modelSourceCompany)
        self.modelDict['responses'][12]=(self.modelGlobalCoords)
        self.modelDict['responses'][13]=(self.modelLCS)
        self.modelDict['responses'][14]=(self.modelUnits)
        self.modelDict['responses'][15]=(self.modelSAFVersion)
        self.modelDict['responses'][16]=(self.modelModuleVersion)
        self.modelDict['responses'][17]=(self.modelIgnoredObjects)
        self.modelDict['responses'][18]=(self.modelIgnoredGroups)
        self.modelDict['responses'][19]=(self.modelID)