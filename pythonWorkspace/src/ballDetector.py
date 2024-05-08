import cv2
import numpy as np
from point import Point
# import matplotlib.pyplot as plt


class BallDetector:
    def __init__(self, img) -> None:
        self.img = img
        self.detected_circles = None
        self.start = Point()
        self.rad = 0.0

    def detectBall(self) -> bool:
        img_1 = cv2.addWeighted(self.img, 9, self.img, 0, 0)
        b_s, g_s, r_s = cv2.split(img_1)
        img_1 = cv2.merge((r_s*0, g_s, b_s))
        # self.show_img_2(img_1)
        gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)  # Converting to grayscale
        gray = cv2.blur(gray, (9, 9))  # Adding Gaussian blur

        self.detected_circles = cv2.HoughCircles(gray,
                                        cv2.HOUGH_GRADIENT, 1.9, 20, param1=60,
                                        param2=60, minRadius=12, maxRadius=30)
        if self.detected_circles is not None:
            return True
        else:
            return False

        # print("DEBUG POINT")

    def drawCircles(self):
        if self.detected_circles is not None:

            # Convert the circle parameters a, b and r to integers.
            self.detected_circles = np.uint16(np.around(self.detected_circles))

            for pt in self.detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]

                # Draw the circumference of the circle.
                cv2.circle(self.img, (a, b), r, (0, 255, 0), 2)

                # Draw a small circle (of radius 1) to show the center.
                cv2.circle(self.img, (a, b), 1, (255, 0, 0), 3)

    def fillCircles(self) -> None:
        if self.detected_circles is not None:

            # Convert the circle parameters a, b and r to integers.
            self.detected_circles = np.uint16(np.around(self.detected_circles))

            for pt in self.detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]+5
                self.start = Point(a, b)
                self.rad = r
                # Draw the circle.
                cv2.circle(self.img, (a, b), r, (255, 255, 255), -1)

    def show_img(self):
        temp_img = cv2.resize(self.img, None, fx=0.5,
                              fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imshow("Captured Image for Ball Detection", temp_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def get_image(self) -> np.ndarray:
        return self.img

    def get_start_point(self) -> Point:
        return self.start

    def get_radius(self) -> float:
        return self.rad

    def show_img_2(self, img):
        temp_img = cv2.resize(img, None, fx=0.5,
                              fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imshow("Captured Image for Ball Detection", temp_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
