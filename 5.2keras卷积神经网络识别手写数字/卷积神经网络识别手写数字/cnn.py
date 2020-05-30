from keras.datasets import mnist
from keras.utils import np_utils
import numpy as np
np.random.seed(10)

(x_Train, y_Train) , (x_Test, y_Test) = mnist.load_data()

x_Train4D = x_Train.reshape(x_Train.shape[0], 28, 28,1).astype('float32')
x_Test4D = x_Test.reshape(x_Test.shape[0], 28, 28, 1).astype('float32')

x_Train4D_normalize = x_Train4D / 255
x_Test4D_normalize = x_Test4D / 255
y_TrainHot = np_utils.to_categorical(y_Train)
y_TestHot = np_utils.to_categorical(y_Test)

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

model = Sequential()
model.add(Conv2D(filters=16, kernel_size=(5,5), padding='same', input_shape = (28, 28, 1), activation='relu'))
# 参数说明
# filter = 16 建立16个滤镜
# kernel_size = (5,5) 每一个滤镜是5 × 5的大小
# padding = 'same' 设置卷积运算产生的图像大小不变
# input_shape = (28, 28, 1) 第一二维代表输入图像的形状是28 × 28，第三维因为是单色灰度图像，所以最后维数值是1
# activation设置激活函数为relu建立池化层1
model.add(MaxPooling2D(pool_size=(2,2)))
# 输入参数为pool_size=(2,2),执行第一次缩减采样，将16个28 ×28的图像缩小为16个14 × 14的图像建立卷积层2，将16个图像转化为36个图像，不改变图像大小，仍为14 × 14
model.add(Conv2D(filters=36, kernel_size=(5,5), padding='same', activation='relu'))
# 加入池化层2，并加入DropOut避免过拟合
model.add(MaxPooling2D(pool_size=(2,2)))
# 执行第二次缩减采样，将14 × 14图像转换为7 × 7图像
model.add(Dropout(0.25))
# 加入DropOut(0.25)，每次训练时，会在神经网络中随机放弃25%的神经元，避免过拟合建立神经网络（平坦层，隐藏层，输出层)建立平坦层
model.add(Flatten())
# 将之前步骤建立的池化层2，一共有36个7 × 7的图像转化为一维向量，长度是36 × 7 × 7 = 1764， 也就是1764个float数，对应1764个神经元建立隐藏层，一共128个神经元
model.add(Dense(128, activation='relu'))
# 把DropOut加入模型中，DropOut(0.5)在每次迭代时候会随机放弃50%的神经元，避免过拟合
model.add(Dropout(0.5))
# 建立输出层，一共10个单元，对应0-9一共10个数字。使用softmax进行激活
model.add(Dense(10, activation='softmax'))
# 查看模型摘要
print(model.summary())
# # 进行训练
# 定义训练方式
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 开始训练
train_history = model.fit(x = x_Train4D_normalize, y = y_TrainHot,
                          validation_split=0.2, epochs=10, batch_size=300, verbose=2)