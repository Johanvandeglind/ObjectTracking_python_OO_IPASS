# from src.Application.flask_app import App
from src.imageProcessing.ImageProcessor import ImageProcessor
from src.imageProcessing.LiveImage import LiveImage
from src.imageProcessing.statImage import StaticImage
from src.Application.flask_app import app


class Main:
    cam_image = StaticImage('Recources/topview2.jpg', 'cam_img')
    robo_dk_image = StaticImage('Recources/cameraSideMount v5_v11.png', 'robodk_img')
    live_image = LiveImage(1, 'liveImage')
    imgprocessor = ImageProcessor()
    imgprocessor.show_and_save_image(cam_image.get_SourcePath(), robo_dk_image.get_SourcePath(),
                                     'combined_image.png', 25, False, live_image.get_CameraNumber())
