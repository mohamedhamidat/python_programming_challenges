import fileinput
from glob import glob 
fnames=glob('*.txt')
for line in fileinput.input(fnames,'r+'): 
	a=line.split(",")
	b=','.join(a[6:-3])
	print b

