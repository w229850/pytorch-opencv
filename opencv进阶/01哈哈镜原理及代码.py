#哈哈镜的原理：输入图像f(x,y), 设置图像中心坐标Center(cx, xy)为缩放中心点。
#图像上任意一点到中心点的相对坐标tx= x-cx,ty=y-cy.哈哈镜效果分为图像拉伸放大和图像缩小。
#对于图像拉伸放大，设置图像变换的半径为radius,哈哈镜变换后的图像为p(x,y).
# x = (tx/2)*(sqrt(tx*tx + ty*ty)/radius)+cx
# y = (ty/2)*(sqrt(tx*tx + ty*ty)/radius)+cy
#对于图像缩小，设置图像变换的半径为radius,哈哈镜变换后的图像为p(x,y).
# x = cos(atan2(ty , tx))* 12*(sqrt(tx*tx + ty*ty))+cx
# y = sin(atan2(ty , tx))* 12*(sqrt(tx*tx + ty*ty))+cy

# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import math

def MaxFrame(frame):                 #定义图像拉伸放大函数
    height, width, n = frame.shape    #获取输入图像的长宽和通道
    center_X = width / 2              #计算公式
    center_Y = height / 2
    radius = 400                     #这里直接定义半径了
    newX = 0                         #初始变换后的坐标
    newY = 0
    real_radius =int(radius / 2.0)   #计算公式
    new_data = frame.copy()         #复制一个与原图像一样的图片

    for i in range(width):                #建立循环移动像素遍历宽度方向的像素
        for j in range(height):               #遍历高度方向的像素
            tX = i - center_X                  #计算公式
            tY = j - center_Y

            distance = tX * tX + tY * tY
            if distance < radius * radius:    #变换点的距离是否太远

                newX = int(tX/ 2.0)
                newY = int(tY/ 2.0)

                newX = int(newX * (math.sqrt(distance) / real_radius))
                newX = int(newX * (math.sqrt(distance)/ real_radius))

                newX = int(newX + center_X)
                newY = int(newY + center_Y)
                if newX<width and newY<height:            #计算出的新坐标可能超出原图层，这里用if加以判断
                    new_data[j, i][0] = frame[newY, newX][0]        #将计算后的坐标移动到原坐标
                    new_data[j, i][1] = frame[newY, newX][1]
                    new_data[j, i][2] = frame[newY, newX][2]

            else:                                          #若变换点距离太远，图像像素不变动
                new_data[j, i][0] = frame[j, i][0]
                new_data[j, i][1] = frame[j, i][1]
                new_data[j, i][2] = frame[j, i][2]

    return new_data

def MinFrame(frame):                  #定义图像缩小函数
    height, width, n = frame.shape
    center_X = width / 2
    center_Y = height / 2
    radius = 400
    newX = 0
    newY = 0
    real_radius =int(radius / 2.0)
    new_data = frame.copy()

    for i in range(width):
        for j in range(height):
            tX = i - center_X
            tY = j - center_Y
            theta = math.atan2(tY, tX)
            radius = math.sqrt((tX * tX) + (tY * tY))             #与上面一样，计算公式不一样

            newR = math.sqrt(radius) *12
            newX = int(center_X + (newR * math.cos(theta)))
            newY = int(center_Y + (newR * math.sin(theta)))

            if newX < 0 and  newX >width:
                newX = 0

            if newY <0 and newY >height:
                newY = 0

            if newX<width and newY<height:
                new_data[j, i][0] = frame[newY, newX][0]
                new_data[j, i][1] = frame[newY, newX][1]
                new_data[j, i][2] = frame[newY, newX][2]

            else:
                new_data[j, i][0] = frame[j, i][0]
                new_data[j, i][1] = frame[j, i][1]
                new_data[j, i][2] = frame[j, i][2]

    return new_data

def main():                                 #调用主函数
    img = cv2.imread("1.jpg")                #输入图片

    cv2.imshow("original", img)           #输出原始图片
    img2=MaxFrame(img)
    cv2.imshow("enlarge", img2)           #输出拉伸放大后的图片
    img3 = MinFrame(img)
    cv2.imshow("ensmall", img3)           #输出缩小后的图片
    cv2.waitKey(0)                        #设置等待时间为零


if __name__ == '__main__':
    main()



