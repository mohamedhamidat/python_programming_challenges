'''  8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 
'From ' like the following line:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

You will parse the From line using split() and print out the second word in the line 
(i.e. the entire address of the person who sent the message). Then print out a count at the end.

Hint: make sure not to include the lines that start with 'From:'.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt'''


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