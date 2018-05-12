#!/usr/bin/env python
# -*- coding: utf-8 -*-
#code:myhaspl@qq.com
#7-18.py
 
import numpy as np

x =np.matrix([[7,2,3],[3,7,17],[11,3,5]],dtype=np.float64)
y =np.matrix([28,40,44],dtype=np.float64).T
b=(x.T*x).I*x.T*y
print u"参数项矩阵为{0}".format(b)
i=0
cb=[]
while  i<3:
    cb.append(b[i,0])
    i+=1
temp_e=y-x*b
mye=temp_e.sum()/temp_e.size
e=np.matrix([mye,mye,mye]).T

print "y=%f*x1+%f*x2+%f*x3+%f"%(cb[0],cb[1],cb[2],mye)