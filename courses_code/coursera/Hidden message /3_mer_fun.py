def find_location(s):
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
#        print lst                          
	count=dict()
	for word in lst:
		count[word]=count.get(word,0)+1
	print count
	bigcount=None
	bigword=None
	for word,counts in count.items():
		if bigcount is None or counts>bigcount:
			bigword=word
			bigcount=counts
		print bigword,bigcount

find_location('CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA')