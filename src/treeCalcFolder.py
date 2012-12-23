#! /usr/bin/env python

import sys
import os
import cStringIO
import subprocess
import treeCalc

def main(args):
    
    dataDir = args[0]
    outDir = args[1]
    DEFAULT_COUNT = 300
    dataCount = DEFAULT_COUNT
    if (len(args) >= 2):
        dataCount = int(args[2])

    print 'Processing ' + dataDir
    print 'Progress: '
    for i in xrange(1, dataCount+1):
        print '\t' + str(i) + '/' + str(dataCount)

        filenamePrefix = 's' + '{:03d}'.format(i)
        filename = filenamePrefix + '.align.1.msl'
        filePath = os.path.join(dataDir, filename)

        treeNoisyName = filenamePrefix + 'Noisy.tree'
        treeNoisyPath = os.path.join(outDir, treeNoisyName)
        treeNoisyOut = open(treeNoisyPath, 'w')
        
        treeDenoisedName = filenamePrefix + 'Denoised.tree'
        treeDenoisedPath = os.path.join(outDir, treeDenoisedName)
        treeDenoisedOut = open(treeDenoisedPath, 'w')
        try:
            treeCalc.calcTrees(filePath, treeNoisyOut, treeDenoisedOut)
        except RuntimeError:
            treeNoisyOut.close()
            subprocess.call(['rm', treeNoisyPath])
            treeDenoisedOut.close()
            subprocess.call(['rm', treeDenoisedPath])
            continue
        
        treeNoisyOut.close()
        treeDenoisedOut.close()

args = sys.argv[1:]
main(args)
