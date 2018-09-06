# coding: utf-8
# Author: pan
# Filename: 


import tensorflow as tf
import numpy as np
import scipy

a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([2.0, 3.0], name='b')
result = a + b

print tf.__version__

print a.graph is tf.get_default_graph()

# 在不同的计算图上定义和使用变量
g1 = tf.Graph()
with g1.as_default():
    # 在计算图g1中定义变量v并设置初始值为0
    v = tf.get_variable(
        "v", initializer=tf.zeros_initializer(shape=[1]))

g2 = tf.Graph()
with g2.as_default():
    # 在计算图g2中定义变量v并设置初始值为1
    v = tf.get_variable(
        "v", initializer=tf.ones_initializer(shape=[1]))


# 在计算图g1中读取变量v的取值
with tf.Session(graph=g1) as sess:
    tf.initialize_all_variables().run()
