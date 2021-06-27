import cv2 as cv

def add_demo(m1, m2):   #定义像素相加函数
    dst = cv.add(m1, m2)     #对像素进行加法运算
    cv.imshow("add_demo", dst)   #显示像素相加后的图像

def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo",dst)

scr1 = cv.imread("3.jpg")    #读入当前文件夹下名称为3.jpg图片
scr2 = cv.imread("4.jpg")    #读入4.jpg图片
print(scr1.shape)   #显示图片3的大小
print(scr2.shape)   #显示图片4的大小 进行像素加减乘除需要两个图片格式大小一样
cv.imshow("image1",scr1)    #显示原图3
cv.imshow("image2",scr2)    #显示原图4

add_demo(scr1, scr2)   #调用加法运算
subtract_demo(scr1, scr2)   #调用减法运算
cv.waitKey(0)

