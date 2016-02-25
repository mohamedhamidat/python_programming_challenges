def fun(inFile):
	import sys
	basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	with open(inFile) as fh:
		for word in fh:
			word=[basecomplement[i] for i in word.strip()]
			word.reverse()	
			a=''.join(word)
	Outfile=inFile[:-4]+'.output.txt' 
	with open(Outfile,"w") as newFasta:
		newFasta.write(a)
		newFasta.close()
	print "Done !"

fun('dataset_3_2.txt')
