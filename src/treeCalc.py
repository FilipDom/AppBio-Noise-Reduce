import sys
import subprocess
from Bio import SeqIO

def calcTrees(inFilePath, treeNoisyOut, treeDenoisedOut):
    '''
	Inferrs both the tree from the specified protein multialignment as well as
	the tree from the same alignment with reduced noise. 
	IN: inFilePath - file containing the protein multialignment
		treeNoisyOut - file handle where the noisy tree is written
		treeDenoisedOut - file handle where the denoised tree is written
	'''
	
    denoisedFileName = 'tmp_denoised.fa'
    try:
        subprocess.check_call(['python', 'src/noiseReduce.py', inFilePath, denoisedFileName])
    except subprocess.CalledProcessError as e:
        raise RuntimeError(e.message)
    
    calcTree(inFilePath, treeNoisyOut)

    denoisedFileName = 'tmp_denoised.fa'
    subprocess.call(['python', 'src/noiseReduce.py', inFilePath, denoisedFileName])
    calcTree(denoisedFileName, treeDenoisedOut)
    subprocess.call(['rm', denoisedFileName])

def calcTree(inFilePath, outFile):
	'''
	Inferrs a tree from the protein multialignment in the specified file and
	writes the results to the specified output. This method used the phylip
	programs protdist and neighbor. 
	IN: inFilePath - file containing the protein multialignment
		outFile - file handle where output is written
	'''
    
    seqRecs = SeqIO.parse(inFilePath, 'fasta')
    entries = list()
    for seqRec in seqRecs:
        acc = seqRec.id
        seq = str(seqRec.seq)
        entry = (acc, seq)
        entries.append(entry)

    phylipInputFile = open('infile', 'w')
    writeEntries(phylipInputFile, entries)
    phylipInputFile.close()
    
    subprocess.call(['rm', '-f', 'outfile'])
    protdist = subprocess.Popen(['protdist'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    protdist.stdin.write('Y\n')
    protdist.stdin.write('\n')
    protdist.stdin.flush()
    for line in protdist.stdout:
        #do nothing, prevents program from blocking due to a full pipe
        pass
    protdist.wait()

    subprocess.call(['mv', 'outfile', 'infile'])
    subprocess.call(['rm', '-f', 'outtree'])
    neighbor = subprocess.Popen(['neighbor'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    neighbor.stdin.write('Y\n')
    neighbor.stdin.write('\n')
    neighbor.stdin.flush()
    for line in neighbor.stdout:
        #do nothing, prevents program from blocking due to a full pipe
        pass
    neighbor.wait()

    treeFile = open('outtree', 'r')
    tree = treeFile.read()
    treeFile.close()
    tree = tree.replace('\n', '')
    tree = tree.replace('\r', '')
    for i in xrange(len(entries)):
        acc = entries[i][0]
        tree = tree.replace('#' + str(i), acc)
    print >> outFile, tree
    outFile.flush()

    #cleanup
    subprocess.call(['rm', 'outtree'])
    subprocess.call(['rm', 'outfile'])
    subprocess.call(['rm', 'infile'])

def writeEntries(outFile, entries):
    '''
    Formats the entries in as expected by the Phylipe Seqboot programme. First
    the number of entries and maximum sequence length is written, followed by
    an accession of length 10 and the sequence in every line.
    In: outFile - file handle where output should be written
        entreis - sequences to be written in the form (accession, sequence)
    '''
    maxLen = 0
    for entry in entries:
        seq = entry[1]
        if (maxLen < len(seq)):
            maxLen = len(seq)
    entryCount = len(entries)

    print >> outFile, '%5s %5s' % (entryCount, maxLen)
    for i in xrange(entryCount):
        seq = entries[i][1]
        print >> outFile, '{:<10s}{:s}'.format('#' + str(i), seq)
