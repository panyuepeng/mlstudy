#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#9-11.py
#人脸定位 

import cv2

import cv2.cv as cv 



print 'loading  ...'


#请在本程序运行前检查opencv的目录是否为下面的OPCV_PATH值
OPCV_PATH=r"D:/opencv/sources"
 

def findface(image):
    #人脸识别，获取脸在图片中的坐标
    grayscale = cv.CreateImage((image.width, image.height), 8, 1)
    cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)
    cascade = cv.Load(OPCV_PATH+"/data/haarcascades/haarcascade_frontalface_alt_tree.xml")
    rect = cv.HaarDetectObjects(grayscale, cascade, cv.CreateMemStorage(), 1.015, 2,cv.CV_HAAR_DO_CANNY_PRUNING, (10,10))

    result = []
    for r in rect:
        result.append([(r[0][0], r[0][1]), (r[0][0]+r[0][2], r[0][1]+r[0][3])])

    return result
    
fn='facesb.png'
my_img=cv.LoadImage(fn)

#获取脸在图片中的坐标
faceresult=findface(my_img)

    
myimg=cv2.imread(fn)
for  ii in xrange(0,len(faceresult)):
    cv2.rectangle(myimg, faceresult[ii][0], faceresult[ii][1],(0,0,250))    


cv2.namedWindow('img')       
cv2.imshow('img', myimg)   
cv2.waitKey()  
cv2.destroyAllWindows() 
    
