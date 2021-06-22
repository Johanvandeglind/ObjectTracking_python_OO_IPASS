from src.imageProcessing import Image


class StaticImage(Image.Image):
    sourcePath = 0

    def __init__(self, sourcePath:int,name:str):
        self.name = name
        self.sourcePath = sourcePath

    def get_SourcePath(self):
        return self.sourcePath