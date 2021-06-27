import cv2 as cv
import numpy as np

src = cv.imread('11.jpg')  # 导入图片
cv.imshow('11.jpg',src)    #显示原图

def face_detect_demo(image):   #自定义人脸检测函数
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)    #灰度化
    face_detector = cv.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
    #调用级联检测器加载人脸检测数据
    faces = face_detector.detectMultiScale(gray, 1.02,5)
    #调用多尺度人脸检测，参数1输入灰度图，参数2尺度变化每次向上或向下移动多少倍，参数3检测程度
    for x,y,w,h in faces:
        cv.rectangle(image, (x,y), (x+w, y+h), (0, 0, 255), 2)
    cv.imshow('result', image)

face_detect_demo(src)
cv.waitKey(0)

# cv.destroyAllWindows()