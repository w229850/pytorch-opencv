#马赛克原理：马赛克效果其实就是将图像分成大小一致的图像块，每一个图像块都是一个正方形，并且正方形中所有像素值都相等。

from skimage import img_as_float
import matplotlib.pyplot as plt
from skimage import io
import random
import numpy as np

file_name='2.jpg'
img=io.imread(file_name)      #导入图像
img = img_as_float(img)       #将图像转至float类型，范围在【-1,1】或【0,1】之间
img_out = img.copy()             #复制原图
row, col, channel = img.shape       #获得原图的长宽和通道数
half_patch =10      #设置马赛克的大小
for i in range(half_patch, row-1-half_patch, half_patch):
    #对马赛克滑块移动时图像内部像素进行处理，起始点为10，终点为图像长减10，步长为10
  for j in range (half_patch, col-1-half_patch, half_patch):
    k1 = random.random() - 0.5            #生成-0.5到0.5之间的随机数
    k2 = random.random() - 0.5
    m=np.floor(k1*(half_patch*2 + 1))     #生成-10到10之间的随机数，floor是向下取整
    n=np.floor(k2*(half_patch*2 + 1))
    h=int((i+m) % row)                  #获取高度方向上的单位长度
    w=int((j+n) % col)                  #获取宽度方向上的单位长度
    img_out[i-half_patch:i+half_patch, j-half_patch:j+half_patch, :] =img[h, w, :] #输出马赛克图像，在每个方框内的像素值变为一样
plt.figure(1)       #创建窗口
plt.imshow(img)     #显示原图
plt.axis('off')      #关闭坐标轴
plt.figure(2)        #创建窗口2
plt.imshow(img_out)   #显示马赛克图
plt.axis('off')       #关闭坐标轴
plt.show()          #图像显示