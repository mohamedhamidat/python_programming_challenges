def computepay(h,rate):
  
   if h <=40:
        pay= h*rate
   else:
    	pay=rate*40+(rate*1.5*(h-40))
   return pay

try:
    inp=raw_input ("Enter Hours:") 
    hours=float(inp)
    inp=raw_input ("Enter Rate:") 
    rate=float(inp)
#print rate, hours
   	
except:
    print "Error, please enter numeric input"
    quit()
pay= computepay(hours,rate)
print pay