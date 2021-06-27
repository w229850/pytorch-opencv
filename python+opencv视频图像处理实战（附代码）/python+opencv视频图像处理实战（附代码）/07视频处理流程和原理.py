import cv2

cv2.namedWindow('Video')         # 创建显示视频的窗口
video_capture = cv2.VideoCapture(0)        # 打开摄像头
# 创建视频写入对象，创建一个视频对象AVI格式，第二个参数为编码格式，3获取帧率，4宽度，5高度
video_writer = cv2.VideoWriter('test.avi',
                               cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                               video_capture.get(cv2.CAP_PROP_FPS),
                               (int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))))
# 读取视频帧，对视频帧进行高斯模糊，然后写入文件并在窗口显示
success, frame = video_capture.read()
while success and not cv2.waitKey(1) == 27:
    blur_frame = cv2.GaussianBlur(frame, (3, 3), 0)
    video_writer.write(blur_frame)
    cv2.imshow("Video", blur_frame)
    success, frame = video_capture.read()
# 回收资源
cv2.destroyWindow('Video')
video_capture.release()
