#!/usr/bin/env python
#-*- coding: utf-8 -*-
#8-3.py
#拟合sin*0.5+cos*0.5
import neurolab as nl
import numpy as np
import matplotlib.pyplot as plt
isdebug=False

#x和d样本初始化
train_x =[]
d=[]
samplescount=1000
myrndsmp=np.random.rand(samplescount)
for yb_i in xrange(0,samplescount):
    train_x.append([myrndsmp[yb_i]*4*np.pi-2*np.pi])
for yb_i in xrange(0,samplescount):
    d.append(np.sin(train_x[yb_i])*0.5+np.cos(train_x[yb_i])*0.5)

myinput=np.array(train_x)   
mytarget=np.array(d)

bpnet = nl.net.newff([[-2*np.pi, 2*np.pi]], [5, 1])
err = bpnet.train(myinput, mytarget, epochs=800, show=100, goal=0.02)

simd=[]
for xn in xrange(0,len(train_x)):
        simd.append(bpnet.sim([train_x[xn]])[0][0])
     

temp_x=[]
temp_y=simd
temp_d=[]
i=0
for mysamp in train_x:
     temp_x.append(mysamp[0])
     temp_d.append(d[i][0])
     i+=1
                 
x_max=max(temp_x)
x_min=min(temp_x)
y_max=max(max(temp_y),max(d))+0.2
y_min=min(min(temp_y),min(d))-0.2
    
plt.xlabel(u"x")
plt.xlim(x_min, x_max)
plt.ylabel(u"y")
plt.ylim(y_min, y_max)

lp_x1 = temp_x
lp_x2 = temp_y
lp_d = temp_d
plt.plot(lp_x1, lp_x2, 'r*')
plt.plot(lp_x1,lp_d,'bo')
plt.show()

