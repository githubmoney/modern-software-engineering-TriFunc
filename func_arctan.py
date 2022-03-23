#!/usr/bin/python

# 调用函数math可以实现arctan函数功能，例如下所示

import math

print ("atan(0.64) : ",  math.atan(0.64))
print ("atan(0) : ",  math.atan(0))
print ("atan(10) : ",  math.atan(10))
print ("atan(-1) : ",  math.atan(-1))
print ("atan(1) : ",  math.atan(1))

'''
(base) lh@lh:~/文档$ python func_arctan.py

atan(0.64) :  0.5693131911006619
atan(0) :  0.0
atan(10) :  1.4711276743037347
atan(-1) :  -0.7853981633974483
atan(1) :  0.7853981633974483

'''
# ================================================

# ===========自己写实现arctan函数==================
e = 2.718281828459045

pi = 3.141592653589793

tau = 6.283185307179586


def atan(*args, **kwargs):  # real signature unknown
    """ Return the arc tangent (measured in radians) of x. """
    pass


def atan2(*args, **kwargs):  # real signature unknown
    """
    Return the arc tangent (measured in radians) of y/x.

    Unlike atan(y/x), the signs of both x and y are considered.
    """
    pass


def atanh(*args, **kwargs):  # real signature unknown
    """ Return the inverse hyperbolic tangent of x. """
    pass

#=================================================
