fname = raw_input("Enter file name: ")
#[s1,s2]= open(fname).readlines()#.split('\r\n')
p,s2 = open(fname).read().split('\n')
[k,l,t]=s2.split()
#print k, l, t 

'''first step : find position'''

def position_kimer(p, k):
	position = dict()
	for i in range(len(p)-int(k)):
		position[p[i:i+k]]=position.get(p[i:i+k],[])+[i]
    	return position 

'''first step : find the frequent word '''

def isthereaclump(p, k, t, l):
    for i in range(len(p)-(t-1)):
        if p[i+(t-1)] + (k-1) - p[i] <= l-1:
            return True
    return False
    

def clumpfinder(p, k, t, l):
    pos = position_kimer(p, k)
    clumps = {key:value for key,value in pos.items() if len(value)>=t and isthereaclump(value, k, t, l)}
    print clumps.keys()

clumpfinder(p,k, t, l)