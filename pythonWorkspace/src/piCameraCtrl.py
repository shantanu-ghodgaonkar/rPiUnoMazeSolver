from picamera2 import Picamera2, Preview
from libcamera import Transform
import time
from pathlib import Path

IMAGEPATH = Path.joinpath(Path(__file__).parent.resolve(
).parent.resolve(), 'img', 'capture.jpg').__str__()
class Camera:
    def __init__(self) -> None:
        self.camera = camera = Picamera2()
        self.camera.configure(camera.create_preview_configuration())
        self.camera.set_controls({"ExposureTime": 60000, "AnalogueGain": 0.5})
        self.camera.start()

    def startPreview(self) -> None:
        self.camera.start_preview(
            Preview.QTGL, x=50, y=50, width=800, height=600, transform=Transform(hflip=1))
        # self.camera.start()

    def cameraCapture(self):
        # return self.camera.capture_image("capture")
        config = self.camera.create_still_configuration({"size": (2592, 1944)})
        self.camera.switch_mode_and_capture_file(config, IMAGEPATH)
        # self.camera.capture_file(IMAGEPATH)
        # self.camera.stop()

    def getCamera(self) -> Picamera2:
        return self.camera
    
    def stopPreview(self):
        self.camera.stop_preview()


if __name__ == "__main__":
    cam1 = Camera()
    cam1.startPreview()
    time.sleep(10)
    cam1.stopPreview()
