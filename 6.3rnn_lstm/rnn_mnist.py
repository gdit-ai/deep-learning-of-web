# 通过RNN实现Mnist，神经网络将一幅数字图片的像素矩阵从行索引0开始一行一行的循环扫描，将
# 整个像素矩阵扫描完后，再预测数字（而CNN是通过卷积核滑窗扫描、卷积运算进行预测）

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('Mnist_data', one_hot=True)
# 定义超参数
learning_rate = 0.001# 学习率
training_iters = 10000# 循环次数
batch_size = 100# 批次数目（一次输入多少数据）

# Mnist中的图片是28*28*1 #
n_inputs = 28# 一次扫描28个像素点（像素矩阵有28列）
n_steps = 28# 一共扫描28次（像素矩阵有28行），与时间相对应
##############################
n_hidden_units = 128# 在隐藏层中神经元的数量
n_classes = 10# Mnist中只有0-9这10个类


# 定义placeholder
x = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
y = tf.placeholder(tf.float32, [None, n_classes])
keep_drop = tf.placeholder(tf.float32)

# 以字典的形式定义权重与偏值
weights = {
    # (28, 128), 输入数据进入cell时参与的运算的的权重
    'in':tf.Variable(tf.random_normal([n_inputs, n_hidden_units])),
    # (128, 10)，数据从cell中变为输出数据时参与的运算的权重
    'out':tf.Variable(tf.random_normal([n_hidden_units, n_classes]))
}
biases = {
    # (128, )，输入数据进入cell时参与的运算的的偏值
    'in':tf.Variable(tf.constant(0.1, shape=[n_hidden_units,])),
    # (10, )，数据从cell中变为输出数据时参与的运算的偏值
    'out':tf.Variable(tf.constant(0.1, shape=[n_classes,]))
}


# 定义RNN
def RNN(X, weights, biases):
    # 定义输入数据进入cell时经过的隐藏层
    X = tf.reshape(X, [-1, n_inputs])
    X_into_Cell = tf.matmul(X, weights['in']) + biases['in']
    X_into_Cell_drop = tf.nn.dropout(X_into_Cell, keep_drop)# 防止过拟合
    X_into_Cell_drop = tf.reshape(X_into_Cell_drop, [-1, n_steps, n_hidden_units])

    # 定义cell
    lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden_units, forget_bias=1.0, state_is_tuple=True)
    # 对于BasicLSTMCell来说，lstm_cell中的state_is_tuple的作用是确保初始化state时生成一个包含两个元素的tuple，两个元素分别是c_state（主线state）和m_state（分线state）
    # forget_bias=1.0确保分线state都可以得到保留
    __init__state = lstm_cell.zero_state(batch_size, dtype=tf.float32)# 初始化state，与上面定义的cell相对应

    # 定义cell中的运算
    outputs, states = tf.nn.dynamic_rnn(lstm_cell, X_into_Cell_drop, initial_state=__init__state, time_major=False)
    # 其中的outputs就是cell的输出值，而states则是每个cell内存中保留的状态（计算下一次输出值时被调用）
    # 其中time_major的作用指的是n_steps处于主要维度（一维）还是次要维度（二维、三维...），前者则为True，后者则为False
    # 定义数据从cell中变为输出数据时经过的隐藏层
    results = tf.matmul(states[1], weights['out']) + biases['out']
    return results

# 定义预测值
prediction = RNN(x, weights, biases)
# 定义损失函数
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=prediction))
# 定义训练函数
train_step = tf.train.AdamOptimizer(learning_rate).minimize(cost)

# 定义准确率
correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

with tf.Session() as sess:

    sess.run(tf.initialize_all_variables())# 全局初始化
    counter = 10
    for step in range(training_iters):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        batch_xs = batch_xs.reshape([batch_size, n_steps, n_inputs])
        sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys, keep_drop: 0.5})

        if step % 1000 == 0:
            counter -= 1
            # 每训练1000次输出一次剩余的训练次数以及当前的识别准确度
            print('the remaining times trained is ', counter * 1000, '.')
            print('the current accuracy is ', sess.run(accuracy, feed_dict={x: batch_xs, y: batch_ys, keep_drop: 0.5}), '.')
            print()

    # 保存神经网络中的参数
    saver = tf.train.Saver()
    save_path = saver.save(sess, 'Mnist_paramater_RNN/save_parameter.ckpt')

    # 提示神经网络已经完成训练
    print('The training is over!')
