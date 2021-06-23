from unittest import TestCase

from src.imageProcessing.LiveImage import LiveImage


class TestLiveImage(TestCase):
    def test_get_camera_number(self):
        cam = LiveImage(0, "cam0")
        self.assertEqual(cam.get_CameraNumber(), 0)
