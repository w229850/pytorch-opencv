import cv2 as cv
import numpy as np

src = cv.imread('1.jpg')  #读取图片
cv.imshow("input image", src)    #显示原图片
face = src[250:450, 150:450]      #选择区域
gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)    #选择区域灰度化
backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)    #将gray转回BGR格式，因为下面图片合并需要通道数一样
src[250:450, 150:450] = backface   #合并图像
cv.imshow('face',src)    #显示图像
cv.waitKey(0)           #等待时间

def fill_color_demo(image):   #定于彩色填充图像函数
    copyImg = image.copy()    #拷贝出新图像
    h,w = image.shape[:2]     #获取长宽
    mask = np.zeros([h+2, w+2], np.uint8)   #创建mask大小,且必须是8位
    cv.floodFill(copyImg, mask, (30,30), (0, 255, 255), (50,50,50),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    #泛洪填充，第三个参数填充起始点，4重新填充像素值，5填充的最低像素范围 6填充的最高范围 7考虑当前像素与种子像素之差
    cv.imshow("fill_color_demo", copyImg)  #显示图片

src2 = cv.imread('1.jpg')
fill_color_demo(src2)
cv.waitKey(0)