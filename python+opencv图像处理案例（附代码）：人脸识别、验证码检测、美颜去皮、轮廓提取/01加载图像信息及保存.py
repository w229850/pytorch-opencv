import cv2                 #导入opencv库

def get_image_info(image):     #定义加载图像信息函数
    print(type(image))         #读取该图片类别
    print(image.shape)         #加载图像的长宽和通道数
    print(image.size)          #加载图像的大小
    print(image.dtype)         #加载字节位数占多少

img = cv2.imread('1.jpg')    #读入图片
cv2.imshow('image', img)     #图片显示
get_image_info(img)          #调用加载图片信息函数
cv2.waitKey(0)     #等待时间

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #灰度化
cv2.imwrite('./2.jpg', gray)      #写出图片到当前文件夹下
cv2.waitKey(0)