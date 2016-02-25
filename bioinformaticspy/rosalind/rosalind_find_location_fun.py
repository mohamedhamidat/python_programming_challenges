fname = raw_input("Enter file name: ")
s1,s2 = open(fname).read().split('\n') #or split('\r\n') be carful 
#the last line to
#s1,s2 = open(fname).readlines() may work but they have to be a sting i think 
for i in range(len(s1)):
    if s1[i:].startswith(s2):
        print i+1,