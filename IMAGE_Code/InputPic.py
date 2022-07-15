from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
img=Image.open("/Users/wt/Downloads/1.jpeg")
print((img.mode))
img1=img.convert('RGBA')
'''
'1': 表示黑白模式照片
'L': 表示灰度模式照片
'RGB': 表示RGB通道模式的彩色照片
'RGBA': 表示RGB通道及Alpha通道的照片
'''
img.crop((20,20,20,100)) #裁剪
img1.show()
print((img1.mode))




# opencv中cv2.imread读入的是BGR通道顺序
# flags=0是灰度模式，flags=1是默认的彩色模式
# im = cv2.imread('xxxx.png', flags=0) # 读取图像array对象、
im = cv2.imread('/Users/wt/Downloads/1.png', flags=cv2.IMREAD_GRAYSCALE)
cv2.imwrite('/Users/wt/Downloads/1.png', im)
plt.imshow(im) # 显示图片
# plt.show()
# plt.close()
# cv2.imshow('im', im)  # 显示图片

# 标准转换
def PILImageToCV(imagePath):
    # PIL Image转换成OpenCV格式
    img = Image.open(imagePath)
    plt.imshow(img)
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    plt.imshow(img)
    plt.show()


def CVImageToPIL(imagePath):
    # OpenCV图片转换为PIL image
    img = cv2.imread(imagePath)
    plt.imshow(img)
    img2 = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.imshow(img2)
    plt.show()