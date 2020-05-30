# coding: utf-8
import base64
import numpy as np
import cv2

img_file = open(r'./static/1.jpg', 'rb')  # 二进制打开图片文件
img_b64encode = base64.b64encode(img_file.read())  # base64编码
img_file.close()  # 文件关闭
print(img_b64encode)
img_b64decode = base64.b64decode(img_b64encode)  # base64解码
print(img_b64decode)
img_array = np.fromstring(img_b64decode, np.uint8)  # 转换np序列
img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)  # 转换Opencv格式
cv2.imshow("img", img)
cv2.waitKey()