# import serial
# from time import sleep
from pathlib import Path
# from piCameraCtrl import Camera
from imageProcessing import Image_processing


ARDUINO = '/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_24238313635351F0A162-if00'
BAUDRATE = 115200
IMAGEPATH = Path.joinpath(Path(__file__).parent.resolve(
).parent.resolve(), 'img', 'maze_pic_1.jpg').__str__()


if __name__ == "__main__":
    #    ser = serial.Serial(arduino, baudrate)

    imgProc = Image_processing(IMAGEPATH)
    imgProc.rotate_original_img(-2.25)
    imgProc.crop_original_img(73, 2020, 1502, 3465)
    # imgProc.show_original_img()
    imgProc.process_image()
    imgProc.show_processed_img()

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
