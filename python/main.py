import serial
arduino = '/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_24238313635351F0A162-if00'
baudrate = 115200
ser = serial.Serial(arduino, baudrate)
while 1:
    #print(ser.readline())
    count = input("How many times should the LED blink? ")
    ser.write(count.encode('ascii'))
