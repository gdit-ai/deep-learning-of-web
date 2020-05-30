import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
#自动下载minist数据，读进来。
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
# 加载元图和权重
saver = tf.train.import_meta_graph('./model/mninst_dnn-1000.meta')

sess = tf.Session()
saver.restore(sess, tf.train.latest_checkpoint("./model/"))

graph = tf.get_default_graph()
xs = graph.get_tensor_by_name("Placeholder:0") # w1：张量名 => name
w = graph.get_tensor_by_name("w:0") # w1：张量名 => name
prediction = graph.get_tensor_by_name("predict:0") # w1：张量名 => name

print(w)
print(prediction)

batch_xs, batch_ys = mnist.train.next_batch(1)
#得到预测结果
prediction_lable = tf.argmax(prediction, 1)
result = sess.run([prediction, prediction_lable], feed_dict={xs: batch_xs})
print(result[1])


