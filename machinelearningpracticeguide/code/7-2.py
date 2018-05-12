#!/usr/bin/env python
# -*- coding: utf-8 -*-
#7-2.py
import numpy as np
b=1
a=0.3
x=np.array([[b,1,3],[b,2,5],[b,1,8],[b,2,15],[b,3,7],[b,4,29]])
d=np.array([1,1,-1,-1,1,-1])
w=np.array([b,0,0])
def sgn(v):
        if v>=0:
                return 1
        else:
                return -1
def comy(myw,myx):
        return sgn(np.dot(myw.T,myx))
def neww(oldw,myd,myx,a):
        return oldw+a*(myd-comy(oldw,myx))*myx
i=0
for xn in x:
        w=neww(w,d[i],xn,a)
        i+=1

   
test=np.array([b,9,19])
print "%d ~ %d => %d "%(test[1],test[2],comy(w,test))
test=np.array([b,9,64])
print "%d ~ %d => %d "%(test[1],test[2],comy(w,test))