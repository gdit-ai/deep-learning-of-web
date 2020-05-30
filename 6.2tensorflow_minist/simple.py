import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#读取数据
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
#构建网络
# images data
#占用一个空间　[None, 784]
x = tf.placeholder("float", shape=[None, 784])
# images labels
y_ = tf.placeholder("float", shape=[None, 10])
# reshape from 784x1 to 28x28
x_image = tf.reshape(x, [-1,28,28,1])
# convolution
#x [28x28]
def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')
# for weights intialization
def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)
def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)
# pooling
def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')
W_conv1 = weight_variable([5, 5, 1, 32])
#卷积之后大小是32x28x28
new_cov_img = conv2d(x_image,W_conv1)

b_conv1 = bias_variable([32])

print(new_cov_img)
#32x28x28
h_conv1 = tf.nn.relu( new_cov_img)
#32x14x14
h_pool1 = max_pool_2x2(h_conv1)

print(h_pool1)
#32*14*14
h_pool2_flat = tf.reshape(h_pool1, [-1, 32*14*14])
print(h_pool2_flat)
#参数＝　输入维度*输出维度
#　　　＝　6272 * 10
W_fc2 = weight_variable([32*14*14, 10])
#输出维度 = 10维
a10 = tf.matmul(h_pool2_flat, W_fc2)
print(a10)
b_fc2 = bias_variable([10])
y_conv=tf.nn.softmax(a10 + b_fc2)

# loss = (y_ - y_conv)
cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

keep_prob = tf.placeholder("float")

print(y_conv)

# start graph
sess = tf.InteractiveSession()

for i in range(5000):
	# 50一批
	batch = mnist.train.next_batch(50)
	# 训练
	train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})