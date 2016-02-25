def fun(inFile):
    import sys
    import re 
    with open(inFile,"r") as newFile:
                sequences = newFile.read()
                sequences = re.split("^>", sequences, flags=re.MULTILINE) # Only splits string at the start of a line.              
                del sequences[0] # The first fasta in the file is split into an empty empty element and and the first fasta              
                newFile.close()
    
    Outfile='Output.'+inFile     
    with open(Outfile,"w") as newFasta:
            for fasta in sequences:
                try:
                    header, sequence = fasta.split("\n", 1) # Split each fasta into header and sequence. 
                except ValueError:
                        print fasta
                header = ">" + header + "\n" # Replace ">" lost in ">" split, Replace "\n" lost in split directly above.
                sequence = sequence.replace("\n","") + "\n" # Replace newlines in sequence, remember to add one to the end.
                newFasta.write(header + sequence)				# sequence = sequence.replace("\r\n","") or \r
            newFasta.close()
 
    print ">> Done! : "   

fun("s.txt")