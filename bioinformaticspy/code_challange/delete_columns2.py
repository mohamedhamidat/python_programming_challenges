import csv 
import glob
import os
#import sys
mypath=r'output'# name of output folder
if not os.path.exists(mypath): os.makedirs(mypath)
#	os.chdir(mypath)
for filename in glob.glob('*.csv'):
	with open (filename, 'rU') as input, open(os.path.join(mypath, filename), 'w') as out: 
		for line in input:
			a=line.split(",")
			out.write( ','.join(a[6:-3])+'\n')## change number here
