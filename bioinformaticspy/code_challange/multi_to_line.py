myfile=open("s.txt","r")
raw= myfile.read()

d={}
for seqblock in raw.split(">")[1:]:
	parts = seqblock.split("\n") # or ("\r\n")
	fasta = parts[0]
	seq = ''.join(parts[1:])
#	print ">"+fasta+"\n"+seq
	gc = 100 * ( seq.count("G") + seq.count("C") ) / float(len(seq))
	d[gc] = fasta

print d[max(d)], max(d)