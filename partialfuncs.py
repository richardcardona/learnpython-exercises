#!/usr/bin/env python

from functools import partial

def multiply(x,y):
    return x * y

# create a new function that multiplies by 2
dbl = partial(multiply,2)
print dbl(4)

def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x

p = partial(func,5,6,7)
print p(8)
