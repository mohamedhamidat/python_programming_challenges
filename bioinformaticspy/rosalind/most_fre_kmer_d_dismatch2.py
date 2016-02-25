fname = raw_input("Enter file name: ")
#x,y,z= open(fname).read().split('\n')
with open(fname) as input_data:
	genome, [k,d] = [line.strip() if index == 0 else map(int, line.strip().split()) for index, line in enumerate(input_data.readlines())]

import itertools
def ball_edit_distance_d(pattern, d):
    output = []
    indexes = range(len(pattern))
    for i in itertools.combinations(indexes,d):
        for j in itertools.product("ACGT", repeat=d):
            s = list(pattern)
            for k in range(d):
                s[i[k]] = j[k] 
            output = output + ["".join(s)]
            # print i, j, "resulta:", "".join(s)
    # This generating function is not very efficient. In particular it over generates several patterns.
    # That's the reason for the "set" in the next line.
    return list(set(output))

def countaproxkmers(genome, k, d):
    kmers = {}
    balls = {}
    for i in range(len(genome)-k):
        # print i, "out of", len(genome)-k, "-",
        l = balls.get(genome[i:i+k], ball_edit_distance_d(genome[i:i+k],d))
        for kmer in l:
            kmers[kmer] = kmers.get(kmer,0)+1
    return kmers

def mostfrequentapproxkmers(genome,k,d):
    # print "Starting counting"
    kmers = countaproxkmers(genome, k, d)
    # print "Done counting"
    top = max(kmers.values())
    m = [k for k,v in kmers.items() if v==top]
    print "Result:"
    for i in m:
        print i,

mostfrequentapproxkmers(genome,k,d)