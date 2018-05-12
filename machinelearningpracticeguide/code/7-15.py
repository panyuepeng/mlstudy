#!/usr/bin/env python
#-*- coding: utf-8 -*-
#email:myhaspl@qq.com
#author:麦好
#7-15.py
import numpy as np
import matplotlib.pyplot as plt
import mlpy


print 'loading  ...'

x = [[1,1],[2,4],[3,12],[9,70],[5,130],[4,13],[5,29],[5,135],[4,65],[10,1000],[8,520],[7,340],[6,40],[10,150]]
y=[1,1,1,1,0,1,1,0,0,0,0,0,1,1]
showpoint=['ro','r*']
tshowpoint=['bo','b*']
x=np.array(x)
y=np.array(y)
svm = mlpy.LibSvm(svm_type='c_svc', kernel_type='poly', gamma=50)
svm.learn(x, y)
lp_x1 = x[:,0]
lp_x2 = x[:,1]
xmin, xmax = np.min(lp_x1)-0.5, np.max(lp_x1)+0.5
ymin, ymax = np.min(lp_x2)-0.5, np.max(lp_x2)+0.5
plt.subplot(111)
plt.xlabel(u"x")
plt.xlim(xmin, xmax)
plt.ylabel(u"y")
plt.ylim(ymin, ymax)

#显示样本点
for ii in xrange(0,len(x)):
    ty=svm.pred(x[ii])
    if ty>0:
        plt.plot(lp_x1[ii], lp_x2[ii], showpoint[int(ty)])
    else:
        plt.plot(lp_x1[ii], lp_x2[ii], showpoint[int(ty)])        

#未知样本分类
tlp_x10=np.random.rand(100)*(xmax-xmin)+xmin
tlp_x20=tlp_x10**3+np.random.rand(100)*20-10
tlp_x11=np.random.rand(100)*(xmax-xmin)+xmin
tlp_x21=tlp_x11**2+np.random.rand(100)*20-10
tlp_x30=np.random.rand(50)*(xmax-xmin)+xmin
tlp_x31=tlp_x30**(round(np.random.rand()*6,0)+3)+np.random.rand(50)*10-5
tlp_x40=np.random.rand(50)*(xmax-xmin)+xmin
tlp_x41=tlp_x30**(round(np.random.rand(),0)+1)+np.random.rand(50)*10-5

tlp_x1=tlp_x10.tolist()+tlp_x11.tolist()+tlp_x30.tolist()+tlp_x40.tolist()
tlp_x2=tlp_x20.tolist()+tlp_x21.tolist()+tlp_x31.tolist()+tlp_x41.tolist()

tlp_x=np.array(zip(tlp_x1,tlp_x2))
for ii in xrange(0,len(tlp_x)):
    ty=svm.pred(tlp_x[ii])
    if ty>0:
        plt.plot(tlp_x1[ii],tlp_x2[ii], tshowpoint[int(ty)])
    else:
        plt.plot(tlp_x1[ii],tlp_x2[ii], tshowpoint[int(ty)]) 


plt.show()