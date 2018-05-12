#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#9-12.py
#标准欧氏距离实现的人脸识别


import cv2
import numpy as np
import cv2.cv as cv 


print 'loading  ...'
#请在本程序运行前检查opencv的目录是否为下面的OPCV_PATH值
OPCV_PATH=r"F:/soft/c++/opencv"

def get_EuclideanDistance(x,y):  
    myx=np.array(x)  
    myy=np.array(y)  
    return np.sqrt(np.sum((myx-myy)*(myx-myy)))*np.var(myx-myy)



def get_distance(img,findimg):
    newsize=(img.shape[1],img.shape[0])   
    fimg=cv2.resize(findimg,newsize)
    my_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    my_fimg=cv2.cvtColor(fimg,cv2.COLOR_BGR2GRAY)
    return get_EuclideanDistance(my_img,my_fimg)

def findface(image):
    #人脸识别，获取脸在图片中的坐标
    grayscale = cv.CreateImage((image.width, image.height), 8, 1)
    cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)
    cascade = cv.Load(OPCV_PATH+"/data/haarcascades/haarcascade_frontalface_alt_tree.xml")
    rect = cv.HaarDetectObjects(grayscale, cascade, cv.CreateMemStorage(), 1.1, 2,cv.CV_HAAR_DO_CANNY_PRUNING, (10,10))

    result = []
    for r in rect:
        result.append([(r[0][0], r[0][1]), (r[0][0]+r[0][2], r[0][1]+r[0][3])])

    return result
    
fn='billall1.png'
fnt= 'billtest.png'
my_img=cv.LoadImage(fn)
face_test=cv.LoadImage(fnt)

#获取脸在图片中的坐标
faceresult=findface(my_img)
facet_result=findface(face_test)
    
myimg=cv2.imread(fn)
myimgt=cv2.imread(fnt)

#IT精英比尔盖茨
isface1=get_distance(myimg[faceresult[0][0][0]:faceresult[0][1][0],faceresult[0][0][1]:faceresult[0][1][1],:],myimgt[facet_result[0][0][0]:facet_result[0][1][0],facet_result[0][0][1]:facet_result[0][1][1],:])
isface2=get_distance(myimg[faceresult[1][0][0]:faceresult[1][1][0],faceresult[1][0][1]:faceresult[1][1][1],:],myimgt[facet_result[0][0][0]:facet_result[0][1][0],facet_result[0][0][1]:facet_result[0][1][1],:])
if isface1<isface2:
    cv2.rectangle(myimg, faceresult[0][0], faceresult[0][1],(255,0,255))     
    cv2.rectangle(myimgt, facet_result[0][0], facet_result[0][1],(255,0,255))    
else:  
    cv2.rectangle(myimg, faceresult[1][0], faceresult[1][1],(255,0,255))    
    cv2.rectangle(myimgt, facet_result[0][0], facet_result[0][1],(255,0,255))    

    
    
cv2.namedWindow('img')       
cv2.imshow('img', myimg)  
cv2.namedWindow('imgt')       
cv2.imshow('imgt', myimgt)   
cv2.waitKey()  
cv2.destroyAllWindows() 
    

