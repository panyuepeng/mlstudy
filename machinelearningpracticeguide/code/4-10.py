#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#4-10.py
import cv2
import numpy as np


fn="test1.jpg"

if __name__ == '__main__':
    print 'http://blog.csdn.net/myhaspl'
    print 'myhaspl@qq.com'
    print
    print 'loading %s ...' % fn
    print '正在处理中',
    img = cv2.imread(fn)
    w=img.shape[1]
    h=img.shape[0]    
    ii=0
    #关于纵向生成镜像
    #
    mirror_w=w/2
    for j in xrange(0,h):
        for i in xrange(0,mirror_w):
            img[j,i,:]=img[j,w-i-1,:]
        print '.',
    cv2.namedWindow('img')     
    cv2.imshow('img', img)    
    cv2.waitKey()
    cv2.destroyAllWindows()
