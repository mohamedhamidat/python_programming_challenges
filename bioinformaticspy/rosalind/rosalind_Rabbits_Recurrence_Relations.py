#def fun(n,k):
#	f=1+ (k**(n-k))*(n-k)
#	print f 
#fun(29,3)

seqs=["atttct", "aaaact", "aaaacc"]
global a
a={}
c={}
for i in range (len(seqs[0])):
	count=0
	countc=0
	for seq in seqs :
		if seq[i]=="a":
			count=count+1	
		else: 
			count=count 
		
		if seq[i]=="c":
			countc=countc+1	
		else: 
			countc=countc 
	
	a[i] =a.get(i, count)
	c[i] =c.get(i, countc)

print "A:", " ".join(map(str,[value for value in a.itervalues()]))
