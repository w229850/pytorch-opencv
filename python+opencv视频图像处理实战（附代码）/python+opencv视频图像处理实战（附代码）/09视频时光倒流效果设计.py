import cv2
def main():
    vc = cv2.VideoCapture('2.mp4')  # 读入视频文件
    c = 1
    fps = vc.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video_writer = cv2.VideoWriter("Timereflux.mp4", fourcc, fps, (544, 720))
    while vc.isOpened():  # 循环读取视频帧
        rval, frame = vc.read()
        if c>=21 and c<=30:
            cv2.imwrite('image/' + str(30-c) + '.jpg', frame)  # 存储为图像
        c=c+1
    vc.release()
    # for i in range(0, 9):
    #     img = cv2.imread('image/%d'.jpg % i)
    #     video_writer.write(img)
if __name__ == '__main__':
    main()
