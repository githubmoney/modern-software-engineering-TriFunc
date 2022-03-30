# Func_Arctanx函数实现：
import random
import math
pi = 3.141592653


def arctan(in1):
    x1 = in1
    delta = 0.000000001
    n = 0
    y = 0
    # 当x绝对值小于1时用泰勒展开进行计算
    if (x1 == -1) | (x1 == 1):
        t = x1
        n = 0
        m = 0
        while n < 100:
            m += (-1) ** n * t ** (2 * n + 1) / (2 * n + 1)
            n = n + 1
        # result = m * 180 / pi # 可以转角度
        m = format(m, '.9f')
        # w = format(result, '.9f') # 转角度输出
        return m
    if (x1 >= 0) and (x1 < 1):
        while x1 ** (2 * n + 1) / (2 * n + 1) >= delta:
            y += (-1) ** n * x1 ** (2 * n + 1) / (2 * n + 1)
            n += 1
    elif (x1 <= 0) and (x1 > -1):
        x2 = -x1
        while x2 ** (2 * n + 1) / (2 * n + 1) >= delta:
            y += (-1) ** n * x2 ** (2 * n + 1) / (2 * n + 1)
            n += 1
        y = -y
    # 当x绝对值大于1时，arctanx=pi/2-arctan(1/x)
    elif x1 > 1:
        x3 = 1 / x1
        while x3 ** (2 * n + 1) / (2 * n + 1) >= delta:
            y += (-1) ** n * x3 ** (2 * n + 1) / (2 * n + 1)
            n += 1
        y = pi / 2 - y
    else:
        x4 = 1 / -x1
        while x4 ** (2 * n + 1) / (2 * n + 1) >= delta:
            y += (-1) ** n * x4 ** (2 * n + 1) / (2 * n + 1)
            n += 1
        y = pi / 2 - y
        y = -y
    #return format(y, '.9f')
    return y


def ku(in2):

    return format(math.atan(in2), '.9f')


def test(angle):

    myArctan = arctan(angle)
    systemArctan = math.atan(angle)
    print(myArctan)
    print(systemArctan)
    minus = systemArctan - myArctan

    return minus


for i in range(1, 100):
    x = random.uniform(-10000, 10000)
    ans = test(x)
    flag = True
    if ans > 0.0001:
        flag = False
    print('input : %.5f' % x, "minus", '%.9f' % ans, flag)

