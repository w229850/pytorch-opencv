import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract as tess

src = cv.imread('13.jpg')  # 导入图片
cv.imshow('13.jpg',src)    #显示原图

def recognize_text(image):             # 自定义验证码检测函数
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)   #灰度化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  #二值化
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  #定义核方框
    result = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)   #形态学处理
    cv.imshow("binary_image",result)

    # cv.bitwise_not(result, result) 更改背景色
    textImage = Image.fromarray(result)                #将array转至image
    text = tess.image_to_string(textImage)             #将图片信息提取成文本
    print("识别结果：%s"%text)

recognize_text(src)
cv.waitKey(0)
