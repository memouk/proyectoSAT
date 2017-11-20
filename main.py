#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:51:34 2017

@author: xxx
"""


from	 scipy.ndimage	import	imread
from	 matplotlib.pyplot	import	imshow,	show, imsave
from	 skimage.filters.rank	 import	median
from skimage.filters.rank import maximum,minimum
from	skimage.color	import	rgb2yiq,	rgb2hsv,	rgb2xyz,	rgb2lab,	rgb2ycbcr	,convert_colorspace
from skimage.color import rgb2gray	
from skimage.exposure import adjust_gamma
from skimage.exposure import equalize_hist
import matplotlib.pyplot as plt
import numpy as np
from skimage.morphology import square
from skimage.filters import gaussian
import skimage.filters
import matplotlib.pyplot as plt
from skimage.filters.rank import mean
from skimage.filters import sobel, sobel_h, sobel_v
from skimage.feature import canny


s=square(11)
img1=rgb2gray(imread('img/1.jpg'))
#mediaa=mean(img1[:,:,0],s)

#test=mediaa-img1[:,:,1]



print("sobel")
borde2 = skimage.filters.sobel(rgb2gray(img1),mask=None)
imshow(borde2,cmap='gray')
show()




#print('sobel')
#
#B1 = sobel_h(img1)
#B2 = sobel_v(img1)
#BW = np.maximum(B1, B2) > 0.09
#
#imshow(BW,cmap='gray')
#show()



#plt.hist(img1.ravel(), 256, [0, 1])
#plt.show()
#
#plt.hist(test2.ravel(), 256, [0, 1])
#plt.show()
#plt.hist(test3.ravel(), 256, [0, 1])
#plt.show()

#imshow(img1)
#show()
#imshow(test2,cmap='gray')
#show()
#imshow(img1,cmap='gray')
#show()
#imshow(BW,cmap='gray')
#show()

