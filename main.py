#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:51:34 2017

@author: xxx
"""


import matplotlib.pyplot as plt
from scipy.ndimage import imread
from skimage.color import rgb2gray
from	 matplotlib.pyplot	import	imshow,	show
#from balu.FeatureExtraction import Bfx_basicgeo
from skimage.filters import sobel,sobel_v, sobel_h
from skimage.feature import canny
from skimage.morphology import square, disk, rectangle, dilation 
from skimage.morphology import erosion, opening, closing
from skimage.morphology import white_tophat, black_tophat, skeletonize
from skimage.measure import label
from scipy import ndimage
import numpy as np
from skimage.filters.rank import mean
from skimage.filters import gaussian

print("imagen original")

I = 255 - rgb2gray(imread('img/1.jpg').astype('uint8'))
imshow(I, cmap='gray')
show()

print("imagen recortada")

F = I[1525:3000, 1450:1800]
imshow(F, cmap='gray')
show()

print("imagen recortada binarizada")

borde2 = sobel(F,mask=None)
Z=borde2>0.1
imshow(Z,cmap='gray')
show()

plt.hist(borde2.ravel(), 256, [0, 1])
plt.show()

selSquare = square(14)
selDisk = disk(12)
selRectangle = rectangle(6, 20)

IDilationSquare = dilation(Z, selem=selSquare)
#imshow(IDilationSquare, cmap='gray')
#show()
IDilationDisk = dilation(Z, selem=selDisk)
#imshow(IDilationDisk, cmap='gray')
#show()
IDilationRectangle = dilation(Z, selem=selRectangle)
imshow(IDilationRectangle, cmap='gray')
show()

IClosingSquare = closing(IDilationDisk, selem=selSquare)
#imshow(IClosingSquare, cmap='gray')
#show()
IClosingDisk = closing(IDilationDisk, selem=selDisk)
#imshow(IClosingDisk, cmap='gray')
#show()
IClosingRectangle = closing(IDilationDisk, selem=selRectangle)
imshow(IClosingRectangle, cmap='gray')
show()
I3 = gaussian(IClosingRectangle, 3)


borde3 = sobel(I3,mask=None)
imshow(borde3,cmap='gray')
show()



print(np.argmin(borde3))
print(np.argmax(borde3))
print(np.linalg.norm(np.argmin(borde3)-np.argmax(borde3)))
#h1 = square(3)
#for i in range(1,100):
#    I4 = mean(IDilationDisk, h1)




#ISkeletonize = skeletonize(IDilationRectangle)
#imshow(ISkeletonize, cmap='gray')
#show()
#ILabel = label(ISkeletonize)
#imshow(ILabel, cmap='gray')
#show()


#IErosionSquare = erosion(IDilationDisk, selem=selSquare)
#imshow(IErosionSquare, cmap='gray')
#show()
#IErosionDisk = erosion(IDilationDisk, selem=selDisk)
#imshow(IErosionDisk, cmap='gray')
#show()
#IErosionRectangle = erosion(IDilationDisk, selem=selRectangle)
#imshow(IErosionRectangle, cmap='gray')
#show()

#from skimage.filters.rank import mean
#import skimage.filters
#
#h = square(11)
#for i in range(1,50):
#    I2 = mean(IDilationDisk, h)
#
#print("sobel_con_Ruido_pero_filtro _media")
#borde2 = skimage.filters.sobel_h(I2,mask=None)
#imshow(borde2,cmap='gray')
#show()

#open_img = ndimage.binary_opening(IDilationDisk,structure=None, iterations=1000, output=None,origin=0)
## Elimina el pequeño agujero negro
#close_img = ndimage.binary_closing(IDilationDisk)
#
#imshow(open_img,cmap='gray')
#show()
#imshow(close_img,cmap='gray')
#show()
#xx=np.abs(close_img)
#imshow(xx,cmap='gray')
#show()