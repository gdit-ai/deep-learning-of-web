from keras.datasets import mnist
import cv2
(x_Train, y_Train) , (x_Test, y_Test) = mnist.load_data()

print(x_Train.shape)
print(y_Train.shape)
print(x_Test.shape)
print(y_Test.shape)
for num in range(20):
    name = './pic/' + str(num) + '.jpg'
    cv2.imwrite(name, x_Train[num])

f = open("train_label.txt","w")
for num in range(20):
    label = y_Train[num]
    f.write(str(label))
    f.write("\n")

