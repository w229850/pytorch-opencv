import cv2 as cv
import numpy as np

src = cv.imread('6.jpg')  #导入图片
cv.imshow('6.jpg',src)    #显示原图
def contours_demo(image):                 #定义轮廓发现函数
    dst = cv.GaussianBlur(image, (3,3),0)    #调用高斯模糊，第二个参数内核大小，第三个参数高斯核标准偏差
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)              #图像灰度化
    ret,binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY| cv.THRESH_OTSU)   #图像二值化
    cv.imshow("binary image", binary) #输出图像

    clongImage,contours,heriachy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    #调用检测物体轮廓函数，第一个参数寻找轮廓的图像，第二个参数表示轮廓的检索模式，有 cv2.RETR_EXTERNAL表示只检测外轮廓
    # cv2.RETR_LIST检测的轮廓不建立等级关系 cv2.RETR_CCOMP建立两个等级的轮廓cv2.RETR_TREE建立一个等级树结构的轮廓。
    #第三个参数为轮廓的近似办法，cv2.CHAIN_APPROX_SIMPLE压缩各方向的元素
    #最后返回图像、轮廓信息、层次信息
    for i ,contour in enumerate(contours):
        cv.drawContours(image,contours,i,(0,0,255),2)
        #第一个参数指在哪幅图上绘制轮廓信息，第二个参数是轮廓本身，第三个参数是指定绘制哪条轮廓
        #第四个参数是绘图的颜色，第五个参数是绘制的线宽 输入-1则表示填充
        print(i)
    cv.imshow("detect contours",image)

contours_demo(src)
cv.waitKey(0)