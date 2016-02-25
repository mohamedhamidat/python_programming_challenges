fname = raw_input("Enter file name: ")

map= {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
       "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

def translate_RNA_codon(seq): 
	prot=''
	for i in range (0, len(seq),3):
		codon=seq[i:i+3]
		if map[codon]=='STOP':break
		prot+= map[codon]
	return prot

with open(fname) as fh:
	line=fh.read().replace('\n', '')# otherwise you got error unhashable type: 'list'

#	for line in fh:
#		line=line.split # only one line 	
#	translate_RNA_codon(line)
Outfile='Output.'+fname 
with open(Outfile,"w") as trans_prot:
	trans_prot.write(translate_RNA_codon(line))
	trans_prot.close()
print "Done !"