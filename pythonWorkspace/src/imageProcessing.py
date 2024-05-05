import cv2 as cv
import numpy as np
from point import Point
from pathlib import Path


class ImageProcessing:
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
        self.p_img = cv.cvtColor(self.img, cv.COLOR_BGR2HSV)
        b,g,r=cv.split(self.p_img) #Saved image is in RBG decomposing RGB
        self.p_img=cv.merge((r*0,g*1,b*0)) #Merging RGB as BGR and eliminating G and B components
        self.show_processed_img()
        self.p_img=cv.addWeighted(self.p_img,0.5,self.p_img,0.0,0) #Increasing contrast
        self.p_img=cv.cvtColor(self.p_img,cv.COLOR_BGR2GRAY) #Converting to grayscale
        mask = cv.inRange(self.p_img, 100, 255);
        _,self.p_img = cv.threshold(self.p_img,20,255,cv.THRESH_BINARY) #Thresholding image to convert to BW

        self.show_processed_img()

        kernel = np.ones((5,5),np.uint8) #Setting kernel for morphing
        self.p_img = cv.morphologyEx(self.p_img, cv.MORPH_CLOSE, kernel) #Close morphing (Dilation followed by erosion eliminates black dots)

        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5)) #Setting kernel for morphing
        #kernel = np.ones((10,10),np.uint8) #Setting kernel for morphing
        self.p_img = cv.morphologyEx(self.p_img, cv.MORPH_OPEN, kernel)  #Open morphing (Erosion followed by Dilation eliminates white dots)
        self.show_processed_img()

    def detect_edges(self) -> None:
        """_summary_
        """
        self.edge_img = cv.Canny(self.p_img, 0, 255)  # Canny edge detection

    def show_original_img(self) -> None:
        """_summary_
        """
        cv.namedWindow("Unprocessed Image", cv.WINDOW_NORMAL)
        cv.imshow("Unprocessed Image", self.img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def show_processed_img(self) -> None:
        """_summary_
        """
        cv.namedWindow("Processed Image", cv.WINDOW_NORMAL)
        cv.imshow("Processed Image", self.p_img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def resize_original_img(self, h: int, w: int) -> None:
        """_summary_

        Args:
            h (int): _description_
            w (int): _description_
        """
        self.img = cv.resize(self.img, (w, h))

    def scale_original_img(self, fx: float, fy: float) -> None:
        """_summary_

        Args:
            fx (float): _description_
            fy (float): _description_
        """
        self.img = cv.resize(self.img, None, fx=fx,
                             fy=fy, interpolation=cv.INTER_AREA)

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

    def set_original_img(self, img: np.ndarray) -> None:
        """_summary_

        Args:
            img (np.ndarray): _description_
        """
        self.img = img

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

    def irregular_quadrangle_crop_original_img(self, c1: Point, c2: Point, c3: Point, c4: Point):
        mask = np.zeros(self.img.shape, dtype=np.uint8)
        roi_corners = np.array(
            [[(c1.x, c1.y), (c2.x, c2.y), (c3.x, c3.y), (c4.x, c4.y)]], dtype=np.int32)
        # i.e. 3 or 4 depending on your image
        channel_count = self.img.shape[2]
        ignore_mask_color = (255,)*channel_count
        cv.fillPoly(mask, roi_corners, ignore_mask_color)
        self.img = cv.bitwise_and(self.img, mask)
        
