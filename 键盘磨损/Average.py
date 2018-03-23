import cv2
import matplotlib.pyplot as plt

#获取一幅图像的每行像素平均值
def getdiff(img):
    #定义边长
    Sidelength=500
    #缩放图像
    img=cv2.resize(img,(Sidelength,Sidelength),interpolation=cv2.INTER_CUBIC)
    #灰度处理
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #avglist列表保存每行像素平均值
    avglist=[]
    #计算每行均值，保存到avglist列表
    for i in range(Sidelength):
        avg=sum(gray[i])/len(gray[i])
        avglist.append(avg)
    return avglist

# 计算两个图像曲线的差值的方差
def getss(list1,list2):
    newlist = []
    # 计算两个图像每行像素的均值的差，存入newlist
    for i in range(len(list1)):
        avg = list1[i]-list2[i]
        newlist.append(avg)
    # 计算像素均值差的平均值avg
    avg = sum(newlist)/len(newlist)
    # 计算像素均值差的方差ss
    ss = 0
    for i in newlist:
        ss += (i-avg)*(i-avg)/len(newlist)
    return str(ss)

#显示两张图片的各行的像素均值曲线图，横坐标代表行数，纵坐标代表均值大小，表头显示像素均值差的方差
def show(path1,path2,num):
    plt.figure('Button '+str(num))
    plt.plot(range(500),getdiff(cv2.imread(path1)),marker="",label="abrased")
    plt.plot(range(500),getdiff(cv2.imread(path2)),marker="",label="non-abrased")
    plt.title(getss(getdiff(cv2.imread(path1)),getdiff(cv2.imread(path2))))
    plt.legend()
    plt.show()

show(r'Sample/5d.jpg',r'Sample/5u.jpg',5)
show(r'Sample/6d.jpg',r'Sample/6u.jpg',6)
show(r'Sample/7d.jpg',r'Sample/7u.jpg',7)
show(r'Sample/9d.jpg',r'Sample/9u.jpg',9)