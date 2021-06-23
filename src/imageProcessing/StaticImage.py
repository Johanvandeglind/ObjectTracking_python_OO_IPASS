#Copyright 2021, Johan van de Glind, All rights reserved.
from src.imageProcessing import Image


class StaticImage(Image.Image):
    """
    This class is a extantion of the class Image
    This class adds the parameter sourcePath to the object Image.
    """
    sourcePath = ""

    def __init__(self, sourcePath: str, name: str):
        self.name = name
        self.sourcePath = sourcePath

    def get_SourcePath(self):
        return self.sourcePath
