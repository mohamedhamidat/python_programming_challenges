fname = raw_input("Enter file name: ")
#[s1,s2]= open(fname).readlines()#.split('\r\n')
#,s2 = open(fname).read().split('\n')
#k,l,t=s2.split()
with open(fname) as input_data:
	p, [k, l, t] = [line.strip() if index == 0 else map(int, line.strip().split()) for index, line in enumerate(input_data.readlines())]

def positionskmers(p, k):
    positions = {}
    for i in range(len(p)-k):
        positions[p[i:i+k]] = positions.get(p[i:i+k], []) + [i]
    return positions

def isthereaclump(p, k, t, l):
    for i in range(len(p)-(t-1)):
        if p[i+(t-1)] + (k-1) - p[i] <= l-1:
            return True
    return False
  
def clumpfinder(p, k, t, l):
    pos = positionskmers(p, k)
    clumps = {key:value for key,value in pos.items() if len(value)>=t and isthereaclump(value, k, t, l)}
    for i in clumps.keys():
    	print i, 

clumpfinder(p,k, t, l)

#with open(fname[:-3]+'output.txt', 'w') as output_data:
	#output_data.write(clumpfinder(p, k, t, l))