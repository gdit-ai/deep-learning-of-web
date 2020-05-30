from keras.utils import np_utils
import numpy as np
from PIL import Image
img_list = []
for num in range(5000):
    name = './pic/' + str(num) + '.png'
    #print(name)
    img_pil = Image.open(name)
    img_array = np.array(img_pil)
    #print(img_array.shape)
    img_list.append(img_array)
img_list_np = np.array(img_list)
print(img_list_np.shape)


filename = "dig_label.txt"
file = open(filename)
label_list = []
for line in file.readlines():
    new_line = line.strip()
    token = new_line.split(" ")
    label_list.append(token[1])

label_list_np = np.array(label_list)
print(label_list_np)
print(label_list_np.shape)
slice_img = img_list_np[:,:,:,0:1]
print(slice_img.shape)
x_train_image = slice_img
y_train_label = label_list_np
x_test_image = x_train_image
y_test_label = y_train_label
#60000x28x28
x_Train = x_train_image.reshape(5000, 400).astype('float32')
x_Test = x_test_image.reshape(5000, 400).astype('float32')
x_Train_normalize = x_Train / 255
x_Test_normalize = x_Test / 255

y_Train_OneHot = np_utils.to_categorical(y_train_label)
y_Test_OneHot = np_utils.to_categorical(y_test_label)

from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(units=256,
                input_dim=400,
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


