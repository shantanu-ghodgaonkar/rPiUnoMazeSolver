import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_og = cv.imread('capture1.jpg', cv.IMREAD_COLOR)  # Reading Image as BGR
# Increasing contrast for ball detection

b, g, r = cv.split(img_og)  # Saved image is in RBG decomposing RGB
img = cv.merge((r, g, b))  # Merging RGB as BGR

# Removing glare by masking near white with black
lo = np.array([50, 45, 45])
hi = np.array([130, 255, 255])
mask = cv.inRange(img, lo, hi)
img[mask > 0] = (0, 0, 0)
# plt.imshow(img)
# plt.show()

# Thresholding on red scale
lo = np.array([0, 0, 0])
hi = np.array([70, 255, 255])
mask = cv.inRange(img, lo, hi)
img[mask > 0] = (0, 0, 0)

# plt.imshow(img)
# plt.show()


# Thresholding on red scale
b, g, r = cv.split(img)
lo = np.array([82, 0, 0])
hi = np.array([255, 30, 30])
mask = cv.inRange(img, lo, hi)
img[mask > 0] = (255, 0, 0)


b, g, r = cv.split(img)  # Saved image is in RBG decomposing RGB
# Merging RGB as BGR and eliminating G and B components
img = cv.merge((b, r*0, g*0))


img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Converting to grayscale
# plt.imshow(img)
# plt.show()

# Thresholding image to convert to BW
_, img = cv.threshold(img, 12, 255, cv.THRESH_BINARY)
# plt.imshow(img,'gray')
# plt.show()





kernel = np.ones((3, 3), np.uint8)  # Setting kernel for morphing
# Close morphing (Dilation followed by erosion eliminates black dots)
img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel, iterations=5)
# Open morphing (Erosion followed by Dilation eliminates white dots)
img = cv.morphologyEx(img, cv.MORPH_OPEN, kernel, iterations=5)
plt.imshow(img, 'gray')  # Image before resize
plt.show()
img = cv.resize(img, (300, 300))  # resizing image
# Thresholding image to convert to BW
_, img = cv.threshold(img, 12, 255, cv.THRESH_BINARY)
kernel = np.ones((3, 3), np.uint8)  # Setting kernel for morphing
# Open morphing (Erosion followed by Dilation eliminates white dots)
img = cv.morphologyEx(img, cv.MORPH_OPEN, kernel, iterations=2)
plt.imshow(img, 'gray')
plt.show()



# Shape detect
img_1 = cv.addWeighted(img_og, 9, img_og, 0, 0)
b_s, g_s, r_s = cv.split(img_1)
img_1 = cv.merge((r_s*0, g_s, b_s))

gray = cv.cvtColor(img_1, cv.COLOR_BGR2GRAY)  # Converting to grayscale
gray = cv.blur(gray, (9, 9))  # Adding Gaussian blur

detected_circles = cv.HoughCircles(gray,
                                   cv.HOUGH_GRADIENT, 1.9, 20, param1=60,
                                   param2=60, minRadius=12, maxRadius=40)

if detected_circles is not None:

    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a1, b1, r1 = pt[0], pt[1], pt[2]

        # Masking circle white
        # Circle centre coordinates a1,b1
        cv.circle(img, (a1, b1), r1, (255, 255, 255), -1)

# Shape detect End