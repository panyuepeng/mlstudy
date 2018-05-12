#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#9-9.py
#PCA加上ann人工神经网络识别图片类型
import numpy as np
import pylab as pl
import neurolab as nl
import cv2
import mlpy





print u'正在处理中'

def getresult(simjg):
    jg=[]
    for j in xrange(0,len(simjg)):
        maxjg=-2
        nowii=0
        for i in xrange(0,len(simjg[0])):
            if simjg[j][i]>maxjg:
                maxjg=simjg[j][i]
                nowii=i
        jg.append(len(simjg[0])-nowii)
    return jg


def readpic(fn):
    #返回图片特征码
    fnimg = cv2.imread(fn)
    img=cv2.resize(fnimg,(500,400))
    w=img.shape[1]  
    h=img.shape[0]  
    w_interval=w/20
    h_interval=h/10    
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
sp_d=[]
sp_d.append([0,0,1])
sp_d.append([0,1,0])
sp_d.append([1,0,0])
#读取图片
for ii in xrange(1,4):
    for jj in xrange(1,4):
        fn='p'+str(ii)+'-'+str(jj)+'.png'
        pictz=readpic(fn)
        train_x.append(pictz)
        d.append(sp_d[ii-1])


myinput=np.array(train_x) 
mytarget=np.array(d)
mymax=np.max(myinput)
netminmax=[]
for i in xrange(0,len(myinput[0])):
    netminmax.append([0,mymax])

print u'\n正在建立神经网络'
bpnet = nl.net.newff(netminmax, [5, 3])

print u'\n训练神经网络中...'
err = bpnet.train(myinput, mytarget, epochs=800, show=5, goal=0.2)
if err[len(err)-1]>0.4:
    print u'\n训练神经网络失败...\n'
else:
    print u'\n训练神经网络完毕'        
    pl.subplot(111)
    pl.plot(err)  
    pl.xlabel('Epoch number')
    pl.ylabel('error (default SSE)')
    print u"对样本进行测试"
    simd= bpnet.sim(myinput)
    mysimd=getresult(simd)
    print mysimd
    print u"进行仿真"
    testpictz=np.array([readpic('ptest3.png')])
    simtest=bpnet.sim(testpictz) 
    mysimtest=getresult(simtest)
    print "===ptest3.png==="
    print simtest
    print mysimtest
    testpictz=np.array([readpic('ptest1.png')])
    simtest=bpnet.sim(testpictz)
    mysimtest=getresult(simtest)
    print "===ptest1.png==="
    print simtest
    print mysimtest   
    testpictz=np.array([readpic('ptest2.png')])
    simtest=bpnet.sim(testpictz)
    mysimtest=getresult(simtest)
    print "===ptest2.png==="
    print simtest
    print mysimtest     
    testpictz=np.array([readpic('ptest21.png')])
    simtest=bpnet.sim(testpictz)
    mysimtest=getresult(simtest)
    print "===ptest21.png==="
    print simtest
    print mysimtest      
    testpictz=np.array([readpic('ptest22.png')])
    simtest=bpnet.sim(testpictz)
    mysimtest=getresult(simtest)
    print "===ptest22.png==="
    print simtest
    print mysimtest     
    pl.show()
