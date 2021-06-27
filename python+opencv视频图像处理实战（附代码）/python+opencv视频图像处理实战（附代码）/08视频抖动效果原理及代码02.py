#刚才演示了某一帧下的情况，现在设计每隔5帧进行图像的处理，然后将处理后的图像保存到一个视频里
import cv2
def img_shake(img):                #定义抖动函数
    height,width,n=img.shape
    h1=int(height*0.1)
    h2=int(height*0.9)
    w1 = int(width * 0.1)
    w2 = int(width * 0.9)
    img2=img[h1:h2,w1:w2]
    dst = cv2.resize(img2, (width, height))
    cv2.imshow("dst",dst)
    cv2.waitKey(0)
    return dst
def main():
    vc = cv2.VideoCapture('1.mp4')  # 读入视频文件
    c = 1
    cout=5
    fps = vc.get(cv2.CAP_PROP_FPS)    #读取视频的帧数
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')     #编码方式
    video_writer = cv2.VideoWriter("img_shake.mp4", fourcc, fps, (640, 480)) #输出视频格式、编码方式、窗口大小
    while vc.isOpened():  # 循环读取视频帧
        rval, frame = vc.read()
        if (c %5 ==0 or 0<cout<5):    #选择每5帧
            dst=img_shake(frame)     #调用抖动函数
            video_writer.write(dst)   #输出抖动后图片
            cout = cout - 1
        else:
            cout = 5
            cv2.imshow("dst", frame)  #显示抖动图片
            video_writer.write(frame)   #输出图片
            cv2.waitKey(0)
        c = c + 1
        cv2.waitKey(1)
    vc.release()
    print(fps,c)
if __name__ == '__main__':
    main()
