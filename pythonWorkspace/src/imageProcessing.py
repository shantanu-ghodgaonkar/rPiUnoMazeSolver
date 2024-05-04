import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


class Image_processing:
    """_summary_
    """

    def __init__(self, imgPath: str) -> None:
        """_summary_

        Args:
            imgPath (str): _description_
        """
        self.img = cv.imread(imgPath, cv.IMREAD_COLOR)  # Reading Image as BGR
        self.p_img = np.zeros((300, 300, 3), dtype=np.uint8)
        self.edge_img = np.zeros((300, 300, 3), dtype=np.uint8)

    def process_image(self) -> None:
        """_summary_
        """
        b, g, r = cv.split(self.img)  # Saved image is in RBG decomposing RGB
        # type: ignore #Merging RGB as BGR and eliminating G and B components
        self.p_img = cv.merge((r, g*0, b*0))
        self.p_img = cv.addWeighted(
            self.p_img, 2, self.p_img, 0, 0)  # Increasing contrast
        # Converting to grayscale
        self.p_img = cv.cvtColor(self.p_img, cv.COLOR_BGR2GRAY)
        mask = cv.inRange(self.p_img, 100, 255)  # type: ignore
        # Thresholding image to convert to BW
        _, self.p_img = cv.threshold(self.p_img, 20, 255, cv.THRESH_BINARY)

        kernel = np.ones((10, 10), np.uint8)  # Setting kernel for morphing
        # Close morphing (Dilation followed by erosion eliminates black dots)
        self.p_img = cv.morphologyEx(self.p_img, cv.MORPH_CLOSE, kernel)

        kernel = cv.getStructuringElement(
            cv.MORPH_ELLIPSE, (15, 15))  # Setting kernel for morphing
        # kernel = np.ones((10,10),np.uint8) #Setting kernel for morphing
        # Open morphing (Erosion followed by Dilation eliminates white dots)
        self.p_img = cv.morphologyEx(self.p_img, cv.MORPH_OPEN, kernel)
        # print("DEBUG POINT")

    def detect_edges(self) -> None:
        """_summary_
        """
        self.edge_img = cv.Canny(self.p_img, 0, 255)  # Canny edge detection

    def show_original_img(self) -> None:
        """_summary_
        """
        plt.imshow(self.img)
        plt.show()

    def show_processed_img(self) -> None:
        """_summary_
        """
        plt.imshow(self.p_img)
        plt.show()

    def resize_original_img(self, h: int, w: int) -> None:
        """_summary_

        Args:
            h (int): _description_
            w (int): _description_
        """
        self.img = cv.resize(self.img, (w, h))

    def resize_processed_img(self, h: int, w: int) -> None:
        """_summary_

        Args:
            h (int): _description_
            w (int): _description_
        """
        self.img = cv.resize(self.img, (w, h))

    def crop_original_img(self, h0: int, h1: int, w0: int, w1: int) -> None:
        """_summary_

        Args:
            h0 (int): _description_
            h1 (int): _description_
            w0 (int): _description_
            w1 (int): _description_
        """
        self.img = self.img[h0:h1, w0:w1]

    def crop_processed_img(self, h0: int, h1: int, w0: int, w1: int) -> None:
        """_summary_

        Args:
            h0 (int): _description_
            h1 (int): _description_
            w0 (int): _description_
            w1 (int): _description_
        """
        self.p_img = self.p_img[h0:h1, w0:w1]

    def rotate_original_img(self, angle: int) -> None:
        """_summary_

        Args:
            angle (int): _description_
        """
        rows, cols, _ = self.img.shape
        M = cv.getRotationMatrix2D((((cols-1)/2.0), ((rows-1)/2.0)), angle, 1)
        self.img = cv.warpAffine(self.img, M, (cols, rows))

    def rotate_processed_img(self, angle: int) -> None:
        """_summary_

        Args:
            angle (int): _description_
        """
        rows, cols = self.p_img.shape
        M = cv.getRotationMatrix2D((((cols-1)/2.0), ((rows-1)/2.0)), angle, 1)
        self.p_img = cv.warpAffine(self.p_img, M, (cols, rows))

    def get_original_img_array(self) -> np.ndarray:
        """_summary_

        Returns:
            np.ndarray: _description_
        """
        return self.img

    def get_processed_img_array(self) -> np.ndarray:
        """_summary_

        Returns:
            np.ndarray: _description_
        """
        return self.p_img
