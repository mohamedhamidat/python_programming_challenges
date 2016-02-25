s='CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA'
lst=list()
l=list()
for i in range(len(s)-3):
    t=s[i:i+3]
    if t not in l: 
        l.append(t)
#   print l
for mer in l :
    for p in range (len(s)-3): 
        if s[p:].startswith(mer):
        	lst.append(mer)                         
count=dict()
for word in lst:
	count[word]=count.get(word,0)+1
bigcount=None
bigword=None
for word,counts in count.items():
	if bigcount is None or counts>bigcount:
		bigword=word
		bigcount=counts
print bigword,bigcount
#import operator

lit=list()
for key, val in count.items():
	lit.append((val,key))
lit.sort()
for key, val in lit:
    print key, val
    
maxValue = max(count.values())
for a in [key for key, value in count.items() if value==maxValue]:
	print "the frequent k-mer:", a