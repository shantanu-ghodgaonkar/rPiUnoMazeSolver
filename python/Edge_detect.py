import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path

imagePath = Path.joinpath(Path(__file__).parent.resolve(), 'img', 'maze_pic_1.jpg').__str__()
img = cv.imread(imagePath,cv.IMREAD_COLOR) #Reading Image as BGR

#h, w = img.shape[:2];

b,g,r=cv.split(img) #Saved image is in RBG decomposing RGB
img=cv.merge((r,g*0,b*0)) #Merging RGB as BGR and eliminating G and B components
img=cv.addWeighted(img,2,img,0,0) #Increasing contrast
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY) #Converting to grayscale
mask = cv.inRange(img, 100, 255);
_,img = cv.threshold(img,20,255,cv.THRESH_BINARY) #Thresholding image to convert to BW


kernel = np.ones((10,10),np.uint8) #Setting kernel for morphing
img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel) #Close morphing (Dilation followed by erosion eliminates black dots)

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(15,15)) #Setting kernel for morphing
#kernel = np.ones((10,10),np.uint8) #Setting kernel for morphing
img = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)  #Open morphing (Erosion followed by Dilation eliminates white dots)

# img = cv.Canny(img,0,255) #Canny edge detection


# plt.imshow(img,'gray')
plt.imshow(img)
plt.show()

