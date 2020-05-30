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

# the error between prediction and real data
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

#定义会话，进行变量初始化
sess = tf.Session()
sess.run(tf.initialize_all_variables())

#得到预测结果
def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    corrct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(corrct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result

for i in range(2000):
    batch_xs, batch_ys = mnist.train.next_batch(64)
    sess.run(train_step, feed_dict={xs: batch_xs, ys:batch_ys})
    if i % 50 == 0:
       print(compute_accuracy(
           mnist.test.images, mnist.test.labels
       ))