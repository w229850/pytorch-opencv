import cv2 as cv
import numpy as np

src = cv.imread('5.jpg')  #导入图片
cv.imshow('5.jpg',src)    #显示原图

def bi_demo(image):     #定义滤波函数
    dst = cv.bilateralFilter(image,0,100, 15)
#调用双边滤波函数，第一个参数原图，第二个参数每个像素直径范围，第三个参数融合周边像素颜色，第四个参数相似颜色像素相互影响
    cv.imshow('bi_demo', dst)  #输出滤波后图像

bi_demo(src)
cv.waitKey(0)

