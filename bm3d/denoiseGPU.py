import os
import numpy as np

from tifffile import imsave, imread

im = imread('/home/quan/Desktop/brainbowPython/data/00617_1R.tif')
z,y,x,c = im.shape
imgdest = np.zeros((z,y,x,c))
for i in range(0,z):
	temp = im[i,:,:,:]
	imsave('temp.tif', temp)
	os.system("./bm3d temp.tif tempout.tif 1000 color twostep")
	tempim = imread('tempout.tif')
	
	if i == 0:
		imsave('617_1R_dn_1000.tif',tempim)
	else:
		imsave('617_1R_dn_1000.tif', tempim,append='True')

#imsave('final.tif',imgdest)
