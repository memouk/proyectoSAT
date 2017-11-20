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
from skimage.filters import sobel
from skimage.morphology import square, disk, rectangle, dilation 


print("imagen original")

I = 255 - rgb2gray(imread('img/1.jpg').astype('uint8'))
imshow(I, cmap='gray')
show()

print("imagen recortada")

F = I[1500:3000, 1450:1800]
imshow(F, cmap='gray')
show()

print("imagen recortada binarizada")

borde2 = sobel(F,mask=None)
Z=borde2>0.1
imshow(Z,cmap='gray')
show()

plt.hist(borde2.ravel(), 256, [0, 1])
plt.show()

selSquare = square(3)
selDisk = disk(2)
selRectangle = rectangle(2, 3)

IDilationSquare = dilation(Z, selem=selSquare)
imshow(IDilationSquare, cmap='gray')
show()
IDilationDisk = dilation(Z, selem=selDisk)
imshow(IDilationDisk, cmap='gray')
show()
IDilationRectangle = dilation(Z, selem=selRectangle)
imshow(IDilationRectangle, cmap='gray')
show()


