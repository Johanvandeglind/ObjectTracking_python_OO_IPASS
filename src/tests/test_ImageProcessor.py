import unittest
import cv2

from src.imageProcessing.ImageProcessor import ImageProcessor


class TestImageProcessor(unittest.TestCase):


    def test_format_image(self):

        ip = ImageProcessor()

        img = cv2.imread('Resources/topview.jpg')

        self.assertEqual(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), ip.format_image(img))





if __name__ == "__main__":
    unittest.main()