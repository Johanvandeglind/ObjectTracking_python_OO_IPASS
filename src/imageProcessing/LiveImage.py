from src.imageProcessing import Image


class LiveImage(Image.Image):
    """
    This class is a extantion of the class Image
    This class adds the parameter Cameranumber to the object Image.
    This because the LiveImage does not have a sourcepath.
    """
    CameraNumber = 0

    def __init__(self, CameraNumber:int,name:str):
        self.name = name
        self.CameraNumber = CameraNumber

    def get_CameraNumber(self):
        return self.CameraNumber