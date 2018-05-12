#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#4-8.py
import cv2
import numpy as np


fn="pictestt1.png"
if __name__ == '__main__':
    print 'http://blog.csdn.net/myhaspl'
    print 'myhaspl@qq.com'
    print
    print 'loading %s ...' % fn
    print 'working',
    img = cv2.imread(fn)
    w=img.shape[1]
    h=img.shape[0]
    sz1=w*2
    sz0=h*3
    #创建空白图像，然后将图片排列 
    myimg1=np.zeros((sz1,sz0,3), np.uint8)      
    #翻转并生成图像
    #逐个像素复制
    img_x=0
    img_y=0
    for now_y in xrange(0,sz0):
        for now_x in xrange(0,sz1):
            myimg1[now_x,now_y,:]=img[img_y,img_x,:]           
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
