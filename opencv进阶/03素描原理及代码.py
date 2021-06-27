#参考PS素描的实现步骤，先去色将彩色图像装换成灰度图，复制去色层进行反色，
# 对反色图像进行高斯模糊，模糊后的图像叠加模式选择颜色减淡效果
import cv2
import numpy as np
def sketch_style(img):                   #自定义素描函数
    height,width,n = img.shape            #提取原图的长宽和通道
    gray0 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)          #灰度处理
    img2 = np.zeros((height,width),dtype='uint8')         #创建一张像素值都为0的图像。类型为unit8即像素点的范围是0~255
    #addWeighted各参数含义，1参数表示输入图，2表示第一张的透明度，3是第二张图，4是第二张透明度，5是像素点和之后再加数值
    gray1 = cv2.addWeighted(gray0, -1, img2, 0, 255, 0)     #像素值为0的图像与灰度图像进行叠加
    cv2.imshow("img0", gray1)                            #输出图像
    gray1 = cv2.GaussianBlur(gray1, (15, 15), 0)         #高斯模糊
    dst = cv2.addWeighted(gray0, 1, gray1, 1, 0)     #滤波后的图像叠加
    cv2.imshow("sketch_img", dst)              #输出图像
def main():
    img = cv2.imread('1.jpg')
    sketch_style(img)
    cv2.imshow('img', img)
    cv2.waitKey(0)
if __name__ == '__main__':
    main()