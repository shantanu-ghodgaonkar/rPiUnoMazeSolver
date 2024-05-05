# import serial
# from time import sleep
from pathlib import Path
# from piCameraCtrl import Camera
from imageProcessing import ImageProcessing
from ballDetector import BallDetector
from time import time
from point import Point
from mazeSolverBFS import MazeSolverBFS


ARDUINO = '/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_24238313635351F0A162-if00'
BAUDRATE = 115200
IMAGEPATH = Path.joinpath(Path(__file__).parent.resolve(
).parent.resolve(), 'img', 't.jpg').__str__()
IMAGESCALEFACTOR = 0.25


if __name__ == "__main__":
    startTime = time()
    imgProc = ImageProcessing(IMAGEPATH)
    imgProc.irregular_quadrangle_crop_original_img(Point(408,11), Point(2088, 39), Point(2054, 1712), Point(404, 1666))
    imgProc.rotate_original_img(1)
    imgProc.crop_original_img(30, 1690, 400, 2070)
    imgProc.process_image()
    # imgProc.scale_original_img(IMAGESCALEFACTOR, IMAGESCALEFACTOR)
    # imgProc.show_original_img()
    ball = BallDetector(imgProc.get_original_img_array())
    ball.detectBall()
    ball.fillCircles()
    ball.show_img()
    # start = Point(ball.get_start_point().x * IMAGESCALEFACTOR,
    #               ball.get_start_point().y * IMAGESCALEFACTOR)
    # imgProc.set_original_img(ball.get_image())
    # imgProc.scale_original_img(IMAGESCALEFACTOR, IMAGESCALEFACTOR)
    # imgProc.process_image()

    # mazeSolver = MazeSolverBFS(start, imgProc.get_processed_img_array())
    # mazeSolver.find_end()
    # mazeSolver.solve_maze()
    # print(f"Execution time = {time() - startTime}")
    # mazeSolver.show_img()
    

    # while 1: Change condition to maze solved or not and remember to uncomment this while loop initialsation else nothing will work
    # camera.capture_file(imagePath)
    #     # print(ser.readline())
    #     count = input("How to turn the servo? ")
    #     ser.write(count.encode('ascii'))

    #     # Use imageProcessing class to process captured image into greyscale
    #     # Use greyscale image in mazeDetector and ballDetector
    #     # Output of mazeDetector is the maze and the end point of the maze
    #     # Output of the ballDetector is the start point of the maze
    #     # Outputs of mazeDetector and ballDetector are fed to mazeSolver
    #     # mazeSolver returns the path which is going to be followed by the ball in the main
    # camera.annotate_text_size = 100
    # camera.annotate_text = "MAZE SOLVED!"
    # camera.capture(imagePath)
