#!/usr/bin/env python
# coding: utf-8
from keras.datasets import cifar10
import numpy as np
np.random.seed(10)

# # 数据准备
(x_img_train,y_label_train),(x_img_test,y_label_test)=cifar10.load_data()

x_img_train_normalize = x_img_train.astype('float32') / 255.0
x_img_test_normalize = x_img_test.astype('float32') / 255.0

from keras.utils import np_utils
y_label_train_OneHot = np_utils.to_categorical(y_label_train)
y_label_test_OneHot = np_utils.to_categorical(y_label_test)

# # 建立模型
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D

model = Sequential()
#卷积层1
model.add(Conv2D(filters=32,kernel_size=(3,3),
                 input_shape=(32, 32,3), 
                 activation='relu', 
                 padding='same'))
model.add(Dropout(rate=0.25))
model.add(MaxPooling2D(pool_size=(2, 2)))

#卷积层2与池化层2
model.add(Conv2D(filters=64, kernel_size=(3, 3), 
                 activation='relu', padding='same'))
model.add(Dropout(0.25))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dropout(rate=0.25))
model.add(Dense(1024, activation='relu'))
model.add(Dropout(rate=0.25))

model.add(Dense(10, activation='softmax'))
print(model.summary())


# # 加载之前训练的模型
try:
    model.load_weights("./train/cifar.h5")
    print("加载模型成功!继续训练模型")
except :
    print("加载模型失败!开始训练一个新模型")
# 训练模型

model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])


train_history=model.fit(x_img_train_normalize, y_label_train_OneHot,
                        validation_split=0.2,
                        epochs=5, batch_size=128, verbose=1)

scores = model.evaluate(x_img_test_normalize,
                        y_label_test_OneHot, verbose=0)
print(scores[1])

#prediction=model.predict_classes(x_img_test_normalize)


model.save("./train/cifar.h5")
print("Saved model to disk")

# prediction[:10]

# label_dict={0:"airplane",1:"automobile",2:"bird",3:"cat",4:"deer",
#              5:"dog",6:"frog",7:"horse",8:"ship",9:"truck"}
#
#
# # # 查看预测概率
# Predicted_Probability=model.predict(x_img_test_normalize)


