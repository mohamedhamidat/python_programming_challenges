import itertools 

l=[]
for a in itertools.permutations('HHHXXXMMMIIINNNLLLPPPYYYCCC', 3):
   
    b=list(a)
    s = map(str, b)
    s = ''.join(s) 
    if s not in l:
   		l.append (s)   
for i in l: print i
