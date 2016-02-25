import itertools 
n=5
count=0
for a in itertools.permutations(range(1, n+1)):
    count+=1
    b=list(a)
    s = map(str, b)
    s = ' '.join(s) 
    
    print s
print count 