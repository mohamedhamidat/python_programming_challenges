fname = raw_input("Enter file name: ")
from difflib import Differ
#[a,b]= open(fname).readlines().split('\n')
a,b = open(fname).read().split('\n')
#	line=line.split()
#a=list(a)
#b=list(b)
count=0
for i in range(len(a)):
	if a[i]!=b[i]:
		count=count+1
print count 