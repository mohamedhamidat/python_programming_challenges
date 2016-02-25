fname = raw_input("Enter file name: ")
[s1,s2]= open(fname).readlines()#.split('\r\n')
for i in range(len(s1)):
	if s1[i:].startswith(s2):
		print i+1,