fname = raw_input("Enter file name: ")
fh = open(fname)
lst=list()
for line in fh:
        line=line.split()
        lst.append(line)
print lst