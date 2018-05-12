#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#7-6.py
import numpy as np
b=1
a=0.1
x = np.array([[1,1,6],[1,2,12],[1,3,9],[1,8,24]])
d =np.array([1,1,-1,-1])
w=np.array([b,0,0])
expect_e=0.005
maxtrycount=20

def sgn(v):
        if v>0:
                return 1
        else:
                return -1
def get_v(myw,myx):
        return sgn(np.dot(myw.T,myx))
def neww(oldw,myd,myx,a):
        mye=get_e(oldw,myx,myd)
        return (oldw+a*mye*myx,mye)
def get_e(myw,myx,myd):
        return myd-get_v(myw,myx)


mycount=0
while True:
        mye=0
        i=0          
        for xn in x:
                w,e=neww(w,d[i],xn,a)
                i+=1
                mye+=pow(e,2)  
        mye/=float(i)              
        mycount+=1
        print u"第 %d 次调整后的权值："%mycount
        print w
        print u"误差：%f"%mye        
        if abs(mye)<expect_e or mycount>maxtrycount:break 
               
for xn in x:
        print "%d    %d => %d "%(xn[1],xn[2],get_v(w,xn))
test=np.array([1,9,27])  
print "%d     %d => %d "%(test[1],test[2],get_v(w,test))  
test=np.array([1,11,66])  
print "%d     %d => %d "%(test[1],test[2],get_v(w,test))