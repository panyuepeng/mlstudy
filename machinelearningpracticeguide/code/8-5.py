#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#8-5.py
import numpy as np
import wave
import pylab as pl
import copy

  
print 'working...' 



print "read wav data...."
err=[]
# 打开WAV文档
f = wave.open(r"speak.wav", "rb")
fo = wave.open(r"wait_jg.wav", "wb")
fi=wave.open(r"back.wav", "rb")
fend=wave.open(r"end_jg.wav", "wb")

# 读取波形数据
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = f.readframes(nframes)

fi_params=fi.getparams()
fi_nframes = fi_params[3]
fi_str_data=fi.readframes(fi_nframes)

#将波形数据转换为数组，并更改
print "update wav data...."
wave_data = np.fromstring(str_data, dtype=np.short)
fi_wave_data= np.fromstring(fi_str_data, dtype=np.short)




#复制并将背景音乐的振幅(音量)在一个随机的基数基础上
#稍微变动后，与语音合并
#前面预留一段经过波形调整后的背景音乐，以供线性神经网络拟合
emptywdata=np.zeros(framerate, dtype=np.short)
new_wave_data=np.hstack((emptywdata,wave_data,wave_data,wave_data,wave_data,wave_data,wave_data,wave_data,wave_data))
wave_data =copy.deepcopy(new_wave_data)
nframes*=8
nframes+=framerate/2
temp_wavedata=np.hstack((fi_wave_data,fi_wave_data))[:len(new_wave_data)]
backrnd=np.random.rand(len(new_wave_data))*10-5
backbase=np.random.rand()*2+1
temp_wavedata=temp_wavedata*backbase+backrnd
new_wave_data=temp_wavedata+new_wave_data

new_wave_data=np.array(new_wave_data)
new_wave_data =new_wave_data.astype(wave_data.dtype)
new_str_data=new_wave_data.tostring()
#写波形数据参数
print "save mix wav files...."
fo.setnchannels(nchannels)
fo.setframerate(framerate)
fo.setsampwidth(sampwidth)
fo.writeframes(new_str_data)




#线性逼近前段噪声
b=1
a0=5e-1
a=0.0
r=1.5
x=[]
d=[]
ii=0
for audio_i in xrange(0,framerate/2):
    if fi_wave_data[audio_i]!=0.:
        x.append([])
        x[ii].append(1)
        x[ii].append(fi_wave_data[audio_i])
        d.append(new_wave_data[audio_i])
        ii+=1
    if ii>100:
        break
x=np.array(x)
d=np.array(d)

w=np.random.rand(2)*np.mean(x)#np.array([b,0])
expect_e=15
maxtrycount=10000
mycount=0
def sgn(v):
    return  v
def get_v(myw,myx):
        return sgn(np.dot(myw.T,myx))
def neww(oldw,myd,myx,a):
        mye=get_e(oldw,myx,myd)
        a=a0/(1+float(mycount)/r)
        return (oldw+a*mye*myx,mye)
def get_e(myw,myx,myd):
        return myd-get_v(myw,myx)



while True:
        mye=0.
        i=0          
        for xn in x:
                w,e=neww(w,d[i],xn,a)
                i+=1
                mye+=pow(e,2)
        mye=np.sqrt(mye)
        mycount+=1
        err.append(mye)
        print u"第 %d 次调整后的权值："%mycount
        print w
        print u"误差：%f"%mye        
        if abs(mye)<expect_e or mycount>maxtrycount:break 
               
print "w:[%f,%f]"%(w[0],w[1])

#复制并除去背景声音

jg_wave_data=copy.deepcopy(new_wave_data)
jg_temp_wavedata=np.hstack((fi_wave_data,fi_wave_data))[:len(new_wave_data)]
jg_temp_wavedata=jg_temp_wavedata[:len(new_wave_data)]*w[1]+w[0]
jg_wave_data=jg_wave_data-jg_temp_wavedata

for jg_i in xrange(0,len(jg_wave_data)):
    if abs(jg_wave_data[jg_i])<500:
        jg_wave_data[jg_i]=0
jg_wave_data[:framerate]=0
    
jg_wave_data =jg_wave_data.astype(wave_data.dtype)
jg_str_data=jg_wave_data.tostring()

print "save output wav...."
fend.setnchannels(nchannels)
fend.setframerate(framerate)
fend.setsampwidth(sampwidth)
fend.writeframes(jg_str_data)

# 绘制波形
time = np.arange(0, nframes) * (1.0 / framerate)
wave_data.shape = -1, 2
wave_data = wave_data.T

pl.subplot(321)
pl.plot(time, wave_data[0])
pl.subplot(322)
pl.plot(time, wave_data[1], c="g")
pl.xlabel("time (seconds)")

 
# 绘制波形
new_wave_data.shape = -1, 2
new_wave_data =new_wave_data.T

pl.subplot(323)
pl.plot(time,new_wave_data[0])
pl.subplot(324)
pl.plot(time, new_wave_data[1], c="g")
pl.xlabel("time (seconds)")
pl.show()

# 绘制波形
jg_wave_data.shape = -1, 2
jg_wave_data =jg_wave_data.T

pl.subplot(325)
pl.plot(time,jg_wave_data[0])
pl.subplot(326)
pl.plot(time, jg_wave_data[1], c="g")
pl.xlabel("time (seconds)")
pl.show()


