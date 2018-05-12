#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#10-4.py

import numpy as np
import jieba
import copy


ftest1fn='mobile2.txt'
ftest2fn='war1.txt'
sampfn='war2.txt'

def get_cossimi(x,y):
    myx=np.array(x)
    myy=np.array(y)
    cos1=np.sum(myx*myy)
    cos21=np.sqrt(sum(myx*myx))
    cos22=np.sqrt(sum(myy*myy))
    return cos1/float(cos21*cos22)

    
if __name__ == '__main__':

    print
    print 'loading  ...'
    print 'working',
    
    f1 = open(sampfn)  
    try:  
        f1_text = f1.read( ) 
        f1_text=unicode(f1_text,'utf-8')
    finally:  
        f1.close( ) 
    f1_seg_list = jieba.cut(f1_text)
    #第一个待测试数据

    ftest1 = open(ftest1fn)  
    try:  
        ftest1_text = ftest1.read( ) 
        ftest1_text=unicode(ftest1_text,'utf-8')
    finally:  
        ftest1.close( ) 
    ftest1_seg_list = jieba.cut(ftest1_text)
    #第二个待测试数据    
    ftest2 = open(ftest2fn)  
    try:  
        ftest2_text = ftest2.read( ) 
        ftest2_text=unicode(ftest2_text,'utf-8')
    finally:  
        ftest2.close( ) 
    ftest2_seg_list = jieba.cut(ftest2_text)
    

    #读取样本文本
    #去除停用词，同时构造样本词的字典
    f_stop = open('stopwords.txt')  
    try:  
        f_stop_text = f_stop.read( )
        f_stop_text=unicode(f_stop_text,'utf-8')
    finally:  
        f_stop.close( ) 
    f_stop_seg_list=f_stop_text.split('\n')

    test_words={}
    all_words={}
    for  myword in f1_seg_list:
        print ".",
        if not(myword.strip() in f_stop_seg_list):
            test_words.setdefault(myword,0)
            all_words.setdefault(myword,0)
            all_words[myword]+=1
            
            
    #读取待测试文本
    mytest1_words=copy.deepcopy(test_words)
    for  myword in ftest1_seg_list:
        print ".",
        if not(myword.strip() in f_stop_seg_list):
            if mytest1_words.has_key(myword):
                mytest1_words[myword]+=1
    
    mytest2_words=copy.deepcopy(test_words)
    for  myword in ftest2_seg_list:
        print ".",
        if not(myword.strip() in f_stop_seg_list):
            if mytest2_words.has_key(myword):
                mytest2_words[myword]+=1                
    #计算样本与待测试文本的余弦相似度
    sampdata=[]
    test1data=[]
    test2data=[]
    for key in all_words.keys():
        sampdata.append(all_words[key])
        test1data.append(mytest1_words[key])
        test2data.append(mytest2_words[key])
    test1simi=get_cossimi(sampdata,test1data)
    test2simi=get_cossimi(sampdata,test2data)
    

    print u"%s与样本[%s]的余弦相似度:%f"%(ftest1fn,sampfn,test1simi)
    print u"%s与样本[%s]的余弦相似度:%f"%(ftest2fn,sampfn,test2simi) 
                
    
                
    


    

    
 
    
