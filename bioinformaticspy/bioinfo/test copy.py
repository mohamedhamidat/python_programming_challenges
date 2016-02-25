with open ('test.txt', "r") as input, open ('testout.txt',"wb") as out:
	for line in input:
		if line.startswith('>'):
			header=line
		else: 
			line=core.replace('\n','')
			line
			out.write(header+'\n'+line)
			