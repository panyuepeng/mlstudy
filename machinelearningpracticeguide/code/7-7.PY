#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#7-7.py
import numpy as np
import pylab as pl
b=1
a=0.1
x = np.array([[1,1,6],[1,3,12],[1,3,9],[1,3,21],[1,2,16],[1,3,15]]) 
d =np.array([1,1,-1,-1,1,-1]) 
w=np.array([b,0,0])
expect_e=0.005
maxtrycount=200

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

myx=x[:,1]
myy=x[:,2]
pl.subplot(111)
x_max=np.max(myx)+10
x_min=np.min(myx)-5
y_max=np.max(myy)+50  
y_min=np.min(myy)-5
pl.xlabel(u"x")
pl.xlim(x_min, x_max)
pl.ylabel(u"y")
pl.ylim(y_min, y_max)
#绘制样本点
for i in xrange(0,len(d)):
    if d[i]>0:
        pl.plot(myx[i], myy[i], 'r*')
    else:
        pl.plot(myx[i], myy[i], 'ro')        

 #绘制测试点
test=np.array([1,9,27]) 
pl.plot(test[1],test[2], 'bx')
test=np.array([1,11,66]) 
pl.plot(test[1],test[2], 'bx')
pl.show()