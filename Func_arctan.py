from math import pi
from math import atan


def arctan(input):
    x1 = input
    delta = 0.000000001
    n = 0
    y = 0
    # 当x绝对值小于1时用泰勒展开进行计算
    if x1 >= 0 and x1 <= 1:
        while x1 ** (2 * n + 1) / (2 * n + 1) >= delta:
            y += (-1) ** n * x ** (2 * n + 1) / (2 * n + 1)
            n += 1
    elif x1 <= 0 and x1 >= -1:
        x2 = -x1
        while x2 ** (2 * n + 1) / (2 * n + 1) >= delta:
            y += (-1) ** n * x2 ** (2 * n + 1) / (2 * n + 1)
            n += 1
        y = -y
    # 当x绝对值大于1时，arctanx=pi/2-arctan(1/x)
    elif x > 1:
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
    return format(y, '.9f')


x = float(input('请输入x:'))
print("自定义函数输出结果：", arctan(x))
print("库函数输出结果：", atan(x))



