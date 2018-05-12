#!/usr/bin/env python
#-*- coding: utf-8 -*-
#4-11.py
import cv2
import numpy as np

fn="test1.jpg"

if __name__ == '__main__':
    print 'http://blog.csdn.net/myhaspl'
    print 'myhaspl@qq.com'
    print
    print 'loading %s ...' % fn
    img = cv2.imread(fn)
    sp=img.shape
    print sp
    #height
    sz1=sp[0]
    #width
    sz2=sp[1]
    print 'width:%d\nheight:%d'%(sz2,sz1)
    #创建一个窗口并显示图像
    cv2.namedWindow('img')     
    cv2.imshow('img', img)
    #复制图像
    myimg2= img.copy();
    cv2.namedWindow('myimg2')     
    cv2.imshow('myimg2', myimg2)    

    #复制并转换为黑白图像
    myimg1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('myimg1')     
    cv2.imshow('myimg1', myimg1) 
    cv2.waitKey()
    cv2.destroyAllWindows()
