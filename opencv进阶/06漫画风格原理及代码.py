#漫画风格原理：由于漫画风格的图片线条比较粗糙，保留了很多墨水绘制的线条，因此思路如下，
#将彩色图像转换成灰度图，边缘检测，对于检测的边缘增强并二值化加粗线条，最后与原图叠加得到最终效果。
import cv2

def main():
 img_rgb = cv2.imread("2.jpg")  #读取图片
 img_color = img_rgb
 img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)  #原图灰度化
 img_blur = cv2.medianBlur(img_gray, 7)           #进行中值滤波
 #检测到边缘并且增强其效果，adaptiveThreshold是Opencv自带的自适应阈值二值化函数
 img_edge = cv2.adaptiveThreshold(img_blur,255,
          cv2.ADAPTIVE_THRESH_MEAN_C,
          cv2.THRESH_BINARY,
          blockSize=9,
          C=2)
 #转换回彩色图像
 img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
 img_cartoon = cv2.bitwise_and(img_color, img_edge)   #最后经过二进制与操作将图像叠加
 # 保存转换后的图片
 cv2.imshow("out", img_cartoon)
 cv2.waitKey(0)
if __name__ == '__main__':
     main()
