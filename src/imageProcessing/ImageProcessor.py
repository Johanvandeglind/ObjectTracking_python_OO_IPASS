import cv2
import numpy as np
from src.Application.App import App
class ImageProcessor:
    def __init__(self):
        pass

    def empty(a):
        pass
    # cv2.namedWindow("Parameters")
    # cv2.resizeWindow("Parameters",640,240)
    # cv2.createTrackbar("Threshold1","Parameters",115,255,empty)
    # cv2.createTrackbar("Threshold2","Parameters",255,255,empty)
    # cv2.createTrackbar("opp","Parameters",5000,100000,empty)
    # cv2.createTrackbar("opp2","Parameters",65000,100000,empty)


    def get_Contours(self, img, t1,t2,opp,opp2):#
        _, thresh1 = cv2.threshold(img, 122, 51, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        big_cnt = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 25000 and area < 65000:
                #print(cnt)
                big_cnt.append(cnt)
        return big_cnt

    def format_image(self, img):
        #img = cv2.bitwise_not(img)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        return imgGray

    def combine_and_compare(self, cnt_real_img, cnt_robodk_img,real_img):

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
        #cv2.imshow("img_copy", img_copy)

        cv2.drawContours(img_copy, matchcont1, -1, (255, 0, 0), 3)
        cv2.drawContours(img_copy, matchcont2, -1, (0, 0, 255), 3)
        try:
            peri_cnt1 = cv2.arcLength(matchcont1, True)
            approx_cnt1 = cv2.approxPolyDP(matchcont1, 0.02 * peri_cnt1, True)
            # print(len(approx))
            x1, y1, w1, h1 = cv2.boundingRect(approx_cnt1)
            peri_cnt2 = cv2.arcLength(matchcont1, True)
            approx_cnt2 = cv2.approxPolyDP(matchcont2, 0.02 * peri_cnt2, True)
            # print(len(approx))
            x2, y2, w2, h2 = cv2.boundingRect(approx_cnt2)
            M_cnt1 = cv2.moments(matchcont1)
            cnt1X = int(M_cnt1["m10"] / M_cnt1["m00"])
            cnt1Y = int(M_cnt1["m01"] / M_cnt1["m00"])
            cv2.circle(img_copy, (cnt1X, cnt1Y), 3, (255, 0, 0), -1)

            M_cnt2 = cv2.moments(matchcont2)
            cnt2X = int(M_cnt2["m10"] / M_cnt2["m00"])
            cnt2Y = int(M_cnt2["m01"] / M_cnt2["m00"])
            print((cnt1X, cnt1Y), (cnt2X, cnt2Y))
            cv2.circle(img_copy, (cnt2X, cnt2Y), 3, (0, 0, 255), -1)
            return img_copy
        except:
            print("no shape found")
            return img_copy

    def show_and_save_image(self, path_real_image: str, path_robodk_image: str, output_name: str, size_pers: int, live: bool,
                            cameranumber: int,app:App):

        robodk_image = cv2.imread(path_robodk_image)
        if live:
            cap = cv2.VideoCapture(cameranumber)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2048)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1536)
            assert cap.isOpened(), "file/camera could not be opened!"
            while True:
                r, real_image = cap.read()
                #print(r)
                # print("realshape",real_image.shape[1],real_image.shape[0])
                #
                # print("roboshape",robodk_image.shape)
                real_img_format = self.format_image(real_image)
                robodk_img_format = self.format_image(robodk_image)

                t1 = cv2.getTrackbarPos("Threshold1", "Parameters")
                t2 = cv2.getTrackbarPos("Threshold2", "Parameters")
                opp = cv2.getTrackbarPos("opp", "Parameters")
                opp2 = cv2.getTrackbarPos("opp2", "Parameters")

                cnt_real_img = self.get_Contours(real_img_format, t1, t2, opp, opp2)
                cnt_robodk_img = self.get_Contours(robodk_img_format, t1, t2, opp, opp2)

                combined_image = self.combine_and_compare(cnt_real_img, cnt_robodk_img, real_image)
                # cv2.imwrite(output_name, combined_image)
                dim = (int(combined_image.shape[1] * size_pers / 100), int(combined_image.shape[0] * size_pers / 100))
                img = cv2.resize(combined_image, dim, interpolation=cv2.INTER_AREA)
                dim = (int(robodk_image.shape[1] * size_pers / 100), int(robodk_image.shape[0] * size_pers / 100))
                img2_res = cv2.resize(robodk_image, dim, interpolation=cv2.INTER_AREA)
                numpy_horizontal = np.hstack((img, img2_res))
                app.show_Image(numpy_horizontal)
                #cv2.imshow("Match!", numpy_horizontal)
                if cv2.waitKey(1) & 0xff == ord('q'):
                    break
        else:
            while True:
                real_image = cv2.imread(path_real_image)

                real_img_format = self.format_image(real_image)
                robodk_img_format = self.format_image(robodk_image)

                t1 = cv2.getTrackbarPos("Threshold1", "Parameters")
                t2 = cv2.getTrackbarPos("Threshold2", "Parameters")
                opp = cv2.getTrackbarPos("opp", "Parameters")
                opp2 = cv2.getTrackbarPos("opp2", "Parameters")

                cnt_real_img = self.get_Contours(real_img_format, t1, t2, opp, opp2)
                cnt_robodk_img = self.get_Contours(robodk_img_format, t1, t2, opp, opp2)

                combined_image = self.combine_and_compare(cnt_real_img, cnt_robodk_img, real_image)
                #cv2.imwrite(output_name, combined_image)
                dim = (int(combined_image.shape[1] * size_pers / 100), int(combined_image.shape[0] * size_pers / 100))
                img = cv2.resize(combined_image, dim, interpolation=cv2.INTER_AREA)
                dim = (int(robodk_image.shape[1] * 25 / 100), int(robodk_image.shape[0] * 25 / 100))
                img2_res = cv2.resize(robodk_image, dim, interpolation=cv2.INTER_AREA)
                numpy_horizontal = np.hstack((img, img2_res))
                app.show_Image(numpy_horizontal)
                #cv2.imshow("Match!", numpy_horizontal)
                #cv2.waitKey(0)
                if cv2.waitKey(1) & 0xff == ord('q'):
                    break
