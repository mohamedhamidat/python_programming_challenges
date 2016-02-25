def findpos(seq, pat):
    matches = []
    current_match = seq.find(pat)
    while current_match != -1:
        matches.append(current_match)
        current_match =seq.find(pat, current_match+1)
    print matches


def cutposigene(seq, numb):
    for i in range (0,len(seq),numb):
        primer=seq [i:i+numb]
        print primer
        
        if len(primer) = numb:
            matches = []
            current_match = seq.find(primer)
            
            while current_match != -1:
                matches.append(current_match)
                current_match =seq.find(primer, current_match+1)
            print matches
        else: 
            print 'small primer'
        
        
        
def positiongenome(genome, seq, numb):
    for i in range (0,len(seq),numb):
        primer=seq [i:i+numb]
        print primer
        
        matches = []
        current_match = genome.find(primer)
             
        while current_match != -1:
            matches.append(current_match)
            current_match =genome.find(primer, current_match+1)
        print matches