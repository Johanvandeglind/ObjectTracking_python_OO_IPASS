import cv2
from src.imageProcessing import Image


class App():
    def show_Image(self, image: Image.Image):
        # if cv2.getWindowProperty("Output")>0:
        #     cv2.clo
        cv2.imshow("Output",image)
