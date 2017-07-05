__author__ = "freyberg"
__version__ = "1.0.1"
__email__ = "yfreyberg@gmail.com"

import os
import shutil

jetbrainsdir = os.getenv('LOCALAPPDATA') +"\\JetBrains\\Transient"
for root, dirs, files in os.walk(jetbrainsdir):
    for name in dirs:
        if "ReSharperPlatformVs" in root and name == "SolutionCaches":
            dirname= os.path.join(root, name)
            shutil.rmtree(dirname)    
            print 'deleted: ' dirname
