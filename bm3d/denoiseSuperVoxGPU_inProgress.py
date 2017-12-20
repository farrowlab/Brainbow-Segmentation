import os
import numpy as np
import cv2
from tifffile import imsave, imread



def waterShed(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

	kernel = np.ones((3,3),np.uint8)
	opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN, kernel, iterations=2)

	sure_bg = cv2.dilate(opening, kernel, iterations=3)

	dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2,5)
	ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(),255,0)

	sure_fg = np.uint8(sure_fg)
	unknown = cv2.subtract(sure_bg, sure_fg)

	ret, markers = cv2.connectedComponents(sure_fg)

	markers = markers + 1

	markers[unknown==255] = 0

	markers = cv2.watershed(img,markers)
	return markers

im = imread('/home/quan/Desktop/brainbowPython/data/00656_5R_C01-processed.tif')
z,y,x,c = im.shape
bbVol = im
#gradAmplitude = np.zeros((z, y, x))
#tmpbb = np.zeros((z+1,y,x,c))
#end = z
#print end
#tmpbb[0:end,:,:,:] = bbVol
#tmpbb[1:end+1,:,:,:] = bbVol
#gradAmplitude = max(gradAmplitude,np.squeeze(max(abs(np.diff(tmpbb,1,1)),[],4)) );       
#tmpbb = zeros((z,y+1,x,c));
#end = y 
#tmpbb[:,0:end-1,:,:] = bbVol; 
#tmpbb[:,1:end,:,:] = bbVol;
#gradAmplitude = max(gradAmplitude, np.squeeze(max(abs(np.diff(tmpbb,1,2)),[],4)) );
#tmpbb = zeros(z,y,x+1,c);
#end = x
#tmpbb[:,:,0:end-1,:] = bbVol; 
#tmpbb[:,:,1:end,:] = bbVol;
#gradAmplitude = max(gradAmplitude, np.squeeze(max(abs(np.diff(tmpbb,1,3)),[],4)) );

imgdest = np.zeros((z,y,x,c))

print "Detecting and Removing the Background"
for i in range(0,z):
	temp = im[i,:,:,:]
	imsave('temp.tif', temp)
	os.system("./bm3d temp.tif tempout.tif 50 color twostep quite")
	tempim = imread('tempout.tif')
#	markers = waterShed(tempim)
#	tempim[markers==-1] = [255,0,0]
	if i == 0:
		imsave('656_5R_dn_50_watershed_02.tif',tempim)
	else:
		imsave('656_5R_dn_50_watershed_02.tif', tempim,append='True')


#imsave('final.tif',imgdest)
