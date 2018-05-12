#!/usr/bin/env python
# -*- coding: utf-8 -*-
#code:myhaspl@qq.com
#7-4.py

import numpy as np
b=1
a=0.5
x = np.array([[1,1,3],[1,2,3],[1,1,8],[1,2,15]])
d =np.array([1,1,-1,-1])
w=np.array([b,0,0])
wucha=0
ddcount=50


def sgn(v):
        if v>0:
                return 1
        else:
                return -1
def comy(myw,myx):
        return sgn(np.dot(myw.T,myx))


def tiduxz(myw,myx,mya):
        i=0
        sum_x=np.array([0,0,0])
        for xn in myx:
                if comy(myw,xn)!=d[i]:
                        sum_x+=d[i]*xn
                i+=1
        return mya*sum_x


        
i=0                
while  True:
        tdxz=tiduxz(w,x,a)
        w=w+tdxz
        i=i+1
        if abs(tdxz.sum())<=wucha or i>=ddcount:break
        

test=np.array([1,9,19])
print "%d %d => %d "%(test[1],test[2],comy(w,test))
test=np.array([1,3,22])
print "%d %d => %d "%(test[1],test[2],comy(w,test))