import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

src = cv.imread('1.jpg')  #导入图片
cv.imshow('1.jpg',src)    #显示原图

def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])  # image.ravel()是将多维数组降为一维数组，256为bins数量，[0, 256]为范围,计算像素个数
    plt.show()


def image_hist(image):
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        # 计算出直方图，calcHist(images, channels, mask, histSize(有多少个bin), ranges[, hist[, accumulate]]) -> hist
        # hist 是一个 256x1 的数组，每一个值代表了与该灰度值对应的像素点数目。
        hist = cv.calcHist(image, [i], None, [256], [0, 256])
        print(hist.shape)
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()

image_hist(src)
plot_demo(src)
cv.waitKey(0)