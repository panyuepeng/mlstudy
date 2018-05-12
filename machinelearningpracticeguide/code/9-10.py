#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#9-10.py
#PCA加上SVM识别图片类型
import numpy as np

import cv2
import mlpy





print u'正在处理中'


w_fg=10
h_fg=5
picflag=3
def readpic(fn):
    #返回图片特征码
    fnimg = cv2.imread(fn)
    img=cv2.resize(fnimg,(400,200))
    w=img.shape[1]  
    h=img.shape[0]  
    w_interval=w/w_fg
    h_interval=h/h_fg 
    alltz=[]
    for now_h in xrange(0,h,h_interval):
        for now_w in xrange(0,w,w_interval):            
            b = img[now_h:now_h+h_interval,now_w:now_w+w_interval,0]
            g = img[now_h:now_h+h_interval,now_w:now_w+w_interval,1]
            r = img[now_h:now_h+h_interval,now_w:now_w+w_interval,2]
            btz=np.mean(b)
            gtz=np.mean(g)
            rtz=np.mean(r)
            alltz.append([btz,gtz,rtz])
    result_alltz=np.array(alltz).T
    pca = mlpy.PCA() 
    pca.learn(result_alltz) 
    result_alltz = pca.transform(result_alltz, k=len(result_alltz)/2)   
    result_alltz =result_alltz.reshape(len(result_alltz))
    return result_alltz  
        
  
#x和d样本初始化
train_x =[]
d=[]

#读取图片，提取每类图片的特征
for ii in xrange(1,picflag+1):
    smp_x=[]
   
    mytz=np.zeros((3,w_fg*h_fg))
    for jj in xrange(1,4):
        fn='p'+str(ii)+'-'+str(jj)+'.png'
        tmptz=readpic(fn)
        train_x.append(tmptz.tolist())
        d.append(ii)

   

x=np.array(train_x)
y=np.array(d)
svm = mlpy.LibSvm(svm_type='c_svc', kernel_type='poly',gamma=50)
svm.learn(x, y)

print svm.pred(x)

fn='ptest3.png'
testtz=np.array(readpic(fn))
nowi=svm.pred(testtz)     
print u'%s属于第%d类'%(fn,nowi)

fn='ptest1.png'
testtz=np.array(readpic(fn))
nowi=svm.pred(testtz)       
print u'%s属于第%d类'%(fn,nowi)
        
fn='ptest2.png'
testtz=np.array(readpic(fn))
nowi=svm.pred(testtz)      
print u'%s属于第%d类'%(fn,nowi)

fn='ptest21.png'
testtz=np.array(readpic(fn))
nowi=svm.pred(testtz)      
print u'%s属于第%d类'%(fn,nowi)

fn='ptest22.png'
testtz=np.array(readpic(fn))
nowi=svm.pred(testtz)      
print u'%s属于第%d类'%(fn,nowi)

