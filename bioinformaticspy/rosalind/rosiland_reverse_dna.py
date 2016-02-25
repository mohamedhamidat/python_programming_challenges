fname = raw_input("Enter file name: ")
fh = open(fname)
basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
for line in fh:
	line=[basecomplement[i] for i in line.strip()]
	line.reverse()	
	a=''.join(line)
	
print a
