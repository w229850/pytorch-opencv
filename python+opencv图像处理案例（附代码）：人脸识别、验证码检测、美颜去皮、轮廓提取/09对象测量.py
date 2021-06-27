import cv2 as cv
import numpy as np

src = cv.imread('8.jpg')  #导入图片
cv.imshow('8.jpg',src)    #显示原图

def measure_object(image):          #定义测量函数
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)                    #图像灰度化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)  # 图像二值化 cv.THRESH_BINARY_INV是取反
    print("threshold value:%s"%ret)    #输出阈值
    cv.imshow("binary image", binary)  # 输出图像
    outImage, contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # 调用检测物体轮廓函数
    for i ,contour in enumerate(contours):
        area = cv.contourArea(contour)           #求取面积
        x, y, w, h = cv.boundingRect(contour)          #轮廓外接矩形
        mm = cv.moments(contour)                 #计算图像中心矩
        rate = min(w, h)/max(w, h)            #计算宽高比
        print('rectangle rate:%s'%rate)         #输出宽高比
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']          #找出轮廓的中心位置
        cv.circle(image, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)
        # 用个黄色小圆圈把几何图形的中心位置绘制出来， 第三个参数是半径，第四个参数是颜色
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        #用红色框框把外接矩形绘制出来
        print("contour area %s"%area)
    cv.imshow("detect contours", image)
measure_object(src)
cv.waitKey(0)