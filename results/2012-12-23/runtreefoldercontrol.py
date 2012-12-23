import subprocess

dataDir = 'data/2012-12-19/symmetric_0.5'
outDir = 'results/2012-12-23/treefolder_control'
subprocess.call(['python', 'src/treeCalcFolder.py', dataDir, outDir, '10'])

