# 原理 输入图像f（x,y）   设置中心坐标center（cx,cy）为缩放点
# 图像上任意一点到中心点的相对坐标tx= x-cx,ty=y-cy 哈哈镜效果分为图像拉伸放大和图像缩小
# 对于图像拉伸放大 设置图像变换的半径为radius 哈哈镜变换后的图像为p(x,y).
# x = (tx/2)*(sqrt(tx*tx + ty*ty)/radius)+cx
# y = (ty/2)*(sqrt(tx*tx + ty*ty)/radius)+cy
# 对于图像缩小，设置图像变换的半径为radius，哈哈镜变换后的图像为p(x,y)
# x = cos(atan2(ty,tx))*12*(sqrt(tx*tx + ty*ty)+cx
# y = sin(atan2(ty,tx))*12*(sqrt(tx*tx + ty*ty)+cy


import cv2
import numpy as np
import math

def MaxFrame(frame):
    height, width, n = frame.shape
    center_X = width / 2
    center_Y = height / 2
    radius = 600
    newX = 0
    newY = 0
    real_radius = int(radius / 2.0)
    new_data = frame.copy()

    for i in range(width):
        for j in range(height):
            tX = i - center_X
            tY = j - center_Y

            distance = tX * tX + tY * tY
            if distance < radius * radius :

                newX = int(tX/ 2.0)
                newY = int(tY/ 2.0)

                newX = int(newX * (math.sqrt(distance) / real_radius))
                newX = int(newX * (math.sqrt(distance) / real_radius))

                newX = int(newX + center_X)
                newY = int(newY + center_Y)
                if newX < width and newY < height:
                    new_data[j, i][0] = frame[newY, newX][0]
                    new_data[j, i][1] = frame[newY, newX][1]
                    new_data[j, i][2] = frame[newY, newX][2]

            else:
                new_data[j, i][0] = frame[newY, newX][0]
                new_data[j, i][1] = frame[newY, newX][1]
                new_data[j, i][2] = frame[newY, newX][2]
    return new_data

def MinFrame(frame):
    height, width, n = frame.shape
    center_X = width / 2
    center_Y = height / 2
    radius = 600
    newX = 0
    newY = 0
    real_rudius = int(radius / 2.0)
    new_data = frame.copy()

    for i in range(width):
        for j in range(height):
            tX = i - center_X
            tY = j - center_Y
            theta = math.atan2(tY,tX)
            radius = math.sqrt((tX*tX) + (tY * tY))

            newR = math.sqrt(radius) * 12
            newX = int(center_X + (newR * math.cos(theta)))
            newY = int(center_Y + (newR * math.sin(theta)))

            if newX < 0 and newX > width:
                newX = 0

            if newY < 0 and newX >height:
                newY = 0

            if newX <width and newY < height:
                new_data[j, i][0] = frame[newY, newX][0]
                new_data[j, i][1] = frame[newY, newX][1]
                new_data[j, i][2] = frame[newY, newX][2]

            else:
                new_data[j, i][0] = frame[j, i][0]
                new_data[j, i][1] = frame[j, i][1]
                new_data[j, i][2] = frame[j, i][2]
    return new_data

def main():
    img = cv2.imread("2.jpg")

    cv2.imshow("original", img)
    img2 = MaxFrame(img)
    cv2.imshow("enlarge", img2)
    img3 = MinFrame(img)
    cv2.imshow("ensmall", img3)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
