from picamera2 import Picamera2, Preview
from libcamera import controls # type: ignore
import time

picam2 = Picamera2()

camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config) # type: ignore
picam2.set_controls({"ExposureTime": 10000, "AnalogueGain": 1.0})
picam2.start_preview(Preview.QTGL) # type: ignore
picam2.start()
time.sleep(12)
picam2.capture_file("test.jpg")