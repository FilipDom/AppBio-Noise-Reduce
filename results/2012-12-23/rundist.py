import subprocess

dataBaseDir = 'results/2012-12-23/trees'
refTreeBaseDir = 'data/2012-12-19'
endDirs = ['symmetric_0.5', 'symmetric_1.0', 'symmetric_2.0',
           'asymmetric_0.5', 'asymmetric_1.0', 'asymmetric_2.0']
outDir = 'results/2012-12-23/dist'

for endDir in endDirs:
    dataDir = os.path.join(dataBaseDir, endDir)
    outPath = os.path.join(outBaseDir, endDir)
    subprocess.call(['python', 'src/distCalcFolder.py', dataDir, outDir, '300'])
