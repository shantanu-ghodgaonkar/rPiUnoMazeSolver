import serial
from time import sleep
from pathlib import Path
from picamera import PiCamera
from io import BytesIO

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
    while 1:
        camera.start_preview()
        camera.capture(Path.joinpath(Path(__file__).parent.resolve(), 'img', 'capture.jpg'))
        # print(ser.readline())
        count = input("How to turn the servo? ")
        ser.write(count.encode('ascii'))
