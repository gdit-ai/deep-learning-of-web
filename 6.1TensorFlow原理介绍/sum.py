import tensorflow as tf
x1 = tf.constant(90, name="x1")
x2 = tf.constant(80, name="x2")
x3 = tf.constant(70, name="x3")
add = x1 + x2 + x3
print(add)
