def grp(filename):
    mf=open(filenam).readlines()
    
    for line in mf:
        print line
        if not line.startswith('>'):
            line=line.split()
            line=line.extend(line)
            return line 
def grp(filename):
    mf=open(filename).readlines()
    lines=[]
    for line in mf:
        
        if not line.startswith('>'): 
            line=line.split()
            line=lines.extend(line)
            line=''.join(lines)
    print line      
def grp(filename):
    mf=open(filename).readlines()
    lines=[]
    for line in mf:
        if line.startswith('>'):
           print line 
    for line in mf:
            line=line.split()
            line=lines.extend(line)
            line=''.join(lines)
            if '>' in line : break 
            print line 
def readFastaEntry( f ):
    name = ""
    while True:
        line = name or f.readline()
        if not line:
            break
        seq = []
        while True:
            name = f.readline()
            if not name or name.startswith(">"):
                break
            else:
                seq.append(name)
        yield (line, "".join(seq)) 
try:
    with open(outFile,"w") as newFasta:
    for fasta in sequences:
        try:
                header, sequence = fasta.split("\n", 1) # Split each fasta into header and sequence.
            except ValueError:
                    print fasta
            header = ">" + header + "\n" # Replace ">" lost in ">" split, Replace "\n" lost in split directly above.
            sequence = sequence.replace("\n","") + "\n" # Replace newlines in sequence, remember to add one to the end.
            newFasta.write(header + sequence)
        newFasta.close()
except IOError:
    print "Failed to open " + inFile
    exit(1)
 
print ">> Done!"         
