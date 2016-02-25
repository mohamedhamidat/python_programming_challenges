#fname = raw_input("Enter file name: ")
#[s1,s2]= open(fname).readlines()#.split('\r\n')
#s1,s2 = open(fname).read().split('\n')
#k,l,t=s2.split()
#print k, l, t 
p='CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
k=5
l=50
t=4
#for i in range (0, len(s1), int(l)):
#	s=s1[i:i+int(l)]
#print s
#s=[s1[i:i+int(l)] for i in range(0, len(s1), int(l))]
#find the frequent word for every s
'''first step : find the frequent word '''
list1=list()
list2=list()
count=dict()

for i in range(len(p)-int(k)):
	frq=p[i:i+int(k)]
   	if frq not in list1: 
   		list1.append(frq)
       		
for mer in list1 :
 	for n in range (len(p)-int(k)): 	   		
   		if p[n:].startswith(mer):
   			list2.append(mer)  
		
for word in list2:
	count[word]=count.get(word,0)+1
#lit=list()
#for key, val in count.items():
 #   lit.append((val,key))
#lit.sort()
#for key, val in lit:
#    print key, val,
maxValue = t
freq= [key for key, value in count.items() if value==maxValue]
	


''' second step: position'''
for f in freq:
	list3=list()
	print f
	for i in range (len(p)):
		if p[i:].startswith(f):
			list3.append(i)
	for n in range(t):
		try: 
			if list[n+t]-list[n]<=int(l):
				print i
		except: break 
