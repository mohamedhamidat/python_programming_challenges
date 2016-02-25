import numpy as np
from PIL import Image
import time 

def threshold (imageArray):
	balanceAr=[]
	newAr=imageArray
	for row in imageArray:
		print row
		for pix in row:
			print pix[0] 
#

i= Image.open('images/numbers/0.1.png')
iar=np.asarray(i)

i2= Image.open('images/numbers/y0.5.png')
iar2=np.asarray(i2)

i3= Image.open('images/numbers/y0.4.png')
iar3=np.asarray(i)

threshold(iar)

