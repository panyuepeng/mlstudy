# coding: utf-8
# File: tf_demo.py
# Date: 18-9-4
# Time: 下午9:29
# Author: Alpha Pyp

import numpy as np
import tensorflow as tf

if __name__ == '__main__':
    a = tf.constant([1.0, 2.0], name='a')
    b = tf.constant([2.0, 3.0], name='b')
    result = a + b
    print(result)
    sess = tf.Session()
    ar = sess.run(result)
    print(ar)