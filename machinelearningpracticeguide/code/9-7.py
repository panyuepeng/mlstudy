#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#9-7.py
#余弦距离识别图片类型
import numpy as np

import cv2






print u'正在处理中'


w_fg=20
h_fg=15
picflag=3
def readpic(fn):
    #返回图片特征码
    fnimg = cv2.imread(fn)
    img=cv2.resize(fnimg,(800,600))
    w=img.shape[1]  
    h=img.shape[0]  
    w_interval=w/w_fg
    h_interval=h/h_fg 
    alltz=[]
    alltz.append([])
    alltz.append([])
    alltz.append([])
    for now_h in xrange(0,h,h_interval):
        for now_w in xrange(0,w,w_interval):
            b = img[now_h:now_h+h_interval,now_w:now_w+w_interval,0]
            g = img[now_h:now_h+h_interval,now_w:now_w+w_interval,1]
            r = img[now_h:now_h+h_interval,now_w:now_w+w_interval,2]
            btz=np.mean(b)
            gtz=np.mean(g)
            rtz=np.mean(r)
            alltz[0].append(btz)
            alltz[1].append(gtz)
            alltz[2].append(rtz)
    return alltz
        
def get_cossimi(x,y):
    myx=np.array(x)
    myy=np.array(y)
    cos1=np.sum(myx*myy)
    cos21=np.sqrt(sum(myx*myx))
    cos22=np.sqrt(sum(myy*myy))
    return cos1/float(cos21*cos22)
    
#x和d样本初始化
train_x =[]
d=[]

#读取图片，提取每类图片的特征
for ii in xrange(1,picflag+1):
    smp_x=[]
    b_tz=np.array([0,0,0])
    g_tz=np.array([0,0,0])
    r_tz=np.array([0,0,0])
    mytz=np.zeros((3,w_fg*h_fg))
    for jj in xrange(1,3):
        fn='p'+str(ii)+'-'+str(jj)+'.png'
        tmptz=readpic(fn)
        mytz+=np.array(tmptz)
    mytz/=3
    train_x.append(mytz[0].tolist()+mytz[1].tolist()+mytz[2].tolist())

fn='ptest3.png'
testtz=np.array(readpic(fn))
simtz=testtz[0].tolist()+testtz[1].tolist()+testtz[2].tolist()
maxtz=0
nowi=0
for i in xrange(0,picflag):
    nowsim=get_cossimi(train_x[i],simtz)
    if nowsim>maxtz:
        maxtz=nowsim
        nowi=i        
print u'%s属于第%d类'%(fn,nowi+1)

fn='ptest1.png'
testtz=np.array(readpic(fn))
simtz=testtz[0].tolist()+testtz[1].tolist()+testtz[2].tolist()
maxtz=0
nowi=0
for i in xrange(0,picflag):
    nowsim=get_cossimi(train_x[i],simtz)
    if nowsim>maxtz:
        maxtz=nowsim
        nowi=i        
print u'%s属于第%d类'%(fn,nowi+1)
        
fn='ptest2.png'
testtz=np.array(readpic(fn))
simtz=testtz[0].tolist()+testtz[1].tolist()+testtz[2].tolist()
maxtz=0
nowi=0
for i in xrange(0,picflag):
    nowsim=get_cossimi(train_x[i],simtz)
    if nowsim>maxtz:
        maxtz=nowsim
        nowi=i        
print u'%s属于第%d类'%(fn,nowi+1)

