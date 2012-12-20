#! /usr/bin/env python

import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

INDEL = '-'

def main(args):

    filename = args[0]
    seqRecs = SeqIO.parse(filename, 'fasta')
    entries = list()
    for seqRec in SeqRecs:
        seq = seqRec.seq.upper()
        acc = seqRec.id
        entry = (acc, seq)
        entries.append(entry)
    
    entries = denoise(entries)

def denoise(entries):
    
    seqLenMax = 0
    for entry in entries:
        seqLen = len(entry[1])
        if (seqLenMax < seqLen):
            seqLenMax = seqLen

    columns = range(seqLenMax)
    removeHighIndel(entries, columns)
    removeHighUnique(entries, columns)
    removeLowFreqs(entries, colums)

    entriesDenoised = [( entry[0], ''.join([entry[1][col] for col in columns]) ) for entry in entries]
    

def removeHighIndel(entries, columns):
    entryCount = len(entries)
    THRESHOLD_RATIO = 0.5
    for col in columns:
        indelCount = 0
        for entry in entries:
            seq = entry[1]
            if (seq[col] == INDEL):
                indelCount += 1
        indelRatio = float(indelCount)/entryCount
        if (indelRatio > THRESHOLD_RATIO):
            columns.remove(col)

def removeHighUnique(entries, colums):
    entryCount = len(entries)
    THRESHOLD_RATIO = 0.5
    for col in colums:
        symbolPresence = dict()
        for entry in entries:
            seq = entry[1]
            symbolPresence[seq[col]] = 1
        uniqueSymbols = len(symbolPresence)
        uniqueRatio = float(uniqueSymbols)/entryCount
        if (uniqueRatio > THRESHOLD_RATIO):
            colums.remove(col)


def removeLowFreqs(entries, colums):
    MIN_COUNT = 3
    for col in colums:
        symbolCount = dict()
        for entry in entries:
            seq = entry[1]
            symbol = seq[col]
            symbolCount[symbol] = symbolCount.get(symbol, 0) + 1
        freqMax = max(symbolCount.values())
        if (freqMax < MIN_COUNT):
            colums.remove(col)

args = sys.argv[1:]
argsLen = len(args)
USAGE = '''
Program usage:\n
\n
noiseReduce <input_filename> <output_filename>\n
\n
The input_filename is required and the input file should contain a\n
multialignment in Fasta format. The output file is optional, if not specified,\n
output will be written to the standard output.\n
'''
if (argsLen < 1 || argsLen > 2):
    print >> sys.stderr, 'The number of input arguments is incorrect!'
    print >> sys.stderr, USAGE
    sys.exit(2)
main(args)
