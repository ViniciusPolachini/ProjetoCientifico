import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('./img2.png')
blur = cv.GaussianBlur(img,(5,5),0)

print(img)

#plt.subplot(121),plt.imshow(img),plt.title('Original')
#plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
#plt.xticks([]), plt.yticks([])
#plt.show()