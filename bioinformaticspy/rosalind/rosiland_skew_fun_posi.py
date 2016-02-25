fname = raw_input("Enter file name: ")
fh = open(fname)
s=''
for line in fh:
	s=line

def skew(s):
	count=0
	lst=list()
	lst2=list()
	pos=dict()
	for i in range(len(s)):
		if s[i]=='G':
			count=count +1
		elif s[i]=='C': 
			count=count-1
		else:
			count=count
		pos[i+1]=pos.get(i+1,count)
	
	minValue = min(pos.values())
	for a in [key for key, value in pos.items() if value==minValue] :
		print a, 
skew(s) 