with open("consensus_profile.txt","r") as input: 
	sequences =input.readlines()
	seqs=[]
	for i in range (1, len(sequences),2):
		seqs.append(sequences[i])
	myseq=seqs[1]

a={}
c={}
g={}
t={}
d={}

for i in range (len(seqs[0])-1):
	counta=0
	countc=0
	countg=0
	countt=0
	countd=0
	for seq in seqs:
		if seq[i]=="A":
			counta=counta+1	
		else: 
			counta=counta 
		
		if seq[i]=="C":
			countc=countc+1	
		else: 
			countc=countc
		
		if seq[i]=="G":
			countg=countg+1	
		else: 
			countg=countg
		
		if seq[i]=="T":
			countt=countt+1	
		else: 
			countt=countt  
	
	a[i] =a.get(i, counta)
	d[i] = seq[i]
	c[i] =c.get(i, countc)
	g[i] =g.get(i, countg)
	t[i] =t.get(i, countt)
for value,key in a.iteritems(): 
	if key>(len(seqs)/2):
		myseq=list(myseq) 
		myseq[value]="A"
		myseq=''.join(myseq)

for value,key in c.iteritems(): 
	if key>(len(seqs)/2): 
		myseq=list(myseq) 
		myseq[value]="C"
		myseq=''.join(myseq)
		 
for value,key in g.iteritems(): 
	if key>(len(seqs)/2):
		myseq=list(myseq) 
		myseq[value]="G"
		myseq=''.join(myseq)

		
for value,key in t.iteritems(): 
	if key>(len(seqs)/2): 
		myseq=list(myseq) 
		myseq[value]="T"
		myseq=''.join(myseq)
		
print myseq+"A:", " ".join(map(str,[value for value in a.itervalues()]))
print "C:", " ".join(map(str,[value for value in c.itervalues()]))
print "G:", " ".join(map(str,[value for value in g.itervalues()]))
print "T:", " ".join(map(str,[value for value in t.itervalues()]))