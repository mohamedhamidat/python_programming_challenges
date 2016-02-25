def find_location(t,s):
        lst=list()
        for i in range(0,len(s)):
                if s[i:].find(t)!=-1:
                        p=s[i:].find(t)+(i+1)
                        if p not in lst:
                                lst.append(p)                          
        str1 = ' '.join(str(e) for e in lst)
        print str1
