import cv2
import numpy as np
# import matplotlib.pyplot as plt


class BallDetector:
    def __init__(self, img) -> None:
        self.img = img

    def show_img(self):
        cv2.imshow("Captured Image for Ball Detection", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()