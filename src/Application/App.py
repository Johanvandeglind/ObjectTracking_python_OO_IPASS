import cv2
from src.imageProcessing import Image


class App():
    """
    This class generates the application/window where the image is displayed
    """
    def show_Image(self, image: Image.Image):
        # if cv2.getWindowProperty("Output")>0:
        #     cv2.clo
        cv2.imshow("Output",image)
