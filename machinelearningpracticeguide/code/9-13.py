#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#9-13
#pcb+改进变异系数人脸识别


import cv2
import numpy as np
import cv2.cv as cv
import mlpy 



print 'loading  ...'
#请在本程序运行前检查opencv的目录是否为下面的OPCV_PATH值
OPCV_PATH=r"D:/opencv/sources"
def get_EuclideanDistance(x,y):  
    myx=np.array(x)  
    myy=np.array(y)  
    return np.sqrt(np.sum((myx-myy)*(myx-myy)))/(np.var(myx-myy)/abs(np.mean(myx-myy)))



def get_distance(img,findimg):
    newsize=(21,21)   
    fimg=cv2.resize(findimg,newsize)
    img=cv2.resize(img,newsize)
    my_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    my_fimg=cv2.cvtColor(fimg,cv2.COLOR_BGR2GRAY)

    pcaimg = mlpy.PCA() 
    pcaimg.learn(my_img) 
    pca_img = pcaimg.transform(my_img, k=1)  
    pca_img=pcaimg.transform_inv(pca_img)
    
    pcafimg = mlpy.PCA() 
    pcafimg.learn(my_fimg) 
    pca_fimg = pcaimg.transform(my_fimg, k=1)
    pca_fimg= pcafimg.transform_inv(pca_fimg)
    
    return get_EuclideanDistance(pca_img,pca_fimg)

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

  
fn1='jjgdall.png' 
fn2='facesb.png'
fnt='jjgdtest.png'



face_test=cv.LoadImage(fnt)
#获取脸在图片中的坐标
facet_result=findface(face_test)
myimgt=cv2.imread(fnt)

my_img=cv.LoadImage(fn1)
myimg=cv2.imread(fn1)
#获取脸在图片中的坐标
faceresult=findface(my_img)
   



#找到威尔 史密斯
isface1=get_distance(myimg[faceresult[0][0][0]:faceresult[0][1][0],faceresult[0][0][1]:faceresult[0][1][1],:],myimgt[facet_result[0][0][0]:facet_result[0][1][0],facet_result[0][0][1]:facet_result[0][1][1],:])
isface2=get_distance(myimg[faceresult[1][0][0]:faceresult[1][1][0],faceresult[1][0][1]:faceresult[1][1][1],:],myimgt[facet_result[0][0][0]:facet_result[0][1][0],facet_result[0][0][1]:facet_result[0][1][1],:])
if isface1<isface2:
    cv2.rectangle(myimg, faceresult[0][0], faceresult[0][1],(255,0,255))     
    cv2.rectangle(myimgt, facet_result[0][0], facet_result[0][1],(255,0,255))    
else:  
    cv2.rectangle(myimg, faceresult[1][0], faceresult[1][1],(255,0,255))    
    cv2.rectangle(myimgt, facet_result[0][0], facet_result[0][1],(255,0,255))    

    
    
cv2.namedWindow('img1')       
cv2.imshow('img1', myimg)  


my_img=cv.LoadImage(fn2)
myimg=cv2.imread(fn2)
#获取脸在图片中的坐标
faceresult=findface(my_img)

#找到威尔 史密斯
isface1=get_distance(myimg[faceresult[0][0][0]:faceresult[0][1][0],faceresult[0][0][1]:faceresult[0][1][1],:],myimgt[facet_result[0][0][0]:facet_result[0][1][0],facet_result[0][0][1]:facet_result[0][1][1],:])
isface2=get_distance(myimg[faceresult[1][0][0]:faceresult[1][1][0],faceresult[1][0][1]:faceresult[1][1][1],:],myimgt[facet_result[0][0][0]:facet_result[0][1][0],facet_result[0][0][1]:facet_result[0][1][1],:])
if isface1<isface2:
    cv2.rectangle(myimg, faceresult[0][0], faceresult[0][1],(255,0,255))     
    cv2.rectangle(myimgt, facet_result[0][0], facet_result[0][1],(255,0,255))    
else:  
    cv2.rectangle(myimg, faceresult[1][0], faceresult[1][1],(255,0,255))    
    cv2.rectangle(myimgt, facet_result[0][0], facet_result[0][1],(255,0,255))    

cv2.namedWindow('img2')       
cv2.imshow('img2', myimg) 
 
cv2.namedWindow('imgt')       
cv2.imshow('imgt', myimgt) 
  
cv2.waitKey()  
cv2.destroyAllWindows() 
    

