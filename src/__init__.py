from src import ImageProcessor
from src.LiveImage import LiveImage
from src.statImage import StaticImage


def main():
    cam_image = StaticImage('Recources/topview.jpg', 'camImg')
    robo_dk_image = StaticImage('Recources/cameraSideMount v5-Snapshot_v4.png', 'robodkImg')
    live_image = LiveImage(1, 'liveImage')
    ImageProcessor.ImageProcessor.show_and_save_image(cam_image.get_SourcePath(), robo_dk_image.get_SourcePath(),
                                                      'combinedimage.png', 25, False, live_image.get_CameraNumber())


if __name__ == "__main__":
    # execute only if run as a script
    main()
