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

model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(filters=36, kernel_size=(5,5), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))
# 查看模型摘要
print(model.summary())
# # 进行训练
# 定义训练方式
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 开始训练
train_history = model.fit(x = x_Train4D_normalize, y = y_TrainHot,
                          validation_split=0.2, epochs=10, batch_size=300, verbose=2)

# model.save_weights("SaveModel/minist_model.h5")
model.save("SaveModel/minist_model_graphic.h5")