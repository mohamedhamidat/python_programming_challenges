fname = raw_input("Enter file name: ")
x,y,z= open(fname).read().split('\n')

z=int(z)



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

position_in(y,x,z)