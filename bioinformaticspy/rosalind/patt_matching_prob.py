fname = raw_input("Enter file name: ")
x,y,z= open(fname).read().split('\n')

#	p, [k, l, t] = [line.strip() if index == 0 else map(int, line.strip().split()) for index, line in enumerate(input_data.readlines())]

z=int(z)	
def position_in (s,str,d):
	pos=[]
	for i in range (len(str)-len(s)+1):
		if mismatch(str[i:i+len(s)], s, d):
			pos.append(i)
	for n in pos: print n, 

def mismatch(a, b, c):
	count=0
	for i in range(len(b)):
		if a[i]!=b[i]:
			count=count+1
	if count<=c:
		return True 
	return False
	


position_in(x,y,z)