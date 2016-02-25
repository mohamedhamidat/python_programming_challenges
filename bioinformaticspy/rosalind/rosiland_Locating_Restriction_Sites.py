def revcomp(dna):
	basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	line=[basecomplement[i] for i in dna.strip()]
	line.reverse()
	return ''.join(line)
#line.reverse()	

#example

l='TCAATGCATGCGGGTCTATATGCAT'  

d={}
for n in range (4,13,2):
	for i in range (len(l)-(n-1)):
		if l[i:i+n]==revcomp(l[i:i+n]):
			d[i+1] =d.get(i+1, n)
for item, key in d.items():
	print item, key

print '###########'

myfile=open("rosalind_revp.txt","r") 
	
raw= myfile.read()#list
l=[]
for seqblock in raw.split(">")[1:]:
	parts = seqblock.split("\n") # or ("\r\n")
	fasta = parts[0]
	seq = ''.join(parts[1:])
	l.append(seq)
l=l[0] #sequence

d={}
for n in range (4,13,2):
	for i in range (len(l)-(n-1)):
		if l[i:i+n]==revcomp(l[i:i+n]): 
			d[i+1] =d.get(i+1, n)

for key in sorted (d):
	print key, d[key]

