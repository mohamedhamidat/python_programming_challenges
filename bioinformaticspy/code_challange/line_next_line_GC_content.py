def countgc(seq):
	maxgc={}
	gc= float(seq.count("g"))/seq.count("c")
	return "GC conetnent is: " + str(gc)

def maxgc(seq):
	maxgc={}
	gc= float(seq.count("g"))/seq.count("c")
	return "GC conetnent is: " + str(gc)
	 	 

with open ("seqfasta.txt", 'rU') as input, open ("seqfastaout.txt", 'w') as output:
	line= input.readlines()
	for i in range (0, len(line)):
		if line[i].startswith(">"):
			output.write(line[i]+line[i+1]+countgc(line[i+1])+"\n")
		else: continue		
	print "done !!" 

# I can add function that calculate g/c % 
