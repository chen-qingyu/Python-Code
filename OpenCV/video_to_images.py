import cv2


cap = cv2.VideoCapture("test.mp4")  # 实例化一个视频对象
i = 0
while True:
    ret, frame = cap.read()  # 读取视频的每一帧
    if frame is None:  # 最后一帧读取完就退出
        break

    cv2.imshow('images', frame)  # 显示每一帧
    cv2.imwrite('./images/%04d.bmp' % i, cv2.resize(frame, (128, 64)))  # 调整大小为128x64后保存
    i += 1

    if cv2.waitKey(20) & 0xFF == ord(' '):  # 刷新周期为20ms，即FPS为50，可以按空格退出
        break
