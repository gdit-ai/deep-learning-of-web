import tensorflow as tf
import numpy as np


# #獲取數據
# def get_data(path):
#     data = []
#     labels = []
#     with open(path) as ifile:
#         for line in ifile:
#             tokens = line.strip().split(' ')
#             tmp_data = [int(tk) for tk in tokens[:-1]]
#             tmp_label = tokens[-1]
#             #设置胖瘦正常的标签
#             if tmp_label == 'fat':
#                 label = [1,0,0]
#             elif tmp_label == 'normal':
#                 label = [0,1,0]
#             elif tmp_label == 'thin':
#                 label = [0,0,1]
#
#             data.append(tmp_data)
#             labels.append(label)
#     return data,labels
# path = './bmi.txt'
# train_data, train_label = get_data(path)
#
# '''
# 假设胖瘦与体重和身高呈回归方程关系，设为y = w * x + b
# 身高、体重两列，行数设置为None,
# 因为x*w是矩阵运算，第一个矩阵的列数一定要和第二个矩阵的行数相等，
# y输出是瘦、正常、胖的各自的概率，所以w的列数就是3
# '''
#
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
#
#
# #訓練模型
# with tf.Session() as sess:
#     count = 0
#     init = tf.global_variables_initializer()
#     sess.run(init)
#     epoch = 3
#     for i in range(epoch):
#         for j in range(20000):
#             result = sess.run([train_step, y], feed_dict={x: train_data[j: j + 1], y_: train_label[j: j + 1]})
#
#     saver = tf.train.Saver()
#     saver.save(sess, "./model/my-model", global_step=epoch)
#     print('train finsh')
#
#
# # 測試模型
# with tf.Session() as sess:
#     saver = tf.train.Saver()
#     with open(path) as ifile:
#         count = 0
#         true = 0
#         for line in ifile:
#
#             predict = ''
#             saver.restore(sess, tf.train.latest_checkpoint("./model/"))
#             tokens = line.strip().split(' ')
#             tmp_data = [int(tk) for tk in tokens[:-1]]
#             result = sess.run([train_step,y], feed_dict =  {x: [tmp_data], y_: [None]})[1][0]
#             if max(result) == result[0]:
#                 predict = 'fat'
#             if max(result) == result[1]:
#                 predict = 'normal'
#             if max(result) == result[2]:
#                 predict = 'thin'
#             if tokens[-1] == predict:
#                 true+= 1
#             count += 1
#
#     print(true/count)



import matplotlib.pyplot as plt
''' 数据读入 '''
data = []
labels = []
count = 0
with open("bmi.txt") as ifile:
    for line in ifile:
        tokens = line.strip().split(' ')
        tmp_data = [int(tk) for tk in tokens[:-1]]
        tmp_label = tokens[-1]
        if count < 500:
            with tf.Session() as sess:
                saver = tf.train.Saver()
                saver.restore(sess, tf.train.latest_checkpoint("./model/"))
                result = sess.run([train_step, y], feed_dict={x: [tmp_data], y_: [None]})[1][0]
                if max(result) == result[0]:
                    predict = 'fat'
                if max(result) == result[1]:
                    predict = 'normal'
                if max(result) == result[2]:
                    predict = 'thin'
                if tokens[-1] != predict:
                    tmp_label = 0
                count += 1
                print(count)


        data.append(tmp_data)
        labels.append(tmp_label)
data_input = np.array(data)
labels = np.array(labels)
label_num= np.size(labels)

label_transfer = np.zeros(label_num)

''' 标签转换为1/2/3 '''
for num in range(label_num):
    if labels[num] == 'fat':
        label_transfer[num] = 3
    elif labels[num] == 'normal':
        label_transfer[num] = 2
    elif labels[num] == 'thin':
        label_transfer[num] = 1

# print(data_input)

x = data_input[:,0]
y = data_input[:,1]

for indx in range(500):
    if (label_transfer[indx] == 3):
        plt.scatter(x[indx], y[indx], c='red', marker='o')
    elif (label_transfer[indx] == 2):
        plt.scatter(x[indx], y[indx], c='blue', marker='o')
    elif (label_transfer[indx] == 1):
        plt.scatter(x[indx], y[indx], c='green', marker='o')
    elif (label_transfer[indx] == 0):
        plt.scatter(x[indx], y[indx], c='black', marker='o')

# print(label_transfer)
plt.show()