#读取一个5秒的视频，定义一个抖动函数处理抖动中的图像，得到图像的中心Center,
#然后将图像按比例裁剪20%之后再放大至原图
import cv2
def img_shake(img):           #定义抖动函数
    height,width,n=img.shape         #获取原图的长宽和通道数
    h1=int(height*0.1)               #裁剪掉20%
    h2=int(height*0.9)
    w1 = int(width * 0.1)
    w2 = int(width * 0.9)
    img2=img[h1:h2,w1:w2]
    dst = cv2.resize(img2, (width, height))   #将裁剪后的图恢复到原图大小
    cv2.imshow("src",img)         #显示图片
    cv2.imshow("dst",dst)
    cv2.waitKey(0)
def main():
    vc = cv2.VideoCapture('1.mp4')  # 读入视频文件
    c = 1
    fps = vc.get(cv2.CAP_PROP_FPS)       #获取视频的帧率
    while vc.isOpened():  # 循环读取视频每帧图片
        rval, frame = vc.read()
        if (c == 2):
            img_shake(frame)       #将偶数帧数进行抖动函数处理
        c = c + 1
        cv2.waitKey(1)
    vc.release()
    print(fps,c)
if __name__ == '__main__':
    main()
