with open ('cyano.txt', "r") as input_1, open ('cyano2.txt',"r") as input_2:
	with open ('cyano_out.txt',"wb") as output, open ('cyano_out_2.txt',"wb") as otu:
		input2=input_2.readlines()
		for line in input_1:
			a=line.split(' ')
			if line.find('Cyano')==-1: output.write(line)
				for line2 in input_2:
					if line2.find(a[0])!=-1: otu.write(line2)
