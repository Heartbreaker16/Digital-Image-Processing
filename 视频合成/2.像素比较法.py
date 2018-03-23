import cv2
origin = cv2.VideoCapture('origin.mp4')
sky = cv2.VideoCapture('sky.mp4')
light = cv2.VideoCapture('light.mp4')
# 获取背景像素G值
ret,first_frame = origin.read()
g = first_frame[1, 1, 1]
while origin.isOpened() & sky.isOpened() & light.isOpened():
    # 获取每一帧
    ret1, origin_frame = origin.read()
    ret2, sky_frame = sky.read()
    ret3, light_frame = light.read()
    # 遍历原视频的每一帧中的每个像素，将其中与背景像素相等的像素置为黑色
    for i in range(360):
        for j in range(640):
           if  (abs(origin_frame[i, j, 1] - g) < 5):
               origin_frame[i, j, 0] = 0
               origin_frame[i, j, 1] = 0
               origin_frame[i, j, 2] = 0
    # 为使前景覆盖背景而不是叠加在背景上，先将背景和前景的重合区域除去（置为黑色）
    dst = cv2.addWeighted(sky_frame, 1, origin_frame, -100, 0)
    # 视频合成
    dst1 = cv2.addWeighted(dst, 1, origin_frame, 1, 0)
    dst2 = cv2.addWeighted(dst1, 1, light_frame, 1, 0)
    # 输出合成后的帧
    cv2.imshow('frame', origin_frame)
    cv2.imshow('dst', dst)
    cv2.imshow('output', dst2)
    # ESC键退出
    if cv2.waitKey(1) & 0xFF == 27:
        break
# 关闭窗口
cv2.destroyAllWindows()