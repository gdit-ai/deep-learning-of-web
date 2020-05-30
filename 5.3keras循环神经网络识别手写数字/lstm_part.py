import keras
from keras.layers import LSTM
from keras.layers import Dense, Activation
from keras.datasets import mnist
from keras.models import Sequential
from keras.optimizers import Adam

learning_rate = 0.001


display_step = 10


n_classes = 10

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
n_input = 28
n_step = 28
n_hidden = 128


x_train = x_train.reshape(-1, n_step, n_input)
print(x_train.shape)
x_train = x_train.reshape(-1, n_step, n_input)
x_test = x_test.reshape(-1, n_step, n_input)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

y_train = keras.utils.to_categorical(y_train, n_classes)
y_test = keras.utils.to_categorical(y_test, n_classes)

model = Sequential()
#LSTM输入数据维度，n_step时序的维度，n_hidden表示输出数据维度
model.add(LSTM(n_hidden, batch_input_shape=(None, n_step, n_input),
               unroll=True))
model.add(Dense(10))

model.summary()

#每次更新参数的变化快慢 = 梯度 * 学习率
learning_rate = 0.001
adam = Adam(lr=learning_rate)
model.compile(optimizer=adam,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

batch_size = 128 #一次性读进的图片张数
training_iters = 5 #训练数据集的次数
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=training_iters,
          verbose=1,
          validation_data=(x_test, y_test))

scores = model.evaluate(x_test, y_test, verbose=0)
print('LSTM test score:', scores[0])
print('LSTM test accuracy:', scores[1])

