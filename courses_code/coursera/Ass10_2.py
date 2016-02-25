'''  10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour 
of the day for each of the messages. You can pull the hour out from the 'From ' 
line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, 
sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.'''


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
for line in handle:
    if not line.startswith('From '):continue
    else:
        line=line.split() 
        line=line[5]
        lst.append(line)
count=dict()
for word in lst:
    word=word.split(':')
    word=word[0]
    count[word]=count.get(word,0)+1
lt=list()
for key, val in count.items():
    lt.append((key,val))
lt.sort()
for key, val in lt:
    print key, val