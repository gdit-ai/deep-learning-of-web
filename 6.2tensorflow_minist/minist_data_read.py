import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 获取数据,number 1 to 10
#自动下载minist数据，读进来
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
train_x, train_y = mnist.train.next_batch(100)
print(len(train_x[0]))
print(train_y)




