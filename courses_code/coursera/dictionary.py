#dictionary 
name=raw_input("Enter file:")
handle=open(name,'r')
text=handle.read()
words=text.split()

count=dict()
for word in words:
    count[word]=count.get(word,0)+1

bigcount=None
bigword=None
for word,counts in count.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=counts
print bigword,bigcount

#worked exercise
