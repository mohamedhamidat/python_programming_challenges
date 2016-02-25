with open ("seqfasta.txt", 'rU') as input, open ("seqfastaout.txt", 'w') as output:
	line= input.readlines()
	for i in range (0, len(line)):
		if line[i].startswith(">"):
			if line[i].find("0")==-1: ## if 0 not in line, then takt it please 
				output.write(line[i]+line[i+1])	
		else: continue		
	print "done !!" 
