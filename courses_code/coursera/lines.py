# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count=0
value=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line=line.rstrip()
    num=line.find(':')
    posi=line[num+1:]
    val=float(line[num+1:])
    count=count+1
    value=value+val
print "Average spam confidence:", value/count


text = "X-DSPAM-Confidence:    0.8475"
num=text.find(':')
posi=text[num+1:]
value=float(text[num+1:])
print value
count=0
def del_line(filename):
    count=0
    fh=open(filename)
    count
    for line in fh:
        if count%2 != 0: 
            del line [:-count]
    print lines 