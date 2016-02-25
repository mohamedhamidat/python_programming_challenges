dna="gcatgacgttattacgactctgtcacgccgcggtgcgactgaggcgtggcgtctgctggg"
print dna
from string import *
c=count(dna, "a")
print c
t=maketrans("AGCTagct", "TCGAtcga")
a=translate(dna, t)
print a

from string import *
def restrict(dan, enz):
    site = find (dan, enz)
    while site != -1:
	    print "restriction site %s at position %d" % (enz, site)
	    site = find (dan, enz, site + 1)