import pandas as pd
import sys
import os
from cmath import nan

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from model import Model
from project import Project
from material import Material
from section import Section
from point import Point

class StructuralSchema(Model, Project, Material, Section, Point):

    def __init__(self):

        self.modelDict = {
            'fields' : [
                'Name',
                'Description',
                'Discipline',
                'Level of detail',
                'Status',
                'Owner',
                'Revision number',
                'Created',
                'Last update',
                'Source type',
                'Source application',
                'Source company',
                'Global coordinate system',
                'LCS of cross-section',
                'System of units',
                'SAF Version',
                'Module version',
                'Ignored objects',
                'Ignored groups',
                'Id'
                ],
            'responses': [
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                ''
                ]
        }

        self.projectDict = {
            'fields' : [
                'Name',
                'Description',
                'Project nr',
                'Created',
                'Last update',
                'Project type',
                'Project kind',
                'Building type',
                'Status',
                'Location'
                        ],
            'responses' :[
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                ''
            ]
        }

        self.materialDict = {
            'Name' : [],
            'Type' : [],
            'Subtype' : [],
            'Quality' : [],
            'Unit mass [kg/m3]' : [],
            'E modulus [MPa]' : [],
            'G modulus [MPa]' : [],
            'Poisson Coefficient' : [],
            'Thermal expansion [1/K]' : [],
            'Design properties' : [],
            'Id' : []
            }

        self.sectionDict = {
            'Name' : [],
            'Material' : [],
            'Cross-section type' : [],
            'Shape' : [],
            'Parameters [mm]' : [],
            'Profile' : [],
            'Form code' : [],
            'Description ID of the profile' : [],
            'Iy [m4]' : [],
            'Iz [m4]' : [],
            'It [m4]' : [],
            'Iw [m6]' : [],
            'Wply [m3]' : [],
            'Wplz [m3]' : [],
            'Id' : []
        }

        self.pointDict = {
            'Name' : [],
            'Coordinate X [m]' : [],
            'Coordinate Y [m]' : [],
            'Coordinate Z [m]' : [],
            'Id' : []
        }

    def readExcel(self):
        '''
        Read an external xlsx file to define a StructuralSchema object.
        '''

        # read excel sheets
        self.externalModel = pd.read_excel(r"C:\Users\KaratasD\Desktop\Folders\safpy\safGeometryTest.xlsx", sheet_name="Model", index_col=False)
        self.externalProject = pd.read_excel(r"C:\Users\KaratasD\Desktop\Folders\safpy\safGeometryTest.xlsx", sheet_name="Project", index_col=False)
        externalMaterials = pd.read_excel(r"C:\Users\KaratasD\Desktop\Folders\safpy\safGeometryTest.xlsx", sheet_name="StructuralMaterial")

        # assign model information to object dictionary
        if len(self.externalModel.columns) == 2:

            self.modelResponses = self.externalModel.iloc[: ,1].to_list()

            if self.externalModel.columns[1] == 'Unnamed: 1':
                self.modelResponses.insert(0, nan)
            else:
                self.modelResponses.insert(0, self.externalModel.columns[1])
        else:
            pass

        # assign project information to object dictionary
        if len(self.externalProject.columns) == 2:

            self.projectResponses = self.externalProject.iloc[: ,1].to_list()

            if self.externalProject.columns[1] == 'Unnamed: 1':
                self.projectResponses.insert(0, nan)
            else:
                self.projectResponses.insert(0, self.externalProject.columns[1])

        else:
            pass

        # assign material information to the object dictionary
        self.materialDict['Name'] = externalMaterials['Name'].to_list()
        self.materialDict['Type'] = externalMaterials['Type'].to_list()
        self.materialDict['Subtype'] = externalMaterials['Subtype'].to_list()
        self.materialDict['Quality'] = externalMaterials['Quality'].to_list()
        self.materialDict['Unit mass [kg/m3]'] = externalMaterials['Unit mass [kg/m3]'].to_list()
        self.materialDict['E modulus [MPa]'] = externalMaterials['NaE modulus [MPa]me'].to_list()
        self.materialDict['G modulus [MPa]'] = externalMaterials['G modulus [MPa]'].to_list()
        self.materialDict['Poisson Coefficient'] = externalMaterials['Poisson Coefficient'].to_list()
        self.materialDict['Thermal expansion [1/K]'] = externalMaterials['Thermal expansion [1/K]'].to_list()
        self.materialDict['Design properties'] = externalMaterials['Design properties'].to_list()
        self.materialDict['Id'] = externalMaterials['Id'].to_list()

    def exportExcel(self):

        modelFrame = pd.DataFrame(self.modelDict)
        projectFrame = pd.DataFrame(self.projectDict)
        materialFrame = pd.DataFrame(self.materialDict)
        sectionFrame = pd.DataFrame(self.sectionDict)
        pointFrame = pd.DataFrame(self.pointDict)

        safFile = pd.ExcelWriter(r'C:\Users\KaratasD\Desktop\Folders\safpy\mySAF.xlsx')

        modelFrame.to_excel(safFile, sheet_name='Model', index=False, header=False)
        projectFrame.to_excel(safFile, sheet_name='Project', index=False, header=False)
        materialFrame.to_excel(safFile, sheet_name='StructuralMaterial', index=False)
        sectionFrame.to_excel(safFile, sheet_name='StructuralCrossSection', index=False)
        pointFrame.to_excel(safFile, sheet_name='StructuralPointConnection', index=False)

        safFile.save()



