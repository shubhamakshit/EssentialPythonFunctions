import sys
from pathops import PathManipulator
loc = __file__
sys.path.append(PathManipulator.modify_path(loc))
from test import file
print(file)