import cv2


class ImageProcessor:
    def __init__(self):
        pass

    def empty(a):
        pass
    cv2.namedWindow("Match!")
    cv2.resizeWindow("Match!",640,240)
    cv2.createTrackbar("Threshold1","Match!",140,255,empty)
    cv2.createTrackbar("Threshold2","Match!",86,255,empty)
    cv2.createTrackbar("opp","Match!",25000,100000,empty)
    cv2.createTrackbar("opp2","Match!",45000,100000,empty)


    def get_Contours(self, img, cont_image  ,t1,t2,opp,opp2):#
        _, thresh1 = cv2.threshold(img, t1, t2, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        big_cnt = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            # qprint(area)

            if area > opp and area < opp2:
                big_cnt.append(cnt)
        return big_cnt

    def format_image(self, img):

        imgCont = img.copy()
        img = cv2.bitwise_not(img)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        t1 = cv2.getTrackbarPos("Threshold1","Match!")
        t2 = cv2.getTrackbarPos("Threshold2", "Match!")
        opp = cv2.getTrackbarPos("opp", "Match!")
        opp2 = cv2.getTrackbarPos("opp2", "Match!")
        cnt = self.get_Contours(imgGray, imgCont ,t1,t2,opp,opp2)  #
        return cnt

    def combine_and_compare(self, img1, img2):
        cnt1 = self.format_image(img1)
        cnt2 = self.format_image(img2)
        img_copy = img1.copy()
        smatch = 10
        matchcont1 = []
        matchcont2 = []
        for x in range(len(cnt1)):
            for y in range(len(cnt2)):
                match = (cv2.matchShapes(cnt1[x], cnt2[y], 2, 0.0))

                #cv2.drawContours(img_copy, cnt2[y], -1, (0, 0, 255), 3)
                # cv2.imshow("im_Copy",img_copy)
                # cv2.waitKey(3)
                print(match)
                if match < smatch:
                    smatch = match
                    matchcont1 = cnt1[x]
                    matchcont2 = cnt2[y]
        # cv2.imshow("Match!", img_copy)

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
            # calculate x,y coordinate of center
            cnt1X = int(M_cnt1["m10"] / M_cnt1["m00"])
            cnt1Y = int(M_cnt1["m01"] / M_cnt1["m00"])
            cv2.circle(img_copy, (cnt1X, cnt1Y), 3, (255, 0, 0), -1)

            M_cnt2 = cv2.moments(matchcont2)
            cnt2X = int(M_cnt2["m10"] / M_cnt2["m00"])
            cnt2Y = int(M_cnt2["m01"] / M_cnt2["m00"])
            #print((cnt1X, cnt1Y), (cnt2X, cnt2Y))
            cv2.circle(img_copy, (cnt2X, cnt2Y), 3, (0, 0, 255), -1)
            return img_copy
        except:
            print("no shape found")
            return img_copy

    def show_and_save_image(self, real_image: str, robodk_image: str, output_name: str, size_pers: int, live: bool,
                            cameranumber: int):

        img2 = cv2.imread(robodk_image)
        if live:
            cap = cv2.VideoCapture(cameranumber)
            cap.set(3, 2592)
            cap.set(4, 1944)
            assert cap.isOpened(), "file/camera could not be opened!"
            while True:
                succes, img1 = cap.read()
                # cv2.imshow("Match!", img1)
                # #cv2.waitKey(1)
                # if cv2.waitKey(1) & 0xff == ord('q'):
                combined_image = self.combine_and_compare(img1, img2)
                # #cv2.imwrite(output_name, combined_image)
                dim = (int(combined_image.shape[1] * size_pers / 100), int(combined_image.shape[0] * size_pers / 100))
                #
                # # resize image
                img = cv2.resize(combined_image, dim, interpolation=cv2.INTER_AREA)
                cv2.imshow("Match!", img)
                cv2.waitKey(1)
                if cv2.waitKey(1) & 0xff == ord('q'):
                    break
        else:
            while True:
                img1 = cv2.imread(real_image)
                combined_image = self.combine_and_compare(img1, img2)
                cv2.imwrite(output_name, combined_image)
                scale_percent = size_pers  # percent of original size
                width = int(combined_image.shape[1] * scale_percent / 100)
                height = int(combined_image.shape[0] * scale_percent / 100)
                dim = (width, height)
                print(dim)

                # resize image
                img = cv2.resize(combined_image, dim, interpolation=cv2.INTER_AREA)
                cv2.imshow("Match!", img)
                cv2.waitKey()
                if cv2.waitKey(1) & 0xff == ord('q'):
                    break
