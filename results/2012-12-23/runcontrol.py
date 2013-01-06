import os
import subprocess

'''
Runs all the control scripts associated with experiment. 
'''

baseDir = 'results/2012-12-23/'
treeScript = 'runtreecontrol.py'
treePath = os.path.join(baseDir, treeScript)
subprocess.call(['python', treePath])

treeFolderScript = 'runtreefoldercontrol.py'
treeFolderPath = os.path.join(baseDir, treeFolderScript)
subprocess.call(['python', treeFolderPath])