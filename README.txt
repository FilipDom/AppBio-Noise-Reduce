#-------#
| USAGE |
#-------#
All scripts have been written so that they work correctly when called from the 
project root path, ie. the project folder. Otherwise, the relative path 
settings would be incorrect. 
All the scripts use relative paths so they can be run on another system without 
much effort. In order to run them, python needs to be installed on the system, 
and the path and enviromental variables need to be set so that a call such as 

"python <script_name>"

works. 

The scripts used for an individual experiment are in the results folder, under 
a particular experiment subfolder. 

The names "infile", "outfile", "outtree" and "tmp_denoised.fa" should not be 
used as file names in the root directory. These file names are used by some 
scripts and files with those names will be overwritten and deleted. 
For this reason, no two scripts which depend upon these files should be invoked 
at the same time. 

#--------------#
| DEPENDENCIES |
#--------------#
Python 2.7 was used to write the scripts and a compatible version needs to be 
available on the system. The path must also be set so that the "python" command 
may be invoked from the command line. 

Phylip is used to calculate a distance matrix for the mulitple sequence 
alignments and to form a tree using neighbor joining. The path must be set so 
that the commands "protdist" and "neighbor" can be invoked from the command 
line. 

#-------------#
| ASSUMPTIONS |
#-------------#
In order for the program to work correctly, all input files should be valid
multiple sequence alignments in fasta format. This means that there should be
at least three sequences in each file and all sequences should be of the same
length. Indels should be denoted by the character '-'. 
It is assumed that all the sequences are protein sequences. 