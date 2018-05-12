#!/usr/bin/env python
# -*- coding: utf-8 -*-
#code:myhaspl@qq.com
#7-17.py
 
import matplotlib.pyplot as plt
x =[1,2,3,3,6,12,11]
y =[3,5,8,5,12,26,20]
average_x=float(sum(x))//len(x)
average_y=float(sum(y))/len(y)
x_sub=map((lambda x:x-average_x),x)
y_sub=map((lambda x:x-average_y),y)
x_sub_pow2=map((lambda x:x**2),x_sub)
y_sub_pow2=map((lambda x:x**2),y_sub)
x_y=map((lambda x,y:x*y),x_sub,y_sub)
a=float(sum(x_y))/sum(x_sub_pow2)
b=average_y-a*average_x
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x, y, '*')
plt.plot([0,15],[0*a+b,15*a+b])
plt.grid()
plt.title("{0}*x+{1}".format(a,b))
plt.show()