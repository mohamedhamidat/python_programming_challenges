#ros
def sq(a,b):
    a<1000
    b<1000
    x=(a**2)+(b**2)
    print x
    
def str(s,a,b,c,d):
    x= s[a:b+1]
    y=s[c:d+1]
    print x,y #to make use a coma     

def loo(a,b):
    sum=0
    for i in range(a,b):
        if i %2==1:
            sum= sum+i
    print sum       

    
def lines(fileinput):
    