#!/usr/bin/env python
# coding: utf-8
from keras.utils import np_utils
import numpy as np
import os
np.random.seed(10)
from keras.datasets import mnist
(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()

#60000x28x28
#转变成二维转为一维向量
x_Train = x_train_image.reshape(60000, 784).astype('float32')
x_Test = x_test_image.reshape(10000, 784).astype('float32')
x_Train_normalize = x_Train / 255
x_Test_normalize = x_Test / 255

y_Train_OneHot = np_utils.to_categorical(y_train_label)
y_Test_OneHot = np_utils.to_categorical(y_test_label)

from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(units=256,
                input_dim=784,
                kernel_initializer='normal',
                activation='relu'))

model.add(Dense(units=10,
                kernel_initializer='normal',
                activation='softmax'))
print(model.summary())

# # 训练模型
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])

train_history = model.fit(x=x_Train_normalize,
                          y=y_Train_OneHot, validation_split = 0.2,
                        epochs = 10, batch_size = 200, verbose = 2)

scores = model.evaluate(x_Test_normalize, y_Test_OneHot)
print('accuracy=', scores[1])
prediction = model.predict_classes(x_Test)
print(prediction)


