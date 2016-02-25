def del_line(filename):
    count=0
    fh=open(filename)
    for line in fh:
        line=line.rstrip()
        count=count+1
        if count%2=0: 
            print line