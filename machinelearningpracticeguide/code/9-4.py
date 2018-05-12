#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#9-4.py
#图像倾斜后定位图片

import cv2
import numpy as np


print 'loading  ...'

def get_EuclideanDistance(x,y):  
    myx=np.array(x)  
    myy=np.array(y)  
    return np.sqrt(np.sum((myx-myy)*(myx-myy)))  
    
def findpic(img,findimg,h,fh,w,fw):
    minds=1e8
    mincb_h=0
    mincb_w=0
    for now_h in xrange(0,h-fh):
        for now_w in xrange(0,w-fw):
            my_img=img[now_h:now_h+fh,now_w:now_w+fw,:]
            my_findimg=findimg  
            dis=get_EuclideanDistance(my_img,my_findimg)
            if dis<minds:   
                mincb_h=now_h
                mincb_w=now_w                
                minds=dis
        print ".",   
    findpt=mincb_w,mincb_h
    cv2.rectangle(img, findpt, (findpt[0]+fw,findpt[1]+fh),(0,0,255))    
    return img
 

def showpiclocation(img,findimg):
    #定位图片
    w=img.shape[1]  
    h=img.shape[0]  
    fw=findimg.shape[1]
    fh=findimg.shape[0]
    return findpic(img,findimg,h,fh,w,fw)



fn='pictestxz.png'
fn1='pictestt1.png'
fn2='pictestt2.png'
myimg=cv2.imread(fn)
myimg1=cv2.imread(fn1)
myimg2=cv2.imread(fn2)

myimg=showpiclocation(myimg,myimg1)
myimg=showpiclocation(myimg,myimg2)
cv2.namedWindow('img')       
cv2.imshow('img', myimg)   
cv2.waitKey()  
cv2.destroyAllWindows() 
    
