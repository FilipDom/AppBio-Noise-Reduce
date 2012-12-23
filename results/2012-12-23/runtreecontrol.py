#! /usr/bin/env

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
