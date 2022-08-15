import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from safpy.structure import StructuralSchema

def test_Structure():
    
    mySaf = StructuralSchema()
    mySaf.addModelInfo(modelName= 'myFirstTestModel')
    mySaf.addProjectInfo(projectLocation= 'Germany')
    mySaf.addMaterial(materialEMod=210000)

    assert mySaf.getModelInfo()['responses'][0] == 'myFirstTestModel'
    assert mySaf.getProjectInfo()['responses'][9] == 'Germany'
    assert mySaf.getMaterialInfo()['E modulus [MPa]'][0] == 210000
    



