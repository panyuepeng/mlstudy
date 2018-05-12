#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#8-4.py
import numpy as np
import pylab as pl
import neurolab as nl



print u'正在处理中'

#x和d样本初始化
train_x =[]
d=[]
f = open("cubage.csv")  
try:  
    f_text = f.read( ) 
finally:  
    f.close( ) 
x_text=f_text.split('\n')
for line_i in xrange(0,len(x_text)):
    line=x_text[line_i]
    if line_i>1 and len(line)>0:
        train_x.append([])
        hdata=line.split(',')
        train_x[line_i-2].append(float(hdata[0]))
        d.append([float(hdata[1])])
    


myinput=np.array(train_x)  
mytarget=np.array(d)
mymax=np.max(d)
tz=(0.1**(len(str(int(mymax)))))*5
myinput=myinput
mytarget=tz*mytarget
netminmax=[0,np.max(myinput)]
print u'\n正在建立神经网络'
bpnet = nl.net.newff([netminmax], [5, 1])

print u'\n训练神经网络中...'
err = bpnet.train(myinput, mytarget, epochs=800, show=5, goal=0.0001)
if err[len(err)-1]>0.0001:
    print u'\n训练神经网络失败...\n'
else:
    print u'\n训练神经网络完毕'    
    pl.subplot(211)
    pl.plot(err)  
    pl.xlabel('Epoch number')
    pl.ylabel('error (default SSE)')
    #对样本进行测试
    simd= bpnet.sim(myinput)
    temp_x=myinput
    temp_d=mytarget
    simd/=tz
    temp_y=simd
    temp_d/=tz  

    #对未知样本进行测试
    myinputtest=[[6],[9],[17],[20]]
    testsimd= bpnet.sim(myinputtest)
    end_x=np.array(myinputtest)
    testsimd/=tz
    end_y=testsimd
 
    
                  
    x_max=np.max(temp_x)
    x_min=np.min(temp_x)-5
    y_max=np.max(temp_y)+2  
    y_min=np.min(temp_y)
    
    pl.subplot(212)
    pl.xlabel(u"x")
    pl.xlim(x_min, x_max)
    pl.ylabel(u"y")
    pl.ylim(y_min, y_max)
    lp_x1 = temp_x
    lp_x2=temp_y

    lp_d = temp_d
    pl.plot(lp_x1, lp_x2, 'g-')
    pl.plot(end_x, end_y, 'ro')
    pl.plot(lp_x1,lp_d,'b*')