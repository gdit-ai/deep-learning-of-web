
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

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

data_path = './bmi.txt'
train_data, train_labels, test_labels = get_data(data_path)

#用占位符定义w,y的大小
w = tf.Variable(tf.zeros([2,3]), dtype=tf.float32)
b = tf.Variable(np.zeros([3]), dtype=tf.float32)
#身高和體重兩列，行數爲[None]
x=tf.placeholder(tf.float32,[None,2],name = "x_input")
y_=tf.placeholder(tf.float32,name = "y_predict")
#回歸方程表達式
y=tf.nn.softmax(tf.matmul(x,w) + b)

# 測試模型
predict_labels = []
with tf.Session() as sess:
    count = 0
    true = 0
    saver = tf.train.Saver()
    saver.restore(sess, tf.train.latest_checkpoint(model_save_path))
    for i in range(len(train_labels)):
        result1 = sess.run([y], feed_dict={x: train_data[i: i + 1]})
        # print(result1[0][0])
        result = result1[0][0]
        if max(result) == result[0]:
            print("fat")
        if max(result) == result[1]:
           print('normal')
        if max(result) == result[2]:
            print('thin')
        count += 1
    print(true / count)