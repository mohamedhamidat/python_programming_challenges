#s='ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG'
#print s
#print len(s)
#s1=['ATCGGTCGAA','ATCGGTCGAGCGTGT']
#for char in s1:
#	s=s.replace(char,'')
#print s
#print len(s)

#myfile=open("rosalind_splc.txt","r").readlines()[1::2]
#print myfile
map= {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'', 'TAG':'',
    'TGC':'C', 'TGT':'C', 'TGA':'', 'TGG':'W',}

def translate_RNA_codon(seq): 
	prot=''
	for i in range (0, len(seq), 3):
#		if map[codon]=='_':break #to avoid printing STop instes-ad of using stop=seq_start.find('TAA')
		if seq[i:i+3] in map: 
			codon=seq[i:i+3]
			prot+= map[codon]
	return prot


myfile=open("rosalind_splc.txt","r") 
	
raw= myfile.read()
l=[]
for seqblock in raw.split(">")[1:]:
	parts = seqblock.split("\n") # or ("\r\n")
	fasta = parts[0]
	seq = ''.join(parts[1:])
	#print ">" + fasta +'\n'+ seq format fasta 
	l.append(seq)
s=l[0]
intron =[item for item in l[1:]]
#print intron

#print len(intron) 
print len(s)

for char in intron:
	s=s.replace(char,'')
#print s
print len(s)
print translate_RNA_codon(s)

