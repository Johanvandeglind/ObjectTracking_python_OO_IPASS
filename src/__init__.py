#lulaconst1
import cv2

from src.Application.App import App
from src.imageProcessing.ImageProcessor import ImageProcessor
from src.imageProcessing.LiveImage import LiveImage
from src.imageProcessing.statImage import StaticImage


class Main:
    """
    The purpose of this class is to make and define the used objects
    and after that to run the imageprocessor with these objects as input

    app             ->  The window/application where the edited image is shown
    cam_image       ->  a static image taken with the camera, this image is used when there is no camera atached to the system
    robo_dk_image   ->  this is a generated refference image created in a program called RoboDk,
                        this is wat the camera is supposed to see
    live_image      ->  declaration of the camera
    imageprocessor  ->  The object that processes the image.

    """
    app = App()
    cam_image = StaticImage('Recources/topview2.jpg', 'cam_img')
    robo_dk_image = StaticImage('Recources/cameraSideMount v5_v11.png', 'robodk_img')
    live_image = LiveImage(1, 'liveImage')
    imgprocessor = ImageProcessor()
    imgprocessor.show_and_save_image(cam_image, robo_dk_image, 25, live_image, app)

if __name__ == "__main__":
    Main()

