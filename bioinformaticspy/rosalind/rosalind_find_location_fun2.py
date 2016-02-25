fname = raw_input("Enter file name: ")
#[s1,s2]= open(fname).readlines()#.split('\r\n')
s1,s2 = open(fname).read().split('\n')
for i in range(len(s2)):
	if s2[i:].startswith(s1):
		print i, #i or i+1 depends on position they ask for 