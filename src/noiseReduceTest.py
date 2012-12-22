#! /usr/bin/env python

import subprocess
import os
import sys

args = sys.argv[1:]
if (len(args) < 1):
    print >> sys.stderr, 'Expected path to results directory as argument!'
    sys.exit(2)
resultDir = args[0]
print resultDir
controlDir = 'data/2012-12-21/noise_control'
for root, dirs, files in os.walk(controlDir):
    for name in files:
        testFilePath = os.path.join(root, name)
        resultFilename = None
        if '.' in name:
            nameParts = name.rpartition('.')
            resultFilename = nameParts[0] + '_result' + nameParts[1] + nameParts[2]
        else:
            resultFilename = name + '_result'
        resultFilePath = os.path.join(resultDir, resultFilename)
        print resultFilePath
        subprocess.call(['python', 'src/noiseReduce.py', testFilePath, resultFilePath])

