class Image:
    """
    This class is a perent class of LiveImage and StaticImage,
    this is because these classes have much in commen but have 2 differentses.
    The LiveImage class has a camera number, and the StaticImage has a sourcepath where the image can be found.
    """
    resolution = (0, 0)
    name = ''

    def __init__(self,name:str):
        self.name = name


    def set_resolution(self, res:(int,int)):
        self.resolution = res