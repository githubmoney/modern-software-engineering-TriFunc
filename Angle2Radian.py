# from math import degrees, radians
from math import pi
import math
import random


# 角度转弧度函数
def angel2radian(angel):
    radian = angel * pi / 180
    # return format(radian, '.9f')
    return radian


"""# 弧度转角度函数
def radian2angel(radian):
    angel = radian * 180 / pi
    return format(angel, '.9f')"""
# angel_input = float(input("请输入一个角度："))
# y = angel2radian(angel_input)
# print("幅度计算结果：", radian_output)
# print("库函数计算结果：", math.radians(angel_input))
"""radian_input = float(input("请输入一个弧度："))
angel_output = radian2angel(radian_input)
print("角度计算结果：", angel_output)
print("库函数计算结果：", math.degrees(radian_input))"""


def test(angle):
    myAngel2radian = angel2radian(angle)
    systemmyAngel2radian = math.radians(angle)
    minus = systemmyAngel2radian - myAngel2radian

    return minus


for i in range(1, 100):
    x = random.uniform(-10000, 10000)
    ans = test(x)
    flag = True
    if ans > 0.001:
        flag = False
    print('input : %.5f' % x, "minus", '%.9f' % ans, flag)
