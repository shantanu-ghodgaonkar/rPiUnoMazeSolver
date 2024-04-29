import serial
from time import sleep
from pathlib import Path
from picamera2 import Picamera2, Preview

arduino = '/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_24238313635351F0A162-if00'
baudrate = 115200
camera = Picamera2()

if __name__ == "__main__":
#    ser = serial.Serial(arduino, baudrate)
    imagePath = Path.joinpath(Path(__file__).parent.resolve(), 'img', 'capture.jpg')
    
    camera.configure(camera.create_preview_configuration()) # type: ignore
    camera.start_preview(Preview.QTGL) # type: ignore
    camera.start()
    while 1: # Change condition to maze solved or not
        camera.capture_file(imagePath)
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

