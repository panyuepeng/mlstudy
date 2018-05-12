#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#4-7.py
import cv2
import numpy as np


fn="pictestt1.png"
if __name__ == '__main__':
    print 'http://blog.csdn.net/myhaspl'
    print 'myhaspl@qq.com'
    print
    print 'loading %s ...' % fn
    print u'正在处理中',
    img = cv2.imread(fn)
    w=img.shape[1]
    h=img.shape[0]
    sz1=w*5
    sz0=h*2
    #创建空白图像，然后将图片排列 
    myimg1=np.zeros((sz0,sz1,3), np.uint8)      
    #
    #逐个像素复制
    img_x=0
    img_y=0
    for now_y in xrange(0,sz0):
        for now_x in xrange(0,sz1):
            myimg1[now_y,now_x,0]=img[img_y,img_x,0]
            myimg1[now_y,now_x,1]=img[img_y,img_x,1]
            myimg1[now_y,now_x,2]=img[img_y,img_x,2]              
            img_x+=1
            if img_x>=w:
                img_x=0
        img_y+=1        
        if img_y>=h:
            img_y=0            
        print '.',
    cv2.namedWindow('img1')     
    cv2.imshow('img1', myimg1)    
    cv2.waitKey()
    cv2.destroyAllWindows()