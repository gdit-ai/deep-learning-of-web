import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
#自动下载minist数据，读进来。
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
#定义对应数据占位 [1,784]
#定义对应标签占位 [1,10]
xs = tf.placeholder(tf.float32, [None, 784])  # 28x28
ys = tf.placeholder(tf.float32, [None, 10])
#定义全连接所需要的权重参数矩阵
#每一个神经元定义一个偏置
w = tf.Variable(tf.random_normal([784, 10]), name='W')
b = tf.Variable(tf.zeros([1, 10]) + 0.1, name='b')
#out = xs * w + b
#输入与权重参数相乘再加上偏置
wx_plus_b = tf.matmul(xs, w) + b
#激活函数
prediction = tf.nn.softmax(wx_plus_b)
print(prediction)
#定义会话，进行变量初始化
sess = tf.Session()
sess.run(tf.initialize_all_variables())
#读一个数据
batch_xs, batch_ys = mnist.train.next_batch(1)
#得到预测结果
result = sess.run([prediction, w, b], feed_dict={xs: batch_xs})
print(result)
