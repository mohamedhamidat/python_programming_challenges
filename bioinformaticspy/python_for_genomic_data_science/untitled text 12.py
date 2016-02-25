
       	
#   print l
def find_kmer (s, s2): 
	for mer in a :
		for p in range (len(s)-int(s2)): 
			if s[p:].startswith(mer):
				lst.append(mer)                         
			return lst
kmer= find_kmer (s, s2)
count=dict()
for word in kmer:
	count[word]=count.get(word,0)+1
#lit=list()
#for key, val in count.items():
 #   lit.append((val,key))
#lit.sort()
#for key, val in lit:
#    print key, val,
maxValue = max(count.values())
for a in [key for key, value in count.items() if value==maxValue] :
		print "the frequent k-mers:", a