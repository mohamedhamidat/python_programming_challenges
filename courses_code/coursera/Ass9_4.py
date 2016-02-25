'''  9.4 Write a program to read through the mbox-short.txt and figure out who has the sent 
the greatest number of mail messages. The program looks for 'From ' lines and takes 
the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of 
times they appear in the file. After the dictionary is produced, the program reads through 
the dictionary using a maximum loop to find the most prolific committer.'''


fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
lst=list()
for line in fh:
    if not line.startswith('From:'):continue
    else:
        line=line.split()
        line=line[1]
        lst.append(line)
count=dict()
for word in lst:
    count[word]=count.get(word,0)+1
bigcount=None
bigword=None
for word,counts in count.items():
    if bigcount is None or counts>bigcount:
        bigword=word
        bigcount=counts
print bigword,bigcount