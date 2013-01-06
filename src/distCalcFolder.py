#! /usr/bin/env python

import sys
import os
import dendropy

def main(args):

    dataDir = args[0]
    refTreeFilename = args[1]
    outFile = sys.stdout
    isStdoutFree = False
    if (len(args) >= 3):
        outFilename = args[3]
        outFile = open(outFilename, 'w')
        isStdoutFree = True
    DEFAULT_COUNT = 300
    dataCount = DEFAULT_COUNT
    if (len(args) >= 2):
        dataCount = int(args[2])

    TREE_FORMAT = 'newick'
    treeRef = dendropy.Tree.get_from_path(refTreeFilename, TREE_FORMAT)
    HEADER = 'filename\td_noisy\td_denoised'
    print >> outFile, HEADER
    if (isStdoutFree):
        print 'Processing ' + dataDir
        print 'Progress: '
    for i in xrange(1, dataCount+1):
        if (isStdoutFree):
            print '\t' + str(i) + '/' + str(dataCount)
        
        filenamePrefix = 's' + '{:03d}'.format(i)
        
        treeNoisyName = filenamePrefix + 'Noisy.tree'
        treeNoisyPath = os.path.join(dataDir, treeNoisyName)
        if not os.path.exists(treeNoisyPath):
            continue
        treeNoisy = dendropy.Tree.get_from_path(treeNoisyPath, TREE_FORMAT)
        distNoisy = treeRef.symmetric_difference(treeNoisy)

        treeDenoisedName = filenamePrefix + 'Denoised.tree'
        treeDenoisedPath = os.path.join(dataDir, treeDenoisedName)
        treeDenoised = dendropy.Tree.get_from_path(treeDenoisedPath, TREE_FORMAT)
        distDenoised = treeRef.symmetric_difference(treeDenoised)

        print >> outFile, filenamePrefix, '\t', distNoisy, '\t', distDenoised

    outFile.close()
    
    
args = sys.argv[1:]
USAGE = '''
Program usage:\n
    distCalcFolder.py <folder_with_trees> <path_to_ref_tree> <tree_count> <output_file>\n
Folder with trees should contain pairs of noisy and denoised trees with\n
filenames such as s001Noisy.tree and s001Denoised.tree. At the moment, only numbers\n
up to 999 are supported and three digits must be written.\n
'''
if (len(args) < 2 or len(args) > 4):
    print USAGE
    sys.exit(2)
main(args)
