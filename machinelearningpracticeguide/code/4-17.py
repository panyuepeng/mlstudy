#!/usr/bin/env python  
#-*- coding: utf-8 -*-  
#code:myhaspl@qq.com  
#解码文件  
#4-17.py
import cv2  
import numpy as np  
fn="secret.png"  
if __name__ == '__main__':  
    print 'loading  ...'  
    print u'正在处理中',  
    img = cv2.imread(fn)  
    w=img.shape[1]  
    h=img.shape[0]    
    imginfo =np.zeros((h,w,3), np.uint8)     
    for j in xrange(0,h):  
        for i in xrange(0,w):  
            if (img[j,i,0]%2)==1:  
                imginfo[j,i,1]=255  
        print '.',    
    cv2.imshow('info', imginfo)           
    cv2.imwrite(fn, imginfo)        
    cv2.waitKey()  
    cv2.destroyAllWindows()       