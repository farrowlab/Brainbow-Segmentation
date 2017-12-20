import numpy as np
from tifffile import imsave, imread
#from scipy import ndimage as ndi
img = imread('/home/quan/Desktop/brainbowPython/bm3d-gpu/656_5R_dn_500.tif')

#z,y,x,c =  img.shape

print img.shape


#from skimage.morphology import watershed
#from skimage.feature import peak_local_max
import cv2


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

print markers.shape
img[markers == -1] = [255,0,0]
imsave('testvox.tif',img)
#distance = ndi.distance_transform_edt(image)
#local_maxi = peak_local_max(distance, indices=False, footprint=np.ones((3,3)), labels=image)

#markers = ndi.label(local_maxi)[0]
#labels = watershed(-distance, markers, mask=image)



