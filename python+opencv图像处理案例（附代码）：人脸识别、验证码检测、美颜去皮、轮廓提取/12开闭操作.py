#先腐蚀再膨胀就是开操作，先膨胀再腐蚀就是闭操作
import cv2 as cv
import numpy as np

src = cv.imread('10.jpg')  #导入图片
cv.imshow('10.jpg',src)    #显示原图

def open_demo(image):                           #自定义开操作函数
    print(image.shape)                             #显示图片格式
    gray =  cv.cvtColor(image, cv.COLOR_BGR2GRAY)    #图像灰度化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 二值化
    cv.imshow("binary", binary)  # 显示二值化后的图片
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (6, 6))
    # 建立指定结构 第一个参数定义形状，这里是方形，第二个参数指定程度
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN,kernel)
    #进行形态学操作，参数1传入图片，参数2进行开运算，参数3表示方框大小
    cv.imshow('open-result',binary)

def close_demo(image):                           #自定义闭操作函数
    print(image.shape)                             #显示图片格式
    gray =  cv.cvtColor(image, cv.COLOR_BGR2GRAY)    #图像灰度化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 二值化
    cv.imshow("binary", binary)  # 显示二值化后的图片
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (10, 10))
    # 建立指定结构 第一个参数定义形状，这里是方形，第二个参数指定程度
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE,kernel)   #参数2改成闭操作运算
    cv.imshow('close-result',binary)


open_demo(src)
close_demo(src)
cv.waitKey(0)