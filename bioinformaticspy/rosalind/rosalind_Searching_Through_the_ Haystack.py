myfile=open("rosalind_lcsm(1).txt","r") 
	
raw= myfile.read()
l=[]
d={}
for seqblock in raw.split(">")[1:]:
	parts = seqblock.split("\n") # or ("\r\n")
	fasta = parts[0]
	seq = ''.join(parts[1:])
	l.append(seq)
myseq=l[0]
#for seq in l: 
	
kmer_list= []

def kimers(seq):
	for k in range (len(seq)):
		for i in range (len(seq)-k):
			if seq[i:i+k] not in kmer_list:
				kmer_list.append(seq[i:i+k])
	return kmer_list 

#print kimers(myseq)

def fonction(sequence, kmer):
	if kmer in sequence : return True 
results=[]
a={}
for item in kimers(myseq) :
	count=0
	for s in l: 
		if fonction(s, item):
			count=count+1
	a[item] =a.get(item, count)
z= [key for key,val in a.iteritems() if val == max(a.values())]	
y={}
for key in z: 
	y[key] =y.get(key, len(key))
print " ".join(map(str,[key for key,val in y.iteritems() if val == max(y.values())]))