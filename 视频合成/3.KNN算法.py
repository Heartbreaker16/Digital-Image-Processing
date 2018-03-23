import cv2
camera = cv2.VideoCapture('origin.mp4')
camera1 = cv2.VideoCapture('sky.mp4')
camera2 = cv2.VideoCapture('light.mp4')
history = 10    # 训练帧数
bs = cv2.createBackgroundSubtractorKNN(detectShadows=True)  # 背景减除器，设置阴影检测
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
    th = cv2.threshold(fg_mask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
    th = cv2.erode(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1)), iterations=2)
    dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)), iterations=2)
    res = cv2.bitwise_and(frame, frame, mask=dilated)
    # 为使前景覆盖背景而不是叠加在背景上，先将背景和前景的重合区域除去（置为黑色）
    dst = cv2.addWeighted(frame1, 1, res, -20, 0)
    # 视频合成
    dst1 = cv2.addWeighted(dst, 1, res, 1, 0)
    dst2 = cv2.addWeighted(dst1, 1, frame2, 1, 0)
    cv2.imshow("input", fg_mask)
    cv2.imshow("mask", dilated)
    cv2.imshow("output", dst2)
    if cv2.waitKey(5) & 0xff == 27:
        break
camera.release()

