import serial
from time import sleep
from pathlib import Path
from piCameraCtrl import Camera
from imageProcessing import ImageProcessing
from ballDetector import BallDetector
from time import time
from point import Point
from mazeSolverBFS import MazeSolverBFS
# import cv2


ARDUINO = '/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_24238313635351F0A162-if00'
BAUDRATE = 115200
# IMAGEPATH = Path.joinpath(Path(__file__).parent.resolve(
# ).parent.resolve(), 'img', 'maze_pic_1.jpg').__str__()
IMAGEPATH = Path.joinpath(Path(__file__).parent.resolve(
).parent.resolve(), 'img', 'capture.jpg').__str__()
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
    ser = serial.Serial(ARDUINO, BAUDRATE)
    sleep(3)
    camera = Camera()
    camera.cameraCapture()
    # camera.startPreview()

    imgProc = ImageProcessing(Path.joinpath(Path(__file__).parent.resolve(
).parent.resolve(), 'img', 'capture_031.jpg').__str__())
    # imgProc.show_original_img()
    # imgProc.irregular_quadrangle_crop_original_img(Point(408,11), Point(2088, 39), Point(2054, 1712), Point(404, 1666))
    # imgProc.show_original_img()
    # imgProc.rotate_original_img(-1)  # : Capture1.jpg
    imgProc.crop_original_img(5, -1, 0, -1)  # : Capture1.jpg
    # imgProc.show_original_img()
    # imgProc.rotate_original_img(-1.5)  # : testdata
    # imgProc.crop_original_img(75, 2010, 1501, 3466)  # : testdata

    # ball = BallDetector(imgProc.get_original_img_array())
    # ballDetected = ball.detectBall()
    # ball.fillCircles()
    # ball.show_img()
    # start = Point(ball.get_start_point().x * IMAGESCALEFACTOR,
    #                 ((ball.get_start_point().y * IMAGESCALEFACTOR) - (ball.get_radius() * IMAGESCALEFACTOR *0)))
    # imgProc.set_original_img(ball.get_image())
    imgProc.process_image()
    # imgProc.show_processed_img()
    imgProc.store_processed_image()
    imgProc.scale_processed_img(IMAGESCALEFACTOR, IMAGESCALEFACTOR)
    scaledMaze = imgProc.get_processed_img_array()
    # imgProc.show_processed_img()
    
    imgProc = ImageProcessing(IMAGEPATH)
    imgProc.rotate_original_img(-1)  # : Capture1.jpg
    imgProc.crop_original_img(80, 1795, 345, 2045)  # : Capture1.jpg
    ball = BallDetector(imgProc.get_original_img_array())
    ballDetected = ball.detectBall()
    ball.fillCircles()
    # ball.show_img()
    start = Point(ball.get_start_point().x * IMAGESCALEFACTOR,
                    ((ball.get_start_point().y * IMAGESCALEFACTOR) - (ball.get_radius() * IMAGESCALEFACTOR *0)))

    mazeSolver = MazeSolverBFS(start, scaledMaze)
    # mazeSolver.find_end()
    end = Point(0,146)
    # end = Point(0,142)
    # mazeSolver.solve_maze()
    # print(f"Execution time = {time() - startTime}")
    # path = mazeSolver.__getattribute__("path")
    # mazeSolver.show_img()
    # diff = path[1] - path[0]
    
    # ballUndetectedReps = 0
    lastMove = {"move":0, "count":0}
    y_move_count=0
    # while ballUndetectedReps < 3:
    #     if ~ballDetected:
    #         ballUndetectedReps = ballUndetectedReps + 1
    #         ballDetected = True
    while ballDetected:
        camera.cameraCapture()
        imgProc = ImageProcessing(IMAGEPATH)
        imgProc.rotate_original_img(-1)  # : Capture1.jpg
        imgProc.crop_original_img(80, 1795, 345, 2045)  # : Capture1.jpg
        ball = BallDetector(imgProc.get_original_img_array())
        ballDetected = ball.detectBall()
        if ballDetected == False:
            for i in range (0,2):
                sleep(1)
                camera.cameraCapture()
                imgProc = ImageProcessing(IMAGEPATH)
                imgProc.rotate_original_img(-1)  # : Capture1.jpg
                imgProc.crop_original_img(80, 1795, 345, 2045)  # : Capture1.jpg
                ball = BallDetector(imgProc.get_original_img_array())
                ballDetected = ball.detectBall()
                if ballDetected : break
            if ballDetected == False: 
                print("BALL UNDETECTED AFTER 3 TRIES")
                exit(0)
        ball.fillCircles()
        start = Point(ball.get_start_point().x * IMAGESCALEFACTOR,
                        ball.get_start_point().y * IMAGESCALEFACTOR)
        # imgProc.set_original_img(ball.get_image())
        # imgProc.scale_processed_img(IMAGESCALEFACTOR, IMAGESCALEFACTOR)
        # imgProc.show_processed_img()
        # ball.show_img()

        mazeSolver = MazeSolverBFS(start, scaledMaze)
        mazeSolver.set_end(end)
        mazeSolver.solve_maze()
        # print(f"Execution time = {time() - startTime}")
        path = mazeSolver.__getattribute__("path")
        # mazeSolver.show_img()
        # print(f"last move = {lastMove['move']}; count = {lastMove['count']}")
        # diff = path[int(1.8*ball.get_radius()*IMAGESCALEFACTOR)] - path[0]
        pathOffset = 32 if lastMove['count'] > 2 else 20


        if len(path) > pathOffset:
            diff = path[pathOffset] - path[0]
        else :
            diff=path[len(path)-1]-path[0]
        
        if ((abs(diff.y) > abs(diff.x)) & (y_move_count<3)):
            y_move_count+=1
            if (diff.y > 0) :
                ser.write('4'.encode('ascii'))
                if lastMove['move'] == 4 : lastMove['count'] +=1
                else: lastMove.update({'move':4, 'count':1})
            else :
                ser.write('3'.encode('ascii'))
                if lastMove['move'] == 3 : lastMove['count'] +=1
                else: lastMove.update({'move':3, 'count':1})
        elif abs(diff.x) > abs(diff.y):
            y_move_count=0
            if (diff.x > 0):
                ser.write('2'.encode('ascii'))
                if lastMove['move'] == 2 : lastMove['count'] +=1
                else: lastMove.update({'move':2, 'count':1})
            else :
                ser.write('1'.encode('ascii'))
                if lastMove['move'] == 1 : lastMove['count'] +=1
                else: lastMove.update({'move':1, 'count':1})
        else:
            y_move_count=0
            if (diff.x > 0):
                ser.write('2'.encode('ascii'))
                if lastMove['move'] == 2 : lastMove['count'] +=1
                else: lastMove.update({'move':2, 'count':1})
            else :
                ser.write('1'.encode('ascii'))
                if lastMove['move'] == 1 : lastMove['count'] +=1
                else: lastMove.update({'move':1, 'count':1})


        # diff = path[5] - path[0]
        # if (diff.x == 0 ):
        #     if(diff.y>0):
        #         ser.write('4'.encode('ascii'))
        #         if lastMove['move'] == 4 : lastMove['count'] +=1
        #         else: lastMove.update({'move':4, 'count':1})
        #     else:
        #         ser.write('3'.encode('ascii'))
        #         if lastMove['move'] == 3 : lastMove['count'] +=1
        #         else: lastMove.update({'move':3, 'count':1})
        # elif (diff.y == 0):
        #     if(diff.x>0):
        #         ser.write('2'.encode('ascii'))
        #         if lastMove['move'] == 2 : lastMove['count'] +=1
        #         else: lastMove.update({'move':2, 'count':1})
        #     else:
        #         ser.write('1'.encode('ascii'))
        #         if lastMove['move'] == 1 : lastMove['count'] +=1
        #         else: lastMove.update({'move':1, 'count':1})
        # elif(diff.x == diff.y):
        #     if(diff.x>0):
        #         ser.write('2'.encode('ascii'))
        #         if lastMove['move'] == 2 : lastMove['count'] +=1
        #         else: lastMove.update({'move':2, 'count':1})
        #     else:
        #         ser.write('1'.encode('ascii'))
        #         if lastMove['move'] == 1 : lastMove['count'] +=1
        #         else: lastMove.update({'move':1, 'count':1})
        # elif ((diff.x > 0) & (diff.y > 0) ):
        #     if diff.y < diff.x:
        #         ser.write('2'.encode('ascii'))
        #         if lastMove['move'] == 2 : lastMove['count'] +=1
        #         else: lastMove.update({'move':2, 'count':1})
        #     # else:
        #     #     ser.write('2'.encode('ascii'))
        #     #     if lastMove['move'] == 2 : lastMove['count'] +=1
        #     #     else: lastMove.update({'move':2, 'count':1})
        # elif ((diff.x < 0) & (diff.y < 0)):
        #     if diff.y > diff.x:
        #         ser.write('2'.encode('ascii'))
        #         if lastMove['move'] == 2 : lastMove['count'] +=1
        #         else: lastMove.update({'move':2, 'count':1})
        #     else:
        #         ser.write('1'.encode('ascii'))
        #         if lastMove['move'] == 1 : lastMove['count'] +=1
        #         else: lastMove.update({'move':1, 'count':1})
        # elif ((diff.x>0) & (diff.y <0)):
        #     ser.write('2'.encode('ascii'))
        #     if lastMove['move'] == 2 : lastMove['count'] +=1
        #     else: lastMove.update({'move':2, 'count':1})
        # else :
        #     if abs(diff.y) < abs(diff.x):
        #         ser.write('2'.encode('ascii'))
        #         if lastMove['move'] == 2 : lastMove['count'] +=1
        #         else: lastMove.update({'move':2, 'count':1})
        #     else:
        #         ser.write('1'.encode('ascii'))
        #         if lastMove['move'] == 1 : lastMove['count'] +=1
        #         else: lastMove.update({'move':1, 'count':1})
    
        
        sleep(2)
        