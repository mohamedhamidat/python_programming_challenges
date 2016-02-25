fname = raw_input("Enter file name: ")
[s1,s2]= open(fname).readlines()#.split('\r\n')
#s1,s2 = open(fname).read().split('\r\n') #or split('\r\n') be carful 
#the last line to
#s1,s2 = open(fname).readlines() may work but they have to be a sting i think 
count=0
for i in range (len(s1)-len(s2)):
    if s1[i:].startswith(s2):
		count+=1
print count 