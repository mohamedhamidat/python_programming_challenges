dna="AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

def reverse_dan(dna):
	dna= [basecomplement[i] for i in dna.strip()]
	dna.reverse()	
	a=''.join(dna)
	return a 
	

genetic_code= {
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
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',}
    
def dan3_pair(dna,k):
	myseq=[]
	seq=dna[k:]
	for i in range (0, len(seq)-k,3):
		myseq.append(seq[i:i+3]) 
	return myseq
stop_codons = ('TGA', 'TAA', 'TAG') 

def verif(dna):
	for stop in dna:
		if stop in stop_codons:
			if "ATG" in dna[:dna.index(stop)]:
				print dna[:dna.index(stop)+1]
				return True 
			else: return False 
			 	
	
	
def verif2(dna):
	for d in stop_codons: 
		if d in dna:
			return True   

from itertools import takewhile
 
def openframe(dna):
	l=[]
	for frame in range (3):
		for i in range (len(dan3_pair(dna,frame))):
			if dan3_pair(dna,frame)[i]=="ATG": 
				#if verif(dan3_pair(dna,frame)[:i]):
					#continue 
				if verif2(dan3_pair(dna,frame)[i:]):
					code= dan3_pair(dna,frame)[i:] 
					coding_sequence  =  takewhile(lambda x: x not in stop_codons and len(x) == 3 ,code)
					a=''.join([genetic_code[codon] for codon in coding_sequence])
					if a not in l: l.append (a)
	return l
				
myfile=open("rosalind_orf(3).txt","r") 
raw= myfile.read()
for seqblock in raw.split(">")[1:]:
	parts = seqblock.split("\n") # or ("\r\n")
	fasta = parts[0]
	seq = ''.join(parts[1:])
l=[]
lis1= openframe(seq)+ openframe (reverse_dan(seq))
for item in lis1: 
	if item not in l:
		l.append(item)
for i in l : print i 