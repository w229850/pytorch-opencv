# 怀旧风格照片形成原理： 怀旧风格的设计主要是在图像的颜色空间进行处理， 以BGR空间为例，对B/G/R这三个通道进行颜色处理
# 让图像有种泛黄的效果 设计公式：
# R = 0.393*r + 0.769*g + 0.189*b
# G = 0.349*r + 0.686*g + 0.168*b
# B = 0.272*r + 0.534*g + 0.131*b
# 其中r,g,b分别代表输入的原图某一点像素的BGR值，BGR代表了该点变换后的BGR，注意变换后的BGR值约束在0~255之间。
import cv2

def retro_style(img):                 #定义怀旧风格函数
    img2 = img.copy()                   #复制图像
    height, width, n = img.shape           #获得原图像的长宽和其通道
    for i in range(height):
        for j in range(width):    #循环获取各层的像素值，由于图像的实际图层是BGR排序，这里也用小写代替
            b = img[i, j][0]
            g = img[i, j][1]
            r = img[i, j][2]
                                                  #计算新图像的BGR值，B相当于加了0.272倍的r,0.534倍的g，和0.131倍的b
            B = int(0.272*r + 0.534*g + 0.131*b)
            G = int(0.349*r + 0.686*g + 0.168*b)
            R = int(0.393*r + 0.769*g + 0.189*b)
                                                   #最后进行阈值处理，防止有像素值不在0~255之间
            img2[i, j][0] = max(0,min(B,255))
            img2[i, j][1] = max(0,min(G,255))
            img2[i, j][2] = max(0,min(R,255))

    cv2.imshow("retroimg", img2)

def main():
    img = cv2.imread('2.jpg')
    retro_style(img)
    cv2.imshow("img", img)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()