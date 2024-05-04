import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


class Image_processing:

    def __init__(self, imgPath: str) -> None:
        self.img = cv.imread(imgPath,cv.IMREAD_COLOR) #Reading Image as BGR
        self.p_img = np.zeros((300,300,3), dtype=np.uint8)
        self.edge_img = np.zeros((300,300,3), dtype=np.uint8)

    def process_image(self) -> None:
        b,g,r=cv.split(self.img) #Saved image is in RBG decomposing RGB
        self.p_img=cv.merge((r,g*0,b*0)) # type: ignore #Merging RGB as BGR and eliminating G and B components
        self.p_img=cv.addWeighted(self.p_img,2,self.p_img,0,0) #Increasing contrast
        self.p_img=cv.cvtColor(self.p_img,cv.COLOR_BGR2GRAY) #Converting to grayscale
        mask = cv.inRange(self.p_img, 100, 255) # type: ignore
        _,self.p_img = cv.threshold(self.p_img,20,255,cv.THRESH_BINARY) #Thresholding image to convert to BW
        
        kernel = np.ones((10,10),np.uint8) #Setting kernel for morphing
        self.p_img = cv.morphologyEx(self.p_img, cv.MORPH_CLOSE, kernel) #Close morphing (Dilation followed by erosion eliminates black dots)

        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(15,15)) #Setting kernel for morphing
        #kernel = np.ones((10,10),np.uint8) #Setting kernel for morphing
        self.p_img = cv.morphologyEx(self.p_img, cv.MORPH_OPEN, kernel)  #Open morphing (Erosion followed by Dilation eliminates white dots)
        # print("DEBUG POINT")
    
    def detect_edges(self) -> None:
        self.edge_img = cv.Canny(self.p_img,0,255) #Canny edge detection

    def show_original_img(self) -> None:
        plt.imshow(self.img)
        plt.show()

    def show_processed_img(self) -> None:
        plt.imshow(self.p_img)
        plt.show()

    def resize_original_img(self, h:int, w:int) -> None:
        self.img = cv.resize(self.img, (w, h))

    def resize_processed_img(self, h:int, w:int) -> None:
        self.img = cv.resize(self.img, (w, h))

    def crop_original_img(self, h0:int, h1:int, w0:int, w1:int) -> None:
        self.img = self.img[h0:h1, w0:w1]

    def crop_processed_img(self, h0:int, h1:int, w0:int, w1:int) -> None:
        self.p_img = self.p_img[h0:h1, w0:w1]

    def rotate_original_img(self, angle:int) -> None:
        rows, cols, _ = self.img.shape
        M = cv.getRotationMatrix2D((((cols-1)/2.0), ((rows-1)/2.0)), angle, 1)
        self.img = cv.warpAffine(self.img, M, (cols,rows))
    
    def rotate_processed_img(self, angle:int) -> None:
        rows, cols = self.p_img.shape
        M = cv.getRotationMatrix2D((((cols-1)/2.0), ((rows-1)/2.0)), angle, 1)
        self.p_img = cv.warpAffine(self.p_img, M, (cols,rows))

    def get_original_img_array(self) -> np.ndarray:
        return self.img
    
    def get_processed_img_array(self) -> np.ndarray:
        return self.p_img