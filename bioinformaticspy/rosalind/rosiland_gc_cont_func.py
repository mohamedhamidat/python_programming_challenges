fname = raw_input("Enter file name: ")
import sys
import re 
with open(fname) as newFile:
    seq = newFile.read()
    seq = re.split("^>", seq, flags=re.MULTILINE)
    del seq[0]
    for s in seq:
 #   	sequence = s.split("\n") # Split each fasta into header and sequence.
  #  	print sequence
	   	sequence = s.replace("\n","") 
	   	a=float((sequence.count('G') + sequence.count('C')) / (sequence.count('A')+ sequence.count('C')+sequence.count('G')+sequence.count('T')))

'''count=dict()
for word in words:
    count[word]=count.get(word,0)+1

bigcount=None
bigword=None
for word,counts in count.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=counts
print bigword,bigcount
print seq
#	return (seq.count('G') + seq.count('C')) / len(seq)'''