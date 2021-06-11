class Image:
    resolution = (0, 0)
    name = ''

    def __init__(self,name:str):
        self.name = name


    def set_resolution(self, res:(int,int)):
        self.resolution = res