fname = raw_input("Enter file name: ")
[s,s2]= open(fname).readlines()#.split('\r\n')
lst=list()
l=list()
for i in range(len(s)-int(s2)):
    t=s[i:i+int(s2)]
    if t not in l: 
        l.append(t)
#   print l
for mer in l :
    for p in range (len(s)-int(s2)): 
        if s[p:].startswith(mer):
        	lst.append(mer)                         
count=dict()
for word in lst:
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