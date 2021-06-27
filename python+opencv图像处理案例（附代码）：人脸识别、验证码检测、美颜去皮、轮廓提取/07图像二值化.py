import cv2 as cv
import numpy as np

src = cv.imread('1.jpg')  #导入图片
cv.imshow('1.jpg',src)    #显示原图

def threshold_demo(image):                          #定义二值化函数
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)            #图片灰度化处理
    ret,binary = cv.threshold(gray, 0, 255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    #调用二值化函数 第一个参数为输入图像，第二参数为进行分类的像素，第三个参数表示阈值，第四参数表示运算方法
    print("threshold value %s"%ret)     #输出划分像素点
    cv.imshow("binary",binary)           #显示图像

threshold_demo(src)
cv.waitKey(0)