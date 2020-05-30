import cv2
from keras.models import load_model

img = cv2.imread("./pic/2.jpg")
print(img.shape)
grey_img = img
print(grey_img.shape)

shape_img= (grey_img.reshape(1, 28, 28, 3)).astype('float32')/255
print(shape_img.shape)


model = load_model('SaveModel/minist_model_graphic.h5')

prediction = model.predict_classes(shape_img)
print(prediction[0])