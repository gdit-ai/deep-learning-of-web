import tensorflow as tf

#x = tf.placeholder(shape=[3], dtype=tf.float32)

x = tf.placeholder(dtype=tf.float32)
xShape = tf.shape(x)

w = tf.Variable(tf.zeros([3]), dtype=tf.float32)

#w = tf.Variable(dtype=tf.float32)

n = x * w

#y = n1 + n2 + n3
y = tf.reduce_sum(n)

print(y)

sess = tf.Session()
#  
init = tf.global_variables_initializer()
sess.run(init)

# result = sess.run([y], feed_dict={x1: [90,98], x2: [80,95], x3: [70,87]})
# print(result)

result = sess.run([y], feed_dict={x: [90,80,70],w:[0.6,0.3,0.1]})
print(result)

# result = sess.run([y], feed_dict={x1: 98, x2: 95, x3: 87})
# print(result)


#result = sess.run([x1, x2, x3, w1, w2, w3, y], feed_dict={x1: 90, x2: 80, x3: 70})
#print(result)
