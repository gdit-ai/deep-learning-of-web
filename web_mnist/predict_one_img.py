import cv2
from keras.models import load_model

img = cv2.imread("./pic/0.jpg")
print(img.shape)
grey_img = img[:,:,0:1]
print(grey_img.shape)
shape_img= (grey_img.reshape(1, 28, 28, 1)).astype('float32')/255

# model = load_model('SaveModel/minist_model.h5')  #选取自己的.h模型名称
model = load_model('SaveModel/minist_model_graphic.h5')  #选取自己的.h模型名称
prediction = model.predict_classes(shape_img)
print(prediction[0])

