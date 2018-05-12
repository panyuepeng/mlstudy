#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#7-9.py
import mplannliner as nplann                         
traindata1=[[[9,25],-1],[[5,8],-1],[[15,31],-1],[[35,62],-1],[[19,40],-1],[[28,65],1],[[20,59],1],[[9,41],1],[[12,60],1],[[2,37],1]]
myann=nplann.Mplannliner()
#样本初始化
myann.samples_init(traindata1)
#学习率初始化
myann.a_init(0.1)
#搜索时间常数初始化
myann.r_init(50)
#最大训练次数
myann.maxtry_init(500)
#期望最小误差
myann.e_init(0.05)
#训练
myann.train()
#仿真，测试，对未知样本分类
myc=myann.simulate([35,68])
print "[35,68]"
if myc==1:
    print u"正类"
else:
    print u"负类"

#将测试点在最终效果图上显示出来，将它加入drawponint集，测试点表现为"*",并且色彩由其最终的分类结果而决定
myann.drawponint_add([35,68])
myc=myann.simulate([35,82])
print "[35,82]"
if myc==1:
    print u"正类"
else:
    print u"负类"
myann.drawponint_add([35,82])    
myann.draw2d()

#下面直接使用默认参数进行训练
traindata2=[[[9,25,30],-1],[[5,8,12],-1],[[15,31,49],-1],[[35,62,108],-1],[[19,40,60],-1],[[28,65,98],1],[[20,59,72],1],[[9,41,38],1],[[12,60,46],1],[[2,37,18],1]]
myann2=nplann.Mplannliner()
myann2.samples_init(traindata2)
myann2.train()
myc=myann2.simulate([35,68,110])
print "[35,68,110]"
if myc==1:
    print u"正类"
else:
    print u"负类"