# Func_Arctanx函数实现：
# import random
# import math
pi = 3.141592653


def arctan(in1):
    delta = 0.000000001
    n = 0
    y = 0
    # 当 |x| <= 1时用泰勒展开进行计算
    if (in1 == -1) | (in1 == 1):
        t = in1
#         n = 0
#         m = 0
        while n < 1000000000:
            y += (-1) ** n * t ** (2 * n + 1) / (2 * n + 1)
            n = n + 1
        # result = m * 180 / pi # 可以转角度
        # w = format(result, '.9f') # 转角度输出
        return y
    elif (in1 >= 0) and (in1 < 1):
        while in1 ** (2 * n + 1) / (2 * n + 1) >= delta:
            y += (-1) ** n * in1 ** (2 * n + 1) / (2 * n + 1)
            n += 1
    elif (in1 <= 0) and (in1 > -1):
        x1 = -in1
        while x1 ** (2 * n + 1) / (2 * n + 1) >= delta:
            y += (-1) ** n * x1 ** (2 * n + 1) / (2 * n + 1)
            n += 1
        y = -y
    # 当|x| > 1时，arctanx=pi/2-arctan(1/x)
    elif in1 > 1:
        x2 = 1 / in1
        while x2 ** (2 * n + 1) / (2 * n + 1) >= delta:
            y += (-1) ** n * x2 ** (2 * n + 1) / (2 * n + 1)
            n += 1
        y = pi / 2 - y
    else:
        x3 = 1 / -in1
        while x3 ** (2 * n + 1) / (2 * n + 1) >= delta:
            y += (-1) ** n * x3 ** (2 * n + 1) / (2 * n + 1)
            n += 1
        y = pi / 2 - y
        y = -y
    #return format(y, '.9f')
    return y


# 测试函数
# def test(angle):
#     myArctan = arctan(angle)
#     systemArctan = math.atan(angle)
#     print(myArctan)
#     print(systemArctan)
#     minus = systemArctan - myArctan

#     return minus


# for i in range(1, 100):
#     x = random.uniform(-10000, 10000)
#     ans = test(x)
#     flag = True
#     if ans > 0.001:
#         flag = False
#     print('input : %.5f' % x, "minus", '%.9f' % ans, flag)
