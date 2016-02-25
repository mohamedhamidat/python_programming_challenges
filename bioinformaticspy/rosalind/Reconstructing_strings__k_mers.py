fname = raw_input("Enter file name: ")
#s1,s2]= open(fname).readlines()#.split('\r\n')
[k, p]= open(fname).read().split('\n')
#k,l,t=s2.split()
#with open(fname) as input_data:
#	p, [k] = [line.strip() if index == 0 else map(int, line.strip().split()) for index, line in enumerate(input_data.readlines())]
k=int(k)
positions = {}
def positionskmers(p, k):    
    for i in xrange(len(p)-k+1):
        positions[p[i:i+k]] = positions.get(p[i:i+k], []) + [i]
positionskmers(p, k)

for key in sorted(positions):
    print key


#with open(fname[:-3]+'output.txt', 'w') as output_data:
#	output_data.write()