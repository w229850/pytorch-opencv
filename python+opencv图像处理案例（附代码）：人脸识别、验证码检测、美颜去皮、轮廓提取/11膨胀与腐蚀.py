import cv2 as cv
import numpy as np

src = cv.imread('9.jpg')  #导入图片
cv.imshow('9.jpg',src)    #显示原图

def erode_demo(image):                    #定义腐蚀函数
    print(image.shape)                    #显示图片格式
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)    #图像灰度化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  #二值化
    cv.imshow("binary",binary)        #显示二值化后的图片
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(8,8))
    #建立指定结构 第一个参数定义形状，这里是方形，第二个参数指定程度
    dst = cv.erode(binary,kernel)          #腐蚀
    cv.imshow("erode_demo", dst)          #输出图像

def erode_dilate(image):          #定义膨胀函数
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(8,8))
    dst = cv.dilate(binary,kernel)              #膨胀
    cv.imshow("erode_dilate", dst)

erode_dilate(src)
erode_demo(src)
cv.waitKey(0)