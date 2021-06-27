import cv2 as cv
import numpy as np

src = cv.imread('7.jpg')
cv.imshow('7.jpg',src)

def measure_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshold value:%s"%ret)
    cv.imshow("binary image", binary)
    dst = cv.cvtColor(binary,cv.COLOR_GRAY2BGR)    #'''还原三通道图片'''
    outImage, contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for i ,contour in enumerate(contours):
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)
        mm = cv.moments(contour)
        rate = min(w, h)/max(w, h)
        print('rectangle rate:%s'%rate)
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        cv.circle(dst, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)

        approxCurve = cv.approxPolyDP(contour,4,True)
        #'''调用固定边数精度函数 第二参数指定原始曲线与近似曲线之间最大距离精度 第三参数近似曲线闭合'''
        print(approxCurve.shape)
        if approxCurve.shape[0] > 4:     # '''判断图形边数是否大于4'''
            cv.drawContours(dst, contours, i, (0,255,0),2)   #'''将符合要求的用绿色轮廓输出'''

        print("contour area %s"%area)
    cv.imshow("detect contours", dst)
measure_object(src)
cv.waitKey(0)