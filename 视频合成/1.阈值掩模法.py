import cv2
import numpy as np
# 加载视频合成素材
origin = cv2.VideoCapture('origin.mp4')
sky = cv2.VideoCapture('sky.mp4')
light = cv2.VideoCapture('light.mp4')
while origin.isOpened() & sky.isOpened() & light.isOpened():
# 获取每一帧
    ret1, origin_frame = origin.read()
    ret2, sky_frame = sky.read()
    ret3, light_frame = light.read()
# 原视频画面转换到HSV
    hsv = cv2.cvtColor(origin_frame,cv2.COLOR_BGR2HSV)
# 设定绿色的阈值
    lower_green = np.array([50, 43, 46])
    upper_green = np.array([70, 255, 255])
# 根据阈值构建掩模
    mask = cv2.inRange(hsv,lower_green,upper_green)
# 对原图像和掩模进行位运算,去除绿色背景
    res = cv2.bitwise_and(origin_frame,origin_frame,mask=~mask)
# 为使前景覆盖背景而不是叠加在背景上，先将背景和前景的重合区域除去（置为黑色）
    dst = cv2.addWeighted(sky_frame, 1, res, -20, 0)
# 视频合成
    dst1 = cv2.addWeighted(dst, 1, res, 1, 0)
    dst2 = cv2.addWeighted(dst1, 1, light_frame, 1, 0)
# 显示视频每一帧（包括掩模和原视频）
    cv2.imshow('frame',dst)
    cv2.imshow('res',res)
    cv2.imshow('mask',~mask)
    cv2.imshow('output',dst2)
# ESC键退出
    if cv2.waitKey(10)&0xFF == 27:
         break
# 关闭窗口
cv2.destroyAllWindows()


