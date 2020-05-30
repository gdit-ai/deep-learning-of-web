import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

data_path = './bmi.txt'
model_save_path = './model/'

#获取数据和标签
def get_data(path):
    train_data = []
    train_labels = []
    test_labels = []
    with open(path) as ifile:
        for line in ifile:
            tokens = line.strip().split(' ')
            tmp_data = [int(tk) for tk in tokens[:-1]]
            tmp_label = tokens[-1]
            #设置胖瘦正常的标签，
            if tmp_label == 'fat':
                label = [1,0,0]
            elif tmp_label == 'normal':
                label = [0,1,0]
            elif tmp_label == 'thin':
                label = [0,0,1]


            train_data.append(tmp_data)
            train_labels.append(label)
            test_labels.append(tmp_label)

    return train_data, train_labels, test_labels

train_data, train_labels, test_labels = get_data(data_path)


#用占位符定义w,y的大小
w = tf.Variable(tf.zeros([2,3]), dtype=tf.float32)
b = tf.Variable(np.zeros([3]), dtype=tf.float32)
#身高和體重兩列，行數爲[None]
x=tf.placeholder(tf.float32,[None,2],name = "x_input")
y_=tf.placeholder(tf.float32,name = "y_predict")
#回歸方程表達式
y=tf.nn.softmax(tf.matmul(x,w) + b)
#定義交叉熵函數
cross_encropy=-tf.reduce_mean(y_*tf.log(y))
#選擇優化器，學習率：0.01
train_step = tf.train.AdamOptimizer(0.01).minimize(cross_encropy)


#train
def train_model(train_data,train_label):
    with tf.Session() as sess:
        count = 0
        init = tf.global_variables_initializer()
        sess.run(init)
        epoch = 3
        for i in range(epoch):
            for j in range(20000):
                result = sess.run([train_step, y], feed_dict={x: train_data[j: j + 1], y_: train_label[j: j + 1]})
                # print(result)
            saver = tf.train.Saver()
            saver.save(sess, "./model/my-model", global_step=epoch)
        print('train finsh')
train_model(train_data,train_labels)