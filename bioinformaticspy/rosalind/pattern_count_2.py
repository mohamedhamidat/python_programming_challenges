s2='TTTAGAGCCTTCAGAGG'
s1= 'GAGG'
c=1

def position_in (s,str,d):
	count=0
	for i in range (len(str)-len(s)+1):
		if mismatch(str[i:i+len(s)], s, d):
		
			count+=1
	print count

def mismatch(a, b, c):
	count=0
	for i in range(len(b)):
		if a[i]!=b[i]:
			count=count+1
	if count<=c:
		return True 
	return False

position_in(s1,s2,c)