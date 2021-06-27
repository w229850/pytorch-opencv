# 参考ps素描的实现步骤，先去色将彩色图像转换成灰度图，复制去色层 进行反色。
# 对反色图像进行高斯模糊，模糊后的图像叠加模式选择颜色减淡效果

import cv2
import numpy as np
def sketrch_style(img):
    heigt, width, n = img.shape
    gray0 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img2 = np.zeros((heigt, width), dtype = 'uint8')
    gray1 = cv2.addWeighted(gray0, -1, img2, 0, 255, 00)
    cv2.imshow("img0", gray1)
    gray1 = cv2.GaussianBlur(gray1,(15,15), 0)
    dst = cv2.addWeighted(gray0, 1, gray1, 1, 0)
    cv2.imshow("sketch_img", dst)

def main():
    img = cv2.imread('2.jpg')
    sketrch_style(img)
    cv2.imshow('img', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()