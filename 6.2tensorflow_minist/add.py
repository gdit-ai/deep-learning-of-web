# -*- coding: utf-8 -*-

a = 1
b = 2
c = a + b 
print('okok')
print('ok1')
print(c)


import tensorflow as tf
sess = tf.Session()
a = tf.constant(10)
b= tf.constant(12)
c = a + b
print(c)
print(sess.run(c))
