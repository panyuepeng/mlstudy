#!/usr/bin/env python  
# -*- coding: utf-8 -*-
#code:myhaspl@qq.com 
#将文件隐藏在声音之中
#4-18.py
import wave
import pylab as pl
import numpy as np


#编码
print u'正在将文件编码进声音'
print "generate wav data...."
# 打开文档

fo = wave.open(r"pltest.wav", "wb") 
file_object = open('4-1.py')
try:
     all_the_text = file_object.read( )
finally:
     file_object.close( )

wdata=map(ord,all_the_text)
wdata=np.array(wdata)
lwdata=len(wdata)
# 设置波形参数
#采样率
framerate = 44100
#声道数
nchannels=2
#每位宽度
sampwidth=2
#长度
nframes =framerate*4

#振幅
base_amplitude = 200
max_amplitude=128*base_amplitude

#每个字符的间隔次数
interval=(nframes-10)/lwdata
#每周期样本数


wave_data=np.zeros((nframes), dtype=np.short)

count=0
myrand=np.random.rand(nframes)
for curpos in xrange(0,nframes):
    if curpos % interval==0 and count<lwdata:
        possamp=wdata[count]*base_amplitude-64*base_amplitude      
        count+=1       
    elif curpos%60==0:
        possamp=int(myrand[curpos]*max_amplitude-max_amplitude/2)
    else:
        possamp=0
    wave_data[curpos]=possamp
#写波形数据参数
print "save new wav files...."
str_data=wave_data.tostring()
fo.setnchannels(nchannels)
fo.setframerate(framerate)
fo.setsampwidth(sampwidth)
fo.setnframes(nframes)

fo.writeframes(str_data)
fo.close()    

# 绘制波形
wave_data.shape = -1, 2
wave_data = wave_data.T

time = np.arange(0, nframes/2)
pl.subplot(211)
pl.plot(time, wave_data[0], c="r")
pl.subplot(212)
pl.plot(time, wave_data[1], c="g")
pl.xlabel("time (seconds)")


#解码
new_wdata=[]
print u'正在从声音解码文件'
fi = wave.open(r"pltest.wav", "rb")  
fi_params=fi.getparams()  
fi_nframes = fi_params[3]  
fi_str_data=fi.readframes(fi_nframes) 
fi_wave_data= np.fromstring(fi_str_data, dtype=np.short)
count=0
for curpos in xrange(0,nframes):
    if curpos % interval==0 and count<lwdata:
        possamp=(fi_wave_data[curpos]+64*base_amplitude)/base_amplitude
        new_wdata.append(possamp)
        count+=1 
my_the_text="".join(map(chr,new_wdata))
file_object = open('mytext.txt', 'w')
file_object.write(my_the_text)
file_object.close( )
pl.show()
