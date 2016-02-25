fname = raw_input("Enter file name: ")
fh = open(fname)
counta=0
countc=0
countg=0
countt=0
for line in fh:
	line.upper()
	a=line.count('A')
	b=line.count('C')
	c=line.count('G')
	d=line.count('T')
print a,b,c,d
	