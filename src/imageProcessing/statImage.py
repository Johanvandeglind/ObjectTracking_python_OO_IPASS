from src.imageProcessing import Image


class StaticImage(Image.Image):
    """
    This class is a extantion of the class Image
    This class adds the parameter sourcePath to the object Image.
    """
    sourcePath = ""

    def __init__(self, sourcePath: int, name: str):
        self.name = name
        self.sourcePath = sourcePath

    def get_SourcePath(self):
        return self.sourcePath
