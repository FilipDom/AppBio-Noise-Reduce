import os
import subprocess

'''
Runs all the data generation scripts associated with experiment. 
This does not include statistical analysis.
'''

baseDir = 'results/2012-12-23/'
treeScript = 'runtrees.py'
treePath = os.path.join(baseDir, treeScript)
subprocess.call(['python', treePath])

distScript = 'rundist.py'
distPath = os.path.join(baseDir, distScript)
subprocess.call(['python', distPath])