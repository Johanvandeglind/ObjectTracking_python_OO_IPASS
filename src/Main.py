from src.ImageProcessor import ImageProcessor
from src.LiveImage import LiveImage
from src.statImage import StaticImage


class Main:
    cam_image = StaticImage('Recources/topview2.jpg', 'cam_img')
    robo_dk_image = StaticImage('Recources/cameraSideMount v5_v12.png', 'robodk_img')
    live_image = LiveImage(1, 'liveImage')
    imgprocessor = ImageProcessor()
    imgprocessor.show_and_save_image(cam_image.get_SourcePath(), robo_dk_image.get_SourcePath(),
                                     'combined_image.png', 25, True, live_image.get_CameraNumber())
