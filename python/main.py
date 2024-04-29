import serial
from time import sleep
from pathlib import Path
from picamera import PiCamera

arduino = '/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_24238313635351F0A162-if00'
baudrate = 115200
camera = PiCamera()

if __name__ == "__main__":
    ser = serial.Serial(arduino, baudrate)
    camera.resolution = (1280, 720)
    camera.exposure_compensation = 2
    camera.exposure_mode = 'auto'
    camera.meter_mode = 'average'
    camera.image_effect = 'none'
    imagePath = Path.joinpath(Path(__file__).parent.resolve(), 'img', 'capture.jpg')
    camera.start_preview()
    while 1: # Change condition to maze solved or not
        camera.capture(imagePath)
        # print(ser.readline())
        count = input("How to turn the servo? ")
        ser.write(count.encode('ascii'))

        # Use imageProcessing class to process captured image into greyscale
        # Use greyscale image in mazeDetector and ballDetector
        # Output of mazeDetector is the maze and the end point of the maze
        # Output of the ballDetector is the start point of the maze
        # Outputs of mazeDetector and ballDetector are fed to mazeSolver
        # mazeSolver returns the path which is going to be followed by the ball in the main
    camera.annotate_text_size = 100
    camera.annotate_text = "MAZE SOLVED!"
    camera.capture(imagePath)

