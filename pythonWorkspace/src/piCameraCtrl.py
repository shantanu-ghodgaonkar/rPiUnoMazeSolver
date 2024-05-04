from picamera2 import Picamera2, Preview
from libcamera import Transform

class Camera:
    def __init__(self) -> None:
        self.camera = camera = Picamera2()
        self.camera.configure(camera.create_preview_configuration())
        self.camera.set_controls({"ExposureTime": 10000, "AnalogueGain": 1.0})
        
    def startPreview(self) -> None:
        self.camera.start_preview(Preview.DRM, x=50, y=50, width=800, height=600, transform=Transform(hflip=1))
        self.camera.start()
        
    def cameraCapture(self):
        return self.camera.switch_mode_and_capture_image(capture_config,"cpature")
        
    def getCamera(self) -> Picamera2:
        return self.camera
