import serial
from time import sleep
from pathlib import Path
# from piCameraCtrl import Camera
from imageProcessing import ImageProcessing
from ballDetector import BallDetector
from time import time
from point import Point
from mazeSolverBFS import MazeSolverBFS


ARDUINO = '/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_24238313635351F0A162-if00'
BAUDRATE = 115200
# IMAGEPATH = Path.joinpath(Path(__file__).parent.resolve(
# ).parent.resolve(), 'img', 'maze_pic_1.jpg').__str__()
IMAGEPATH = Path.joinpath(Path(__file__).parent.resolve(
).parent.resolve(), 'img', 'capture1.jpg').__str__()
MAZEIMGPATH = Path.joinpath(Path(__file__).parent.resolve(
).parent.resolve(), 'img', 'maze_rpi_pic.jpg').__str__()
IMAGESCALEFACTOR = 0.25
CELL_SIZE = 20
HALF_CELL_SIZE = CELL_SIZE/2
ballDetected = True
directions = [Point(0, -1), Point(0, 1),
                           Point(1, 0), Point(-1, 0)]

if __name__ == "__main__":
    startTime = time()
    # ser = serial.Serial(ARDUINO, BAUDRATE)
    # camera = Camera()
    # camera.cameraCapture()


    imgProc = ImageProcessing(IMAGEPATH)
    # imgProc.show_original_img()
    # imgProc.irregular_quadrangle_crop_original_img(Point(408,11), Point(2088, 39), Point(2054, 1712), Point(404, 1666))
    imgProc.rotate_original_img(-2.25)  # : Capture1.jpg
    imgProc.crop_original_img(70, 1790, 480, 2200)  # : Capture1.jpg
    # imgProc.show_original_img()
    # imgProc.rotate_original_img(-1.5)  # : testdata
    # imgProc.crop_original_img(75, 2010, 1501, 3466)  # : testdata
    ball = BallDetector(imgProc.get_original_img_array())
    ballDetected = ball.detectBall()
    ball.fillCircles()
    start = Point(ball.get_start_point().x * IMAGESCALEFACTOR,
                    ball.get_start_point().y * IMAGESCALEFACTOR)
    imgProc.set_original_img(ball.get_image())
    imgProc.process_image()
    # imgProc.show_processed_img()
    imgProc.store_processed_image()
    imgProc.scale_processed_img(IMAGESCALEFACTOR, IMAGESCALEFACTOR)
    mazeSolver = MazeSolverBFS(start, imgProc.get_processed_img_array())
    mazeSolver.find_end()
    end = mazeSolver.__getattribute__("end")
    mazeSolver.solve_maze()
    print(f"Execution time = {time() - startTime}")
    path = mazeSolver.__getattribute__("path")
    mazeSolver.show_img()
    diff = path[1] - path[0]
    
    # if diff.x > 0:
    #     ser.write('1'.encode('ascii'))
    # elif diff.x < 0:
    #     ser.write('2'.encode('ascii'))
    # elif diff.y > 0:
    #     ser.write('3'.encode('ascii'))
    # elif diff.y < 0:
    #     ser.write('4'.encode('ascii'))
    
    while ballDetected:
        imgProc = ImageProcessing(IMAGEPATH)
        # imgProc.show_original_img()
        # imgProc.irregular_quadrangle_crop_original_img(Point(408,11), Point(2088, 39), Point(2054, 1712), Point(404, 1666))
        imgProc.rotate_original_img(-2.25)  # : Capture1.jpg
        imgProc.crop_original_img(70, 1790, 480, 2200)  # : Capture1.jpg
        # imgProc.show_original_img()
        # imgProc.rotate_original_img(-1.5)  # : testdata
        # imgProc.crop_original_img(75, 2010, 1501, 3466)  # : testdata
        ball = BallDetector(imgProc.get_original_img_array())
        ballDetected = ball.detectBall()
        ball.fillCircles()
        start = Point(ball.get_start_point().x * IMAGESCALEFACTOR,
                        ball.get_start_point().y * IMAGESCALEFACTOR)
        imgProc.set_original_img(ball.get_image())
        imgProc.scale_processed_img(IMAGESCALEFACTOR, IMAGESCALEFACTOR)
        # imgProc.show_processed_img()
        scaledMaze = imgProc.get_maze_image(IMAGESCALEFACTOR, IMAGESCALEFACTOR)
        mazeSolver = MazeSolverBFS(start, scaledMaze)
        mazeSolver.set_end(end)
        mazeSolver.solve_maze()
        print(f"Execution time = {time() - startTime}")
        path = mazeSolver.__getattribute__("path")
        mazeSolver.show_img()
        
        diff = path[1] - path[0]
        wall = False
        i = int(0)
        if diff.x == 0:
            while diff.x == 0:
                i = i + 1
                diff = path[i+1] - path[i]
                if diff.x != 0:
                    for d in directions:
                        cell = path[i] + d
                        if (scaledMaze[cell.y][cell.x]==0):
                            print("Wall found")
                            wall = True
                            # if d.y > 0:
                            #     ser.write('3'.encode('ascii'))
                            # elif d.y < 0:
                            #     ser.write('4'.encode('ascii'))
                            break
        
        elif diff.y == 0:
            while diff.y == 0:
                i = i + 1
                diff = path[i+1] - path[i]
                if diff.y != 0:
                    for d in directions:
                        cell = path[i] + d
                        if (scaledMaze[cell.y][cell.x]==0):
                            print("Wall found")
                            wall = True
                            # if d.x > 0:
                            #     ser.write('1'.encode('ascii'))
                            # elif d.x < 0:
                            #     ser.write('2'.encode('ascii'))
                            break
        
        if wall == False:
            print("No Walls")
            diff = path[1] - path[0]
            # if diff.x > 0:
            #     ser.write('5'.encode('ascii'))
            # elif diff.x < 0:
            #     ser.write('6'.encode('ascii'))
            # elif diff.y > 0:
            #     ser.write('7'.encode('ascii'))
            # elif diff.y < 0:
            #     ser.write('8'.encode('ascii'))

    # mazeSolved = False
    # current = Point()
    # lastMsg = '0'
    # j = int(0)
    # while ~mazeSolved:
    #     ser.write('0'.encode('ascii'))
    #     camera = Camera()
    #     camera.cameraCapture()
    #     imgProc = ImageProcessing(IMAGEPATH)
    #     imgProc.rotate_original_img(-2)  # : Capture.jpg
    #     imgProc.crop_original_img(105, 1815, 480, 2200)  # : Capture.jpg
    #     # imgProc.rotate_original_img(-1.5)  # : testdata
    #     # imgProc.crop_original_img(75, 2010, 1501, 3466)  # : testdata
    #     ball = BallDetector(imgProc.get_original_img_array())
    #     ball.detectBall()
    #     ball.fillCircles()
    #     current = Point(ball.get_start_point().x * IMAGESCALEFACTOR,
    #                     ball.get_start_point().y * IMAGESCALEFACTOR)
    #     pathLoc = Point()
    #     while 1:
    #         if(path[j].x-HALF_CELL_SIZE < current.x < path[j].x+HALF_CELL_SIZE):
    #             break
    #         elif (path[j].y-HALF_CELL_SIZE < current.y < path[j].y+HALF_CELL_SIZE):
    #             break
    #         j += 1
    #     diff = path[j+CELL_SIZE] - path[j]
    #     if (diff.x >= 15) & (lastMsg != '1'):

    #         pass
    #     elif (diff.x <= -15) & (lastMsg != '2'):

    #         pass
    #     elif (diff.y >= 15) & (lastMsg != '3'):

    #         pass
    #     elif (diff.y <= -15) & (lastMsg != '4'):

    #         pass
    #     sleep(1)
    #     ser.write('0'.encode('ascii'))
