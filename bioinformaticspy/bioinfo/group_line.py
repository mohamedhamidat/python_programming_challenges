def fun(inFile):
    import sys
    import re 
    try:
        with open(inFile,"r") as newFile:
                sequences = newFile.read()
                sequences = re.split("^>", sequences, flags=re.MULTILINE) # Only splits string at the start of a line.fun('sequence.txt')
                del sequences[0] # The first fasta in the file is split into an empty empty element and and the first fasta
                
# Del removes this empty element.
                newFile.close()
    except IOError:
            print "Failed to open " + inFile
            exit(1)
 

    print ">> Converting FASTA file from multiline to single line and writing to file." 
    Outfile='Output.'+inFile  
    try:
        with open(Outfile,"w") as newFasta:
            for fasta in sequences:
                try:
                    header, sequence = fasta.split("\r\n", 1) # Split each fasta into header and sequence.
                except ValueError:
                        print fasta
                header = ">" + header + "\n" # Replace ">" lost in ">" split, Replace "\n" lost in split directly above.
                sequence = sequence.replace("\r\n","") + "\n" # Replace newlines in sequence, remember to add one to the end.
                newFasta.write(header + sequence)
            newFasta.close()
    except IOError:
        print "Failed to open " + inFile
        exit(1)
 
    print ">> Done!"         

