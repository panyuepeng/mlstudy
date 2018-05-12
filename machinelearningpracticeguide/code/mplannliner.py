#!/usr/bin/env python
#-*- coding: utf-8 -*-
#code:myhaspl@qq.com
#author:麦好
#2013-07-25
#mplannliner.py
import numpy as np
import math
import matplotlib.pyplot as plt


class Mplannliner:
        def __init__(self):
                self.b=1
                self.a0=0.1
                self.a=0.0
                self.r=20.0
                self.expect_e=0.05
                self.traincount=100
                self.testpoint=[]
        def testpoint_init(self):
                self.testpoint=[]
        def e_init(self,mye):
                self.expect_e=mye
        def samples_init(self,mysamples):
                my_x =[]
                my_d =[]
                my_w =[self.b] 
                myexamp=mysamples
                for mysmp in myexamp:
                        tempsmp=[1]+mysmp[0]
                        my_x.append(tempsmp)
                        my_d.append(mysmp[1])
                for i in range(len(my_x[0])-1):
                        my_w.append(0.0)        
                self.x = np.array(my_x)
                self.d = np.array(my_d)
                self.w = np.array(my_w)
        def a_init(self,mya):
                self.a0=mya
        def r_init(self,myr):
                self.r=myr
        def maxtry_init(self,maxc):
                self.traincount=maxc                
        def sgn(self,v):
                if v>0:
                        return 1
                else:
                        return -1
        def get_v(self,myw,myx):
                return self.sgn(np.dot(myw.T,myx))
        def neww(self,oldw,myd,myx,a,mycount):
                mye=self.get_e(oldw,myx,myd)
                self.a=self.a0/(1+mycount/float(self.r))
                return (oldw+a*mye*myx,mye)
        def get_e(self,myw,myx,myd):
                return myd-self.get_v(myw,myx)
        def train(self):         
                mycount=0
                while True:
                        mye=0
                        i=0          
                        for xn in self.x:
                                self.w,e=self.neww(self.w,self.d[i],xn,self.a,mycount)
                                i+=1
                                mye+=pow(e,2)
                        mye=math.sqrt(mye)
                        mycount+=1
                        print u"第%d次调整中。。。误差：%f"%(mycount,mye)   
                        if abs(mye)<self.expect_e or mycount>self.traincount:
                            if mycount>self.traincount:print "已经达到最大训练次数:%d"%mycount
                            print u"麦好   myhaspl@qq.com"
                            print u"http://blog.csdn.net/u010255642"
                            break
        def simulate(self,testdata):
                if self.get_v(self.w,np.array([1]+testdata))>0:
                    return 1
                else:
                    return -1
        def drawponint_add(self,point):
                self.testpoint.append(point)
            
        def draw2d(self):
                temp_x=[]
                temp_y=[]
                i=0
                for mysamp in self.x:
                                temp_x.append(mysamp[1])
                                temp_y.append(mysamp[2])
                                if self.d[i] > 0:
                                                plt.plot(mysamp[1],mysamp[2],"or")
                                else:
                                                plt.plot(mysamp[1],mysamp[2],"og")
                                i+=1
                mytestpointx=[]
                mytestpointy=[]
                for addpoint in self.testpoint:
                    if self.simulate(addpoint)==1:
                        plt.plot(addpoint[0],addpoint[1], '*r')
                    else:
                        plt.plot(addpoint[0],addpoint[1], '*g')
                    
                    mytestpointx.append(addpoint[0])
                    mytestpointy.append(addpoint[1])
                    
                x_max=max(max(temp_x),max(mytestpointx))+5
                x_min=min(min(temp_x),min(mytestpointx))
                y_max=max(max(temp_y),max(mytestpointy))+5
                y_min=min(min(temp_y),min(mytestpointy))
                if x_min >0:
                                x_min=0
                if y_min >0:
                                y_min=0      
                plt.xlabel(u"x1")
                plt.xlim(x_min, x_max)
                plt.ylabel(u"x2")
                plt.ylim(y_min, y_max)
                plt.title("ANN-LINER[red:+ green:-]\n[myhaspl@qq.com]http://blog.csdn.net/u010255642" )
                lp_x1 = [x_min, x_max]
                lp_x2 = []
                myb=self.w[0]
                myw1=self.w[1]
                myw2=self.w[2]
                myy=(-myb-myw1*lp_x1[0])/float(myw2)
                lp_x2.append(myy)
                myy=(-myb-myw1*lp_x1[1])/float(myw2)
                lp_x2.append(myy)
                plt.plot(lp_x1, lp_x2, 'b--')
                plt.show()










