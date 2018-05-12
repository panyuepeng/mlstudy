#!/usr/bin/env python
#-*- coding: utf-8 -*-
#4-3.py
import cv2
import numpy as np

fn="test1.jpg"

if __name__ == '__main__':

    print 'loading %s ...' % fn
    img = cv2.imread(fn)
    sp=img.shape
    print sp
    #height
    sz1=sp[0]
    #width
    sz2=sp[1]
    print 'width:%d\nheight:%d'%(sz2,sz1)


