s1='GACCATCAAAACTGATAAACTACTTAAAAATCAGT'
s2= 'AAA'
 
count=0
for i in range (len(s1)-len(s2)):
    if s1[i:].startswith(s2):
		count+=1
print count 