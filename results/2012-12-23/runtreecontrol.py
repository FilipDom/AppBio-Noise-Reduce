#! /usr/bin/env

'''
The result of this script should be a total of six tree files, indelTreeNoisy,
indelTreeDenoised, s001TreeNoisy, s001TreeDenoised, onlynoiseTreeNoisy and
onlynoiseTreeDenoised in the treecalc_control folder. The last two files should
be empty and an error message should be displayed for the last case. 
'''

import os
import sys

#path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
path = os.path.abspath('src')
if not path in sys.path:
    sys.path.append(path)
del path

import treeCalc

treeNoisyOut = open('./results/2012-12-23/treecalc_control/indelTreeNoisy', 'w')
treeDenoisedOut = open('./results/2012-12-23/treecalc_control/indelTreeDenoised', 'w')
treeCalc.calcTrees('data/2012-12-23/treecalc_control/indels.fa', treeNoisyOut, treeDenoisedOut)
treeNoisyOut.close()
treeDenoisedOut.close()

treeNoisyOut = open('results/2012-12-23/treecalc_control/s001TreeNoisy', 'w')
treeDenoisedOut = open('results/2012-12-23/treecalc_control/s001TreeDenoised', 'w')
treeCalc.calcTrees('data/2012-12-23/treecalc_control/s001.align.1.msl', treeNoisyOut, treeDenoisedOut)
treeNoisyOut.close()
treeDenoisedOut.close()

treeNoisyOut = open('results/2012-12-23/treecalc_control/onlynoiseTreeNoisy', 'w')
treeDenoisedOut = open('results/2012-12-23/treecalc_control/onlynoiseTreeDenoised', 'w')
try:
    treeCalc.calcTrees('data/2012-12-23/treecalc_control/only_noise.fa', treeNoisyOut, treeDenoisedOut)
except StandardError as e:
    print >> sys.stderr, e.message
treeNoisyOut.close()
treeDenoisedOut.close()
