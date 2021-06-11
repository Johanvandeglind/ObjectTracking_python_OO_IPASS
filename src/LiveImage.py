import src
from src import Image
class LiveImage(Image.Image):
    CameraNumber = 0

    def __init__(self, CameraNumber:int,name:str):
        self.name = name
        self.CameraNumber = CameraNumber

    def get_CameraNumber(self):
        return self.CameraNumber