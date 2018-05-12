#!/usr/bin/env python
#-*- coding: utf-8 -*-
#4-12.py
import cv2
import numpy as np

fn="test1.jpg"

if __name__ == '__main__':
    print 'http://blog.csdn.net/myhaspl'
    print 'myhaspl@qq.com'
    print
    print 'loading %s ...' % fn
    img = cv2.imread(fn)
    coutn=100000
    for k in xrange(0,coutn):
	    xi = int(np.random.uniform(0,img.shape[1]))
	    xj = int(np.random.uniform(0,img.shape[0]))
	    if img.ndim == 2: 
		    img[xj,xi] = 255
	    elif img.ndim == 3: 
		    img[xj,xi,0]= 25
		    img[xj,xi,1]= 20
		    img[xj,xi,2]= 20   
    cv2.namedWindow('img')     
    cv2.imshow('img', img) 
    cv2.waitKey()
    cv2.destroyAllWindows()    
