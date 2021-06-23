import cv2
import numpy as np
from src.Application.App import App
from src.imageProcessing.LiveImage import LiveImage
from src.imageProcessing.StaticImage import StaticImage


class ImageProcessor:
    """
    This class processes the inputted images.
    """

    def empty(a):
        pass

    # cv2.namedWindow("Parameters")
    # cv2.resizeWindow("Parameters",640,240)
    # cv2.createTrackbar("Threshold1","Parameters",115,255,empty)
    # cv2.createTrackbar("Threshold2","Parameters",255,255,empty)
    # cv2.createTrackbar("opp","Parameters",5000,100000,empty)
    # cv2.createTrackbar("opp2","Parameters",65000,100000,empty)

    def get_Contours(self, img,t1, t2, opp, opp2):
        """
        This function makes an array wiht all the bigger countours of an image,
        a countour is the outside shape of een object, this fucntions finds the contours by colour differences
        :param img: The input image from what the countours should be found
        :return: An array of the contours witht he right sizes
        """
        _, thresh1 = cv2.threshold(img, 122, 51, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        big_cnt = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 25000 and area < 65000:
                # print(cnt)
                big_cnt.append(cnt)
        return big_cnt

    def format_image(self, img):
        """
        Converts the given image to a black and white image.
        :param img: The image to convert
        :return: a black and white image
        """
        # img = cv2.bitwise_not(img)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        return imgGray

    def get_coordinates(self, cnt):
        """
        this function returns the middelpoint of the given contour
        :param cnt: countour where middelpoint is to be found
        :return: middelpoint
        """
        peri_cnt1 = cv2.arcLength(cnt, True)
        approx_cnt1 = cv2.approxPolyDP(cnt, 0.02 * peri_cnt1, True)
        # print(len(approx))
        x1, y1, w1, h1 = cv2.boundingRect(approx_cnt1)
        M_cnt1 = cv2.moments(cnt)
        cnt1X = int(M_cnt1["m10"] / M_cnt1["m00"])
        cnt1Y = int(M_cnt1["m01"] / M_cnt1["m00"])
        return cnt1X, cnt1Y

    def combine_and_compare(self, cnt_real_img, cnt_robodk_img, real_img):
        """
        this function uses 2 arrays of contours and compares these to find the closest mach as possible.
        From the cnt_robodk_img is known that there is only 1 contours. This is the right contour at the right place,
        this function compares the contours in the real image with the contour in the robodk_image
        then when the matched contours are found it returns an copied image of the real_img with the drawn contours in it
        :param cnt_real_img:
        :param cnt_robodk_img:
        :param real_img:
        :return: copied image with drawn contour and drawn middelpoint
        """
        img_copy = real_img.copy()

        smatch = 10
        matchcont1 = []
        matchcont2 = []
        for x in range(len(cnt_real_img)):
            for y in range(len(cnt_robodk_img)):
                match = (cv2.matchShapes(cnt_real_img[x], cnt_robodk_img[y], 2, 0.0))
                # print(match)
                if match < smatch:
                    smatch = match
                    matchcont1 = cnt_real_img[x]
                    matchcont2 = cnt_robodk_img[y]
        # cv2.imshow("img_copy", img_copy)

        cv2.drawContours(img_copy, matchcont1, -1, (255, 0, 0), 3)
        cv2.drawContours(img_copy, matchcont2, -1, (0, 0, 255), 3)
        try:
            cnt1X, cnt1Y = self.get_coordinates(matchcont1)
            cnt2X, cnt2Y = self.get_coordinates(matchcont2)
            print("cnt_live x,y", (cnt1X, cnt1Y))
            print("cnt_robodk x,y", (cnt2X, cnt2Y))
            cv2.circle(img_copy, (cnt1X, cnt1Y), 3, (255, 0, 0), -1)
            cv2.circle(img_copy, (cnt2X, cnt2Y), 3, (0, 0, 255), -1)
            return img_copy
        except:
            print("no shape found")
            return img_copy


    def generate_new_image(self,rl_image,robodk_image,app: App,size_pers:int):
        """
        This image uses the functions above to find the contour in the live/real image
        that best matches the contour of the robodk image.
        Then it outputs it using the app so the user can see it.
        :param rl_image: Real/live image
        :param robodk_image: the referense image from robodk
        :param app: The app to show the final result
        :param size_pers: the scal the image is outputed in, orignal is 2156*1944 and does not fit on the screen
        :return: The app view
        """
        real_img_format = self.format_image(rl_image)
        robodk_img_format = self.format_image(robodk_image)

        t1 = cv2.getTrackbarPos("Threshold1", "Parameters")
        t2 = cv2.getTrackbarPos("Threshold2", "Parameters")
        opp = cv2.getTrackbarPos("opp", "Parameters")
        opp2 = cv2.getTrackbarPos("opp2", "Parameters")

        cnt_real_img = self.get_Contours(real_img_format, t1, t2, opp, opp2)
        cnt_robodk_img = self.get_Contours(robodk_img_format, t1, t2, opp, opp2)

        combined_image = self.combine_and_compare(cnt_real_img, cnt_robodk_img, rl_image)
        dim = (int(combined_image.shape[1] * size_pers / 100), int(combined_image.shape[0] * size_pers / 100))
        img = cv2.resize(combined_image, dim, interpolation=cv2.INTER_AREA)
        dim = (int(robodk_image.shape[1] * size_pers / 100), int(robodk_image.shape[0] * size_pers / 100))
        img2_res = cv2.resize(robodk_image, dim, interpolation=cv2.INTER_AREA)
        numpy_horizontal = np.hstack((img, img2_res))
        app.show_Image(numpy_horizontal)

    def show_and_save_image(self, real_image: StaticImage, robodk_image: StaticImage, size_pers: int,
                            liveimage: LiveImage, app: App):
        """
        This function checks if the camera is connected via usb.
        If not it uses the static real image and if so it uses the live feed of the camera
        Then it activates the generate_new_image function.
        """
        robodk_image = cv2.imread(robodk_image.get_SourcePath())
        cap = cv2.VideoCapture(liveimage.get_CameraNumber())
        if cap.isOpened():
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2048)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1536)
            assert cap.isOpened(), "file/camera could not be opened!"
            while True:
                r, rl_image = cap.read()
                self.generate_new_image(rl_image,robodk_image,app,size_pers)
                if cv2.waitKey(1) & 0xff == ord('q'):
                    break
        else:
            while True:
                rl_image = cv2.imread(real_image.get_SourcePath())
                self.generate_new_image(rl_image, robodk_image, app, size_pers)
                if cv2.waitKey(1) & 0xff == ord('q'):
                    break
