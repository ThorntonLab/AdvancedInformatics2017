from __future__ import print_function
import sys
import os
import collections
import string

infile = sys.argv[1]

if not os.path.isfile(infile):
    raise RuntimeError("Input file "+infile+" not found")

c=collections.Counter()
translator = str.maketrans({key: None for key in string.punctuation})
with open(infile,'r') as f:
    for line in f:
        stripped=line.rstrip('\n').translate(translator).lower()
        words = stripped.split()
        for w in words:
            c[w]+=1

keys=sorted([i for i in c])

with open('gpl3counts.txt','w') as ofile:
    for ki in keys:
        ofile.write(ki + '\t' + str(c[ki]) + '\n')
