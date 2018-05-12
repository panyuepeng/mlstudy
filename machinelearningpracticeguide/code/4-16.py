#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#4-16.py
import cv2
import numpy as np


fn1="test1.jpg"
fn2="test2.jpg"
fn3="secret.png"
redcolor=(0, 0, 255)
if __name__ == '__main__':
    print u'正在处理中',
    img1 = cv2.imread(fn1)
    img2 = cv2.imread(fn2)

    w=img1.shape[1]
    h=img1.shape[0]  
   

    #加上需要隐藏的消息
    cv2.putText(img1,"hello,world!", (20,300),cv2.FONT_HERSHEY_PLAIN, 3.0, redcolor, thickness = 2)
    cv2.putText(img1,"code by myhaspl:myhaspl@qq.com", (20,60),cv2.FONT_HERSHEY_PLAIN, 2.0, redcolor, thickness = 2) 
    cv2.putText(img1,"Installing Python is generally easy. ", (1,90),cv2.FONT_HERSHEY_PLAIN, 2, redcolor, thickness = 1)     
    
    cv2.namedWindow('img1')     
    cv2.imshow('img1', img1)   
    cv2.namedWindow('img2-1')     
    cv2.imshow('img2-1', img2)    
    #处理隐藏目标图
    #将所有蓝色值变成奇数
    for j in xrange(0,h):
        for i in xrange(0,w):
            if (img2[j,i,0]%2)==1:
                img2[j,i,0]=img2[j,i,0]-1
        print '.',
        mirror_w=w/2
    #读取源图，并将信息写入目标图
    for j in xrange(0,h):
        for i in xrange(0,w):
            if (img1[j,i,0],img1[j,i,1],img1[j,i,2])==redcolor:
                img2[j,i,0]=img2[j,i,0]+1
        print '.',
    #保存修改后的目标图，并显示
    cv2.namedWindow('img2-2')     
    cv2.imshow('img2-2', img2)         
    cv2.imwrite(fn3, img2)      
    cv2.waitKey()
    cv2.destroyAllWindows()    
    
    
