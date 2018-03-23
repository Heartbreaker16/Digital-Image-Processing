import cv2

# 通过计算灰度值之差来比较两幅图像相似度
def getdiff(img1,img2):
    # 定义边长
    Sidelength=300
    # 缩放图像
    img1 = cv2.resize(img1, (Sidelength, Sidelength), interpolation=cv2.INTER_CUBIC)
    img2 = cv2.resize(img2, (Sidelength, Sidelength), interpolation=cv2.INTER_CUBIC)
    avg1 = avg2 = 0
    # 计算像素灰度值总和
    for i in range(Sidelength):
        avg1 += sum(img1[i])
        avg2 += sum(img2[i])
    # 计算像素灰度值总差值
    return abs(avg1-avg2)

# 对图像先高斯滤波再Otsu二值化
def Otsu(path):
    img = cv2.imread(path,0)
    blur = cv2.GaussianBlur(img,(5, 5),0)
    ret, th = cv2.threshold(blur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return th

print('按键5的磨损程度：', getdiff(Otsu(r"Otsu\5u.jpg"), Otsu(r"Otsu\5d.jpg")))
print('按键6的磨损程度：', getdiff(Otsu(r"Otsu\6u.jpg"), Otsu(r"Otsu\6d.jpg")))
print('按键7的磨损程度：', getdiff(Otsu(r"Otsu\7u.jpg"), Otsu(r"Otsu\7d.jpg")))
print('按键9的磨损程度：', getdiff(Otsu(r"Otsu\9u.jpg"), Otsu(r"Otsu\9d.jpg")))
print('注：数值越大，磨损程度越大')

