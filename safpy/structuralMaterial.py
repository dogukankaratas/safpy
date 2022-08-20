class StructuralMaterial:

    def getMaterialInfo(self):

        return self.materialDict

    def addMaterial(self, 
                    materialName: str = "", 
                    materialType: str = "", 
                    materialSubtype: str = "", 
                    materialQuality: str = "", 
                    materialUnitMass: float = None, 
                    materialEMod: float = None, 
                    materialGMod: float = None, 
                    materialPoisson: float = None, 
                    materialThermal: float = None,  
                    materialDesignProps: float = None, 
                    materialId: int = None):

        self.materialName = materialName
        self.materialType = materialType
        self.materialSubtype = materialSubtype
        self.materialQuality= materialQuality
        self.materialUnitMass = materialUnitMass
        self.materialEMod = materialEMod
        self.materialGMod = materialGMod
        self.materialPoisson = materialPoisson
        self.materialThermal = materialThermal
        self.materialDesignProps = materialDesignProps
        self.materialId = materialId

        self.materialDict['Name'].append(self.materialName)
        self.materialDict['Type'].append(self.materialType)
        self.materialDict['Subtype'].append(self.materialSubtype)
        self.materialDict['Quality'].append(self.materialQuality)
        self.materialDict['Unit mass [kg/m3]'].append(self.materialUnitMass)
        self.materialDict['E modulus [MPa]'].append(self.materialEMod)
        self.materialDict['G modulus [MPa]'].append(self.materialGMod)
        self.materialDict['Poisson Coefficient'].append(self.materialPoisson)
        self.materialDict['Thermal expansion [1/K]'].append(self.materialThermal)
        self.materialDict['Design properties'].append(self.materialDesignProps)
        self.materialDict['Id'].append(self.materialId)