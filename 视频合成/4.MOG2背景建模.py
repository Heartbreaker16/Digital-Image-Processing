import cv2
camera = cv2.VideoCapture('origin.mp4')
camera1 = cv2.VideoCapture('sky.mp4')
camera2 = cv2.VideoCapture('light.mp4')
history = 1    # 训练帧数
bs = cv2.createBackgroundSubtractorMOG2(history=history, detectShadows=True)
bs.setHistory(history)
frames = 0
while True:
    res, frame = camera.read()
    res2, frame1 = camera1.read()
    res3, frame2 = camera2.read()
    if not res:
         break
    fg_mask = bs.apply(frame)   # 获取 foreground mask
    if frames < history:
        frames += 1
        continue
    # 对原始帧进行膨胀去噪
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
    dilated = cv2.dilate(fg_mask, element)
    res = cv2.bitwise_and(frame, frame, mask=dilated)
    # 为使前景覆盖背景而不是叠加在背景上，先将背景和前景的重合区域除去（置为黑色）
    dst = cv2.addWeighted(frame1, 1, res, -20, 0)
    # 视频合成
    dst1 = cv2.addWeighted(dst, 1, res, 1, 0)
    dst2 = cv2.addWeighted(dst1, 1, frame2, 1, 0)
    cv2.imshow("input", fg_mask)
    cv2.imshow("mask", dilated)
    cv2.imshow("output", dst2)
    if cv2.waitKey(10) & 0xff == 27:
        break
camera.release()

