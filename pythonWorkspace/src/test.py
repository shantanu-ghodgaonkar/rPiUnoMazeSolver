import cv2
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path

IMAGEPATH = Path.joinpath(Path(__file__).parent.resolve(
).parent.resolve(), 'img', 'maze_pic_1.jpg').__str__()

img = cv2.imread(IMAGEPATH, cv2.IMREAD_COLOR)  # Reading Image as BGR
b, g, r = cv2.split(img)  # Saved image is in RBG decomposing RGB
# Merging RGB as BGR and eliminating G and B components
img_rgb = cv2.merge((r, g, b))
img_1 = cv2.addWeighted(img_rgb, 10, img, 0, 0)  # Increasing contrast
gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)  # Converting to grayscale
gray = cv2.blur(gray, (9, 9))  # Adding Gaussian blur

detected_circles = cv2.HoughCircles(gray,
                                    cv2.HOUGH_GRADIENT, 1.8, 150, param1=20,
                                    param2=80, minRadius=15, maxRadius=40)

# Draw circles that are detected.
if detected_circles is not None:

    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # Draw the circumference of the circle.
        cv2.circle(img_rgb, (a, b), r, (0, 255, 0), 2)

        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(img_rgb, (a, b), 1, (255, 0, 0), 3)
plt.imshow(img_rgb)
plt.show()
