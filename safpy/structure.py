# import external libraries
import pandas as pd
import sys
import os
from cmath import nan

# import internal classes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from model import Model
from project import Project
from structuralMaterial import StructuralMaterial
from structuralCrossSection import StructuralCrossSection
from structuralPointConnection import StructuralPointConnection

class StructuralSchema(Model, 
                       Project, 
                       StructuralMaterial, 
                       StructuralCrossSection, 
                       StructuralPointConnection):

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

        self.structuralMaterialDict = {
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

        self.structuralCrossSectionDict = {
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

        self.compositeShapeDefDict = {
            'Name' : [],
            'Material Name 1' : [],
            'Polygon contour 1' : [],
            'Id' : []
        }

        self.structuralPointConnectionDict = {
            'Name' : [],
            'Coordinate X [m]' : [],
            'Coordinate Y [m]' : [],
            'Coordinate Z [m]' : [],
            'Id' : []
        }

        self.structuralCurveEdge = {
            'Name' : [],
            '2D member' : [],
            'Nodes' : [],
            'Segments' : [],
            'Id' : []
        }

        self.structuralCurveMemberDict = {
            'Name': [],
            'Type' : [],
            'Cross section' : [],
            'Arbitary definition' : [],
            'Nodes' : [],
            'Segments' : [],
            'Begin node' : [],
            'End node' : [],
            'Internal nodes' : [],
            'Length [m]' : [],
            'Geometrical shape' : [],
            'Parent ID' : [],
            'LCS' : [],
            'LCS Rotation [deg]' : [],
            'Coordinate X [m]' : [],
            'Coordinate Y [m]' : [],
            'Coordinate Z [m]' : [],
            'System line' : [],
            'Eccentricity ey [mm]' : [],
            'Eccentricity ez [mm]' : [],
            'Layer' : [],
            'Behaviour in analysis' : [],
            'Color' : [],
            'Id' : []
        }

        self.structuralCurveMemberVarying = {
            'Name': [],
            'Cross sections 1': [],
            'Span 1': [],
            'Alignment 1': [],
            'Cross sections 2': [],
            'Span 2': [],
            'Alignment 2': [],
            'Cross sections 3': [],
            'Span 3': [],
            'Alignment 3': [],
            'Id': [],
        }

        self.structuralCurveMemberRib = {
            'Name': [],
            '2D Member': [],
            'Cross Section': [],
            'Nodes': [],
            'Segments': [],
            'Begin Node': [],
            'End Node': [],
            'Internal Nodes': [],
            'Length [m]': [],
            'Geometrical Shape': [],
            'Alignment': [],
            'Eccentricity ez [mm]': [],
            'Type of connection': [],
            'Shape of the rib': [],
            'Layer': [],
            'Behaviour in analysis': [],
            'Effective width': [],
            'Width left for check [mm]': [],
            'Width left for internal forces [mm]': [],
            'Color': [],
            'Parent ID': [],
            'Id': []
        }

        self.structuralSurfaceMemberDict = {
            'Name' : [],
            'Type' : [],
            'Material' : [],
            'Thickness type' : [],
            'Thickness [mm]' : [],
            'System plane at' : [],
            'Nodes' : [],
            'Internal nodes' : [],
            'Edges' : [],
            'Parent ID' : [],
            'Layer' : [],
            'LCS Type' : [],
            'Coordinate X [m]' : [],
            'Coordinate Y [m]' : [],
            'Coordinate Z [m]' : [],
            'LCS Rotation [deg]' : [],
            'Eccentricity ez [mm]' : [],
            'Shape' : [],
            'Behavior in analysis' : [],
            'Color' : [],
            'Id' : []
        }

        self.structuralSurfaceMemberOpeningDict = {
            'Name':[],
            '2D Member':[],
            'Nodes':[],
            'Edges':[],
            'Id':[]
        }

        self.structuralSurfaceMemberRegionDict = {
            'Name': [],
            'Material': [],
            'Thickness [mm]': [],
            'System plane at': [],
            '2D Member': [],
            'Nodes': [],
            'Edges': [],
            'Eccentricity ez [mm]': [],
            'Area [m2]': [],
            'Parent ID': [],
            'Id': []
        }

        self.structuralStoreyDict = {
            'Name' : [],
            'Height level [m]' : [],
            'Id' : []
        }

        self.structuralProxyElementDict = {
            'Name': [],
            'Material': [],
            'Color': [],
            'Layer': [],
            'Id':[]
        }

        self.structuralProxyElementVerticesDict = {
            'Structural proxy element': [],
            'Index': [],
            'X [m]': [],
            'Y [m]': [],
            'Z [m]': []
        }

        self.structuralProxyElementFacesDict = {
            'Structural proxy element': [],
            'Index': [],
            'Definition': []
        }

        self.structuralPointSupportDict = {
            'Name' : [],
            'Type' : [],
            'Node' : [],
            'ux' : [],
            'uy' : [],
            'uz' : [],
            'fix' : [],
            'fiy' : [],
            'fiz' : [],
            'Stiffness X [MN/m]' : [],
            'Stiffness Y [MN/m]' : [],
            'Stiffness Z [MN/m]' : [],
            'Stiffness Fix [MNm/rad]' : [],
            'Stiffness Fix [MNm/rad]' : [],
            'Stiffness Fiz [MNm/rad]' : [],
            'Id' : []
        }

        self.structuralSurfaceConnectionDict = {
            'Name': [],
            '2D Member': [],
            '2D Member Region': [],
            'Subsoil': [],
            'Description': [],
            'C1x [MN/m3]': [],
            'C1y [MN/m3]': [],
            'C1z Spring': [],
            'C1z [MN/m3]': [],
            'C2x [MN/m]': [],
            'C2y [MN/m]': [],
            'Parent ID': [],
            'Id': []
        }

        self.structuralCurveConnectionDict = {
            'Name': [],
            'Type': [],
            'Member': [],
            'Member rib': [],
            'ux': [],
            'uy': [], 
            'uz': [],
            'fix': [],
            'fiy': [],
            'fiz': [],
            'Stiffness X [MN/m2]': [],
            'Stiffness Y [MN/m2]': [],
            'Stiffness Z [MN/m2]': [],
            'Stiffness Fix [MNm/rad/m]': [],
            'Stiffness Fiy [MNm/rad/m]': [],
            'Stiffness Fiz [MNm/rad/m]': [],
            'Coordinate system': [],
            'Coordinate definition': [],
            'Origin': [],
            'Start point [m]': [],
            'End point [m]': [],
            'Parent ID': [],
            'Id': []
        }

        self.structuralEdgeConnectionDict = {
            'Name' : [],
            'Type' : [],
            '2D Member' : [],
            'Edge' : [],
            'ux' : [],
            'uy' : [],
            'uz' : [],
            'fix' : [],
            'fiy' : [],
            'fiz' : [],
            'Stiffness X [MN/m2]' : [],
            'Stiffness Y [MN/m2]' : [],
            'Stiffness Z [MN/m2]' : [],
            'Stiffness Fix [MNm/rad/m]' : [],
            'Stiffness Fiy [MNm/rad/m]' : [],
            'Stiffness Fiz [MNm/rad/m]' : [],
            'Coordinate system' : [],
            'Coordinate definition' : [],
            'Origin' : [],
            'Start point [m]' : [],
            'End point [m]' : [],
            'Id' : []
        }

        self.relConnectsStructuralMemberDict = {
            'Name': [],
            'Member': [],
            'Position': [],
            'ux': [],
            'uy': [],
            'uz': [],
            'fix': [],
            'fiy': [],
            'fiz': [],
            'Stiffness X [MN/m]': [],
            'Stiffness Y [MN/m]': [],
            'Stiffness Z [MN/m]': [],
            'Stiffness Fix [MNm/rad]': [],
            'Stiffness Fiy [MNm/rad]': [],
            'Stiffness Fiz [MNm/rad]': [],
            'Parent ID': [],
            'Id': []
        }

        self.relConnectsSurfaceEdge = {
            'Name': [],
            '2D Member': [],
            'Edge': [],
            'ux': [],
            'uy': [],
            'uz': [],
            'fix': [],
            'fiy': [],
            'fiz': [],
            'Stiffness X [MN/m2]': [],
            'Stiffness Y [MN/m2]': [],
            'Stiffness Z [MN/m2]': [],
            'Stiffness Fix [MNm/rad/m]': [],
            'Stiffness Fiy [MNm/rad/m]': [],
            'Stiffness Fiz [MNm/rad/m]': [],
            'Coordinate definition': [],
            'Origin': [],
            'Start point [m]': [],
            'End point [m]': [],
            'Parent ID': [],
            'Id': []
        }

        self.relConnectsRigidCrossDict = {
            'Name': [],
            '1D Members': [],
            'Type': [],
            'u1': [],
            'u2': [],
            'u': [],
            'fi1': [],
            'fi2': [],
            'fi': [],
            'Stiffness u1 [MN/m]': [],
            'Resistance u1 [MN]': [],
            'Stiffness u2 [MN/m]': [],
            'Resistance u2 [MN]': [],
            'Stiffness u [MN/m]': [],
            'Resistance u [MN]': [],
            'Stiffness fi1 [MNm/rad]': [],
            'Resistance fi1 [MNm]': [],
            'Stiffness fi2 [MNm/rad]': [],
            'Resistance fi2 [MNm]': [],
            'Stiffness fi [MNm/rad]': [],
            'Resistance fi [MNm]': [],
            'Parent ID': [],
            'Id': []
        }

        self.relConnectsRigidLink = {
            'Name': [],
            'Nodes': [],
            'Hinge position': [],
            'ux': [],
            'uy': [],
            'uz': [],
            'fix': [],
            'fiy': [],
            'fiz': [],
            'Stiffness X [MN/m]': [],
            'Resistance X [MN]': [],
            'Stiffness Y [MN/m]': [],
            'Resistance Y [MN]': [],
            'Stiffness Z [MN/m]': [],
            'Resistance Z [MN]': [],
            'Stiffness Fix [MNm/rad]': [],
            'Resistance Fix [MNm]': [],
            'Stiffness Fiy [MNm/rad]': [],
            'Resistance Fiy [MNm]': [],
            'Stiffness Fiz [MNm/rad]': [],
            'Resistance Fiz [MNm]': [],
            'Id': []
        }

        self.relConnectsRigidMemberDict = {
            'Name' : [],
            'Node' : [],
            '2D Members' : [],
            'Edges' : [],
            'Internal edge' : [],
            '1D Members' : [],
            'Type' : [],
            'ux' : [],
            'uy' : [],
            'uz' : [],
            'fix' : [],
            'fiy' : [],
            'fiz' : [],
            'Stiffness X [MN/m2]' : [],
            'Stiffness Y [MN/m2]' : [],
            'Stiffness Z [MN/m2]' : [],
            'Stiffness Fix [MNm/rad/m]' : [],
            'Stiffness Fiy [MNm/rad/m]' : [],
            'Stiffness Fiz [MNm/rad/m]' : [],
            'Resistance Fiz [MNm/m]' : [],
            'Id' : []
        }

        self.structuralLoadGroupDict = {
            'Name' : [],
            'Load group type' : [],
            'Relation' : [],
            'Load type' : [],
            'Id' : []
        }

        self.structuralLoadCaseDict = {
            'Name' : [],
            'Description' : [],
            'Action type' : [],
            'Load group' : [],
            'Load type' : [],
            'Duration' : [],
            'Id' : []
        }

        self.structuralLoadCombinationDict = {
            'Name': [],
            'Description': [],
            'Category': [],
            'National standard': [],
            'Type': [],
            'Load Factor 1': [],
            'Multiplier 1': [],
            'Load Case name 1': [],
            'Load Factor 2': [],
            'Multiplier 2': [],
            'Load Case name 2': [],
            'Id': []
        }

        self.structuralPointActionDict = {
            'Name': [],
            'Type': [],
            'Direction': [],
            'Force action': [],
            'Reference node': [],
            'Reference member': [],
            'Value [kN]': [],
            'Vector (X;Y;Z) [kN]': [],
            'Load case': [],
            'Coordinate system': [],
            'Origin': [],
            'Coordinate definition': [],
            'Position x [m]': [],
            'Repeat (n)': [],
            'Delta x [m]': [],
            'Id': []
        }

        self.structuralPointMomentDict = {
            'Name': [],
            'Type': [],
            'Direction': [],
            'Force action': [],
            'Reference node': [],
            'Value [kNm]': [],
            'Load case': [],
            'Coordinate system': [],
            'Origin': [],
            'Coordinate definition': [],
            'Position X [m]': [],
            'Repeat (n)': [],
            'Delta x [m]': [],
            'Id': [],
        }

        self.structuralCurveActionDict = {
            'Name': [],
            'Type': [],
            'Force action': [],
            'Distribution': [],
            'Direction': [],
            'Value 1 [kN/m]': [],
            'Value 2 [kN/m]': [],
            'Vector 1(X;Y;Z) [kN/m]': [],
            'Vector 2(X;Y;Z) [kN/m]': [],
            'Member': [],
            'Member rib': [],
            '2D Member': [],
            '2D Member Region': [],
            '2D Member Opening': [],
            'Edge': [],
            'Internal edge': [],
            'Load case': [],
            'Coordinate system': [],
            'Location': [],
            'Coordinate definition': [],
            'Origin': [],
            'Extent': [],
            'Start point [m]': [],
            'End point [m]': [],
            'Eccentricity ey [mm]': [],
            'Eccentricity ez [mm]': [],
            'Parent ID': [],
            'Id': []
        }

        self.structuralCurveMomentDict= {
            'Name': [],
            'Type': [],
            'Force action': [],
            'Distribution': [],
            'Direction': [],
            'Value 1 [kNm/m]': [],
            'Value 2 [kNm/m]': [],
            'Member': [],
            'Member rib': [],
            '2D Member': [],
            '2D Member Region': [],
            '2D Member Opening': [],
            'Edge': [],
            'Internal edge': [],
            'Load case': [],
            'Coordinate system': [],
            'Location': [],
            'Coordinate definition': [],
            'Origin': [],
            'Extent': [],
            'Start point [m]': [],
            'End point [m]': [],
            'Parent ID': [],
            'Id': []
        }

        self.structuralSurfaceActionDict = {
            'Name': [],
            'Direction': [],
            'Type': [],
            'Force action': [],
            'Value [kN/m2]': [],
            '2D Member': [],
            '2D Member Region': [],
            '2D Member Distribution': [],
            'Load case': [],
            'Coordinate system': [],
            'Location': [],
            'Parent ID': [],
            'Id': []
        }
        
        self.structuralSurfaceActionThermalDict = {
            'Name': [],
            'Variation': [],
            'TempT [°C]': [],
            'TempB [°C]': [],
            '2D Member': [],
            '2D Member Region ': [],
            'Load case': [],
            'Parent ID': [],
            'Id': []
        }
        
        self.structuralCurveActionThermal = {
            'Name': [],
            'Force action': [],
            'Variation': [],
            'deltaT [°C]': [],
            'TempL [°C]': [],
            'TempR [°C]': [],
            'TempB [°C]': [],
            'Member': [],
            'Member rib': [],
            'Load case': [],
            'Coordinate definition': [],
            'Origin': [],
            'Start point [m]': [],
            'End point [m]': [],
            'Parent ID': [],
            'Id': []
        }

        self.structuralPointActionFreeDict = {
            'Name': [],
            'Type': [],
            'Direction': [],
            'Value [kN]': [],
            'Vector (X;Y;Z) [kN]': [],
            'Load case': [],
            'Coordinate X [m]': [],
            'Coordinate Y [m]': [],
            'Coordinate Z [m]': [],
            'Coordinate system': [],
            'Id': []
        }

        self.structuralCurveActionFreeDict = {
            'Name': [],
            'Type': [],
            'Distribution': [],
            'Direction': [],
            'Value 1 [kN/m]': [],
            'Value 2 [kN/m]': [],
            'Vector 1(X;Y;Z) [kN/m]': [],
            'Vector 2(X;Y;Z) [kN/m]': [],
            'Load case': [],
            'Coordinate X [m]': [],
            'Coordinate Y [m]': [],
            'Coordinate Z [m]': [],
            'Segments': [],
            'Coordinate system': [],
            'Location': [],
            'Id': []
        }

        self.structuralSurfaceActionFreeDict = {
            'Name': [],
            'Direction': [],
            'Type': [],
            'Distribution': [],
            'q [kN/m2]': [],
            'Load case': [],
            'Coordinate X [m]': [],
            'Coordinate Y [m]': [],
            'Coordinate Z [m]': [],
            'Edges': [],
            'Coordinate system': [],
            'Location': [],
            'Id': []
        }

        self.structuralSurfaceActionDistDict = {
            'Name': [],
            'Type': [],
            'Nodes': [],
            'Edges': [],
            'Layer': [],
            'LCS Type': [],
            'Coordinate X [m]': [],
            'Coordinate Y [m]': [],
            'Coordinate Z [m]': [],
            'LCS Rotation [deg]': [],
            'Distribution to': [],
            'Load applied to': [],
            'Id': []
        }

        self.resultInternalForce1DDict = {
            'Result on': [],
            'Member': [],
            'Member Rib': [],
            'Result for': [],
            'Load case': [],
            'Load combination': [],
            'Combination key': [],
            'Section at [m]': [],
            'Index': [],
            'N [kN]': [],
            'Vy [kN]': [],
            'Vz [kN]': [],
            'Mx [kNm]': [],
            'My [kNm]': [],
            'Mz [kNm]': []
        }

    def readExcel(self):
        '''
        Read an external xlsx file to define a StructuralSchema object.
        '''
        # read excel sheets
        self.externalModel = pd.read_excel(r"C:\Users\KaratasD\Desktop\Folders\safpy\safGeometryTest.xlsx", sheet_name="Model", index_col=False)
        self.externalProject = pd.read_excel(r"C:\Users\KaratasD\Desktop\Folders\safpy\safGeometryTest.xlsx", sheet_name="Project", index_col=False)
        self.externalStructuralMaterial = pd.read_excel(r"C:\Users\KaratasD\Desktop\Folders\safpy\safGeometryTest.xlsx", sheet_name="StructuralMaterial")

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
        self.structuralMaterialDict['Name'] = self.externalStructuralMaterial['Name'].to_list()
        self.structuralMaterialDict['Type'] = self.externalStructuralMaterial['Type'].to_list()
        self.structuralMaterialDict['Subtype'] = self.externalStructuralMaterial['Subtype'].to_list()
        self.structuralMaterialDict['Quality'] = self.externalStructuralMaterial['Quality'].to_list()
        self.structuralMaterialDict['Unit mass [kg/m3]'] = self.externalStructuralMaterial['Unit mass [kg/m3]'].to_list()
        self.structuralMaterialDict['E modulus [MPa]'] = self.externalStructuralMaterial['NaE modulus [MPa]me'].to_list()
        self.structuralMaterialDict['G modulus [MPa]'] = self.externalStructuralMaterial['G modulus [MPa]'].to_list()
        self.structuralMaterialDict['Poisson Coefficient'] = self.externalStructuralMaterial['Poisson Coefficient'].to_list()
        self.structuralMaterialDict['Thermal expansion [1/K]'] = self.externalStructuralMaterial['Thermal expansion [1/K]'].to_list()
        self.structuralMaterialDict['Design properties'] = self.externalStructuralMaterial['Design properties'].to_list()
        self.structuralMaterialDict['Id'] = self.externalStructuralMaterial['Id'].to_list()

    def exportExcel(self):

        modelFrame = pd.DataFrame(self.modelDict)
        projectFrame = pd.DataFrame(self.projectDict)
        materialFrame = pd.DataFrame(self.structuralMaterialDict)
        sectionFrame = pd.DataFrame(self.sectionDict)
        pointFrame = pd.DataFrame(self.pointDict)

        safFile = pd.ExcelWriter(r'C:\Users\KaratasD\Desktop\Folders\safpy\mySAF.xlsx')

        modelFrame.to_excel(safFile, sheet_name='Model', index=False, header=False)
        projectFrame.to_excel(safFile, sheet_name='Project', index=False, header=False)
        materialFrame.to_excel(safFile, sheet_name='StructuralMaterial', index=False)
        sectionFrame.to_excel(safFile, sheet_name='StructuralCrossSection', index=False)
        pointFrame.to_excel(safFile, sheet_name='StructuralPointConnection', index=False)

        safFile.save()



