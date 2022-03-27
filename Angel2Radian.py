import math


def angel2radian(angel):
    radian = angel * math.pi / 180
    return radian


def radian2angel(radian):
    angel = radian * 180 / math.pi
    return angel


angel_input = float(input("请输入一个角度："))
radian_output = angel2radian(angel_input)
print("自定义函数计算结果：", radian_output)
print("库函数计算结果：", math.radians(angel_input))

radian_input = float(input("请输入一个弧度："))
angel_output = radian2angel(radian_input)
print("自定义函数计算结果：", angel_output)
print("库函数计算结果：", math.degrees(radian_input))