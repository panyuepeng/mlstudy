#!/usr/bin/env python
# -*- coding: utf-8 -*-
#code:myhaspl@qq.com
#7-21.py 
#y=b1*x1+b2*x2+b3*(x1^2)+b4*(x2^2)+b5*x1*x2
import numpy as np

z=np.matrix([1.4,1.9,1.7,0.8,1.1]).T
myx =np.matrix([[7,3],[3,17],[11,5]],dtype=np.float64)
x = np.matrix([[myx[0,0],myx[0,1],myx[0,0]**2,myx[0,1]**2,myx[0,0]*myx[0,1]],\
               [myx[1,0],myx[1,1],myx[1,0]**2,myx[1,1]**2,myx[1,0]*myx[1,1]],\
               [myx[2,0],myx[2,1],myx[2,0]**2,myx[2,1]**2,myx[2,0]*myx[2,1]]],\
               dtype=np.float64)
y =x*z
wn=np.linalg.pinv(x.T*x)
b=wn*x.T*y
print u"参数项矩阵为{0}".format(b)
i=0
cb=[]
while  i<5:
    cb.append(b[i,0])
    i+=1
temp_e=y-x*b
mye=temp_e.sum()/temp_e.size
e=np.matrix([mye,mye,mye]).T

print "y=%f*x1+%f*x2+%f*(x1^2)+%f*(x2^2)+%f*x1*x2+%f"%(cb[0],cb[1],cb[2],cb[3],cb[4],mye)