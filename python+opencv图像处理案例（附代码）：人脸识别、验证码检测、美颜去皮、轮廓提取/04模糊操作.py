import cv2 as cv
import numpy as np

src = cv.imread('1.jpg')  #导入图片
cv.imshow('1.jpg',src)    #显示原图


def blur_demo(image):  #定义模糊函数
    dst = cv.blur(image,(15,15))    #水平和垂直方向各模糊15个单位
    cv.imshow('blur_image',dst)

def custom_blur_demo(image):   #自定义图片卷积处理函数
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)    #定义3×3的卷积核
    dst = cv.filter2D(image, -1, kernel=kernel)  #调用卷积函数，第一个参数原图片，第二参数目标图像所需深度，第三参数卷积核
    cv.imshow('custom_blur_demo',dst)          #显示卷积后图像，卷积核的数不同效果不同，这里是锐化

blur_demo(src)   #调用模糊函数
custom_blur_demo(src)
cv.waitKey(0)