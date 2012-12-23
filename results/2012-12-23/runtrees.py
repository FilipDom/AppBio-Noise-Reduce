import os
import subprocess

dataBaseDir = 'data/2012-12-19'
dataEndDirs = ['symmetric_0.5', 'symmetric_1.0', 'symmetric_2.0',
               'asymmetric_0.5', 'asymmetric_1.0', 'asymmetric_2.0']
outBaseDir = 'results/2012-12-23/trees'

for endDir in dataEndDirs:
    dataDir = os.path.join(dataBaseDir, endDir)
    outDir = os.path.join(outBaseDir, endDir)
    if not os.path.exists(outDir):
        os.mkdir(outDir)
    subprocess.call(['python', 'src/treeCalcFolder.py', dataDir, outDir, '300'])
