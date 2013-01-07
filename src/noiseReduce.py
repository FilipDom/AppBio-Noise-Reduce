#! /usr/bin/env python

import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

INDEL = '-'

def main(args):

    filename = args[0]
    seqRecs = SeqIO.parse(filename, 'fasta')
    entries = list()
    for seqRec in seqRecs:
        seq = seqRec.seq.upper()
        acc = seqRec.id
        entry = (acc, seq)
        entries.append(entry)

    entriesDenoised = denoise(entries)
    seqLenNew = len(entriesDenoised[0][1])
    if (seqLenNew == 0):
        print >> sys.stderr, 'Error! All columns have been removed.'
        sys.exit(1)
    outStream = sys.stdout
    if (len(args) >= 2):
        outStream = open(args[1], 'w')
    for entry in entriesDenoised:
        acc = entry[0]
        seq = entry[1]
        seqRec = SeqRecord(Seq(seq), id=acc, description='')
        SeqIO.write(seqRec, outStream, 'fasta')

    outStream.close()    

def denoise(entries):
	'''
	Performs noise reduction for the given protein multialignment specified as 
	a list of (accession, sequence) pairs. Columns with a high number of indels, 
	high number of unique amino acids and a in which no amino acid appears more
	than twice are removed. 
	IN: entries - the multiple sequence alignment
	OUT: the same multiple sequence alignment with noisy columns removed
	'''
    seqLenMax = len(entries[0][1])
    #seqLenMax = 0
    #for entry in entries:
    #    seqLen = len(entry[1])
    #    if (seqLenMax < seqLen):
    #        seqLenMax = seqLen

    columns = range(seqLenMax)
    removeHighIndel(entries, columns)
    removeHighUnique(entries, columns)
    removeLowFreqs(entries, columns)

    entriesDenoised = [( entry[0], ''.join([entry[1][col] for col in columns]) ) for entry in entries]
    return entriesDenoised

def removeHighIndel(entries, columns):
	'''
	From the multiple sequence alignment in entries, reads the columns specified 
	by indices in columns and removes those for which the number of indels is 
	greater than 50%
	IN: entries - the multiple sequence alignment
		columns - column indices which to examine
	'''
    entryCount = len(entries)
    THRESHOLD_RATIO = 0.5
    colRemove = list()
    for col in columns:
        indelCount = 0
        for entry in entries:
            seq = entry[1]
            if (seq[col] == INDEL):
                indelCount += 1
        indelRatio = float(indelCount)/entryCount
        if (indelRatio > THRESHOLD_RATIO):
            colRemove.append(col)

    for col in colRemove:
        columns.remove(col)

def removeHighUnique(entries, columns):
	'''
	From the multiple sequence alignment in entries, reads the columns specified 
	by indices in columns and removes those in which the number of unique amino 
	acids is greater than 50%. Indels are not counted. 
	IN: entries - the multiple sequence alignment
		columns - column indices which to examine
	'''
    entryCount = len(entries)
    THRESHOLD_RATIO = 0.5
    colRemove = list()
    for col in columns:
        symbolPresence = dict()
        for entry in entries:
            seq = entry[1]
            symbolPresence[seq[col]] = 1
        symbolPresence[INDEL] = 0
        uniqueSymbols = sum(symbolPresence.itervalues())
        uniqueRatio = float(uniqueSymbols)/entryCount
        if (uniqueRatio > THRESHOLD_RATIO):
            colRemove.append(col)
    
    for col in colRemove:
        columns.remove(col)


def removeLowFreqs(entries, columns):
	'''
	From the multiple sequence alignment in entries, reads the columns specified 
	by indices in columns and removes those where no amino acid appears more 
	than twice. 
	IN: entries - the multiple sequence alignment
		columns - column indices which to examine
	'''
    MIN_COUNT = 3
    colRemove = list()
    for col in columns:
        symbolCount = dict()
        for entry in entries:
            seq = entry[1]
            symbol = seq[col]
            symbolCount[symbol] = symbolCount.get(symbol, 0) + 1
        
        symbolCount[INDEL] = 0
        freqMax = max(symbolCount.values())
        if (freqMax < MIN_COUNT):
            colRemove.append(col)
    
    for col in colRemove:
        columns.remove(col)

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
if (argsLen < 1 or argsLen > 2):
    print >> sys.stderr, 'The number of input arguments is incorrect!'
    print >> sys.stderr, USAGE
    sys.exit(2)
main(args)
