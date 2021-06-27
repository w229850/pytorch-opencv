import cv2

vc = cv2.VideoCapture('test.avi')  # 读入视频文件
c = 1
if vc.isOpened():  # 判断是否正常打开，将视频读取出来
    rval, frame = vc.read()   #第一个值表示True or False 有无读入内容，第二个值获取读入帧
else:
    rval = False
timeF = 100  # 视频帧计数间隔频率
while rval:  # 循环读取视频帧
    rval, frame = vc.read()
    if (c % timeF == 0):  # 每隔timeF帧进行存储操作
        cv2.imwrite(str(c) + '.jpg', frame)  # 存储为图像
    c = c + 1
    cv2.waitKey(1)
vc.release()


