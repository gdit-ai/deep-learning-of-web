import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# for weights intialization
def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)
# for biases initialization
def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

# convolution
def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

# pooling
def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')

# start graph
sess = tf.InteractiveSession()

# read data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# images data
x = tf.placeholder("float", shape=[None, 784])
# images labels
y_ = tf.placeholder("float", shape=[None, 10])

# first layer's weights and biases
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])

# reshape from 784x1 to 28x28
x_image = tf.reshape(x, [-1,28,28,1])

# Convolutional 1
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)

# Pooling 1
# subsample from 28x28 to 14x14

#28*28*32 ->14*14*32
h_pool1 = max_pool_2x2(h_conv1)


# second layer's weights and biases
# W_conv2 = weight_variable([5, 5, 32, 64])
# b_conv2 = bias_variable([64])

# Convolutional 2
# h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
# Pooling 2
# subsample from 14x14 to 7x7
# h_pool2 = max_pool_2x2(h_conv2)

#7*7*64
# Fully connected
W_fc1 = weight_variable([14*14*32, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool1, [-1, 14*14*32])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# dropout
keep_prob = tf.placeholder("float")
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# output with softmax regression
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)


# training and evaluating
cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
sess.run(tf.initialize_all_variables())
# sess.run(tf.global_variables_initializer())

#epoch
for i in range(5000):
	# 50一批
	batch = mnist.train.next_batch(50)
	# 每100次迭代输出日志
	if i%100 == 0:
		train_accuracy = accuracy.eval(
			feed_dict={
				x:batch[0],
				y_: batch[1],
				keep_prob: 1.0
			})
		print("step %d, training accuracy %g"%(i, train_accuracy))
	# 训练
	train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})
# 输出最终得到的准确率
print("test accuracy %g"%accuracy.eval(
	feed_dict={
		x: mnist.test.images,
		y_: mnist.test.labels,
		keep_prob: 1.0
		}))
