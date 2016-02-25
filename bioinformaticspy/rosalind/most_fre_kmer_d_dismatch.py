fname = raw_input("Enter file name: ")
#x,y,z= open(fname).read().split('\n')
with open(fname) as input_data:
	p, [k,d] = [line.strip() if index == 0 else map(int, line.strip().split()) for index, line in enumerate(input_data.readlines())]


def find(p,k):
	l=list()
	for i in range(len(p)-int(k)):
		if p[i:i+int(k)] not in l:
			if p[i:i+int(k)] not in l : 
				l.append(p[i:i+int(k)])
	return l
	  
#def kmers(p,k):
	lst=list()
	l=find(p,k)
	for mer in l :
		for i in range (len(p)-int(k)): 
			if p[i:].startswith(mer):
				lst.append(mer)  
	return lst

	
def positionskmers(p, k, d):
    lis=list()
    lst=find(p,k)
    for kmer in lst:
    	for i in range (len(p)-int(k)): 
    		if mismatch(p[i:i+int(k)], kmer, d):
    			lis.append(p[i:i+int(k)])
    return lis
	
def final(p,k,d):
	lis= positionskmers(p, k, d)
	pos = {}
	for word in lis:
		pos[word]=pos.get(word,0)+1
	maxValue = max(pos.values())
	for a in [key for key, value in pos.items() if value==maxValue] :
		print "the frequent k-mers:", a	


    	
def mismatch(a, b, d):
	count=0
	for i in range(len(b)):
		if a[i]!=b[i]:
			count=count+1
	if count<=d:
		return True 
	return False
	


#positionskmers(p, k, d)
final(p,k,d)