#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#9-3.py
#少量噪声定位图片

import cv2
import numpy as np

 
print 'loading  ...'

def showpiclocation(img,findimg):
    #定位图片
    w=img.shape[1]  
    h=img.shape[0]  
    fw=findimg.shape[1]
    fh=findimg.shape[0]
    findpt=None
    for now_h in xrange(0,h-fh):
        for now_w in xrange(0,w-fw):
            comp_tz=img[now_h:now_h+fh,now_w:now_w+fw,:]-findimg       
            if abs(np.mean(comp_tz))<20:              
                findpt=now_w,now_h
                print "ok"
        print ".",
    if  findpt!=None:
        cv2.rectangle(img, findpt, (findpt[0]+fw,findpt[1]+fh),(0,0,255))
    return img

def addnoise(img):
    coutn=50000
    for k in xrange(0,coutn):  
        xi = int(np.random.uniform(0,img.shape[1]))  
        xj = int(np.random.uniform(0,img.shape[0]))  
        img[xj,xi,0]= 255 *np.random.rand() 
        img[xj,xi,1]= 255 *np.random.rand()   
        img[xj,xi,2]= 255 *np.random.rand() 

fn='pictest.png'
fn1='pictestt1.png'
fn2='pictestt2.png'
myimg=cv2.imread(fn)
myimg1=cv2.imread(fn1)
myimg2=cv2.imread(fn2)
addnoise(myimg)
myimg=showpiclocation(myimg,myimg1)
myimg=showpiclocation(myimg,myimg2)
cv2.namedWindow('img')       
cv2.imshow('img', myimg)   
cv2.waitKey()  
cv2.destroyAllWindows() 
    

