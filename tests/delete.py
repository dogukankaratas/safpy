import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from safpy.base import StructuralSchema

mySaf = StructuralSchema()
mySaf.addModelInfo(modelName="myFirstTry")

