# from math import degrees, radians
from math import pi


# 角度转弧度函数
def angel2radian(angel):
    radian = angel * pi / 180
    return format(radian, '.9f')


# 弧度转角度函数
def radian2angel(radian):
    angel = radian * 180 / pi
    return format(angel, '.9f')


print("=====1.输入度数=====")
print("=====2.输入弧度=====")
choose_num = int(input("选择输入类型："))
if choose_num == 1:
    # 输入角度转换为弧度并输出
    angel_input = float(input("请输入一个角度："))
    radian_output = angel2radian(angel_input)
    print("自定义函数计算结果：", radian_output)
#   print("库函数计算结果：", radians(angel_input))  # 调用库函数测试自定义函数运算结果
elif choose_num == 2:
    # 输入弧度转换为角度并输出
    radian_input = float(input("请输入一个弧度："))
    angel_output = radian2angel(radian_input)
    print("自定义函数计算结果：", angel_output)
#   print("库函数计算结果：", degrees(radian_input))  # 调用库函数测试自定义函数运算结果
else:
    print("输入错误！！！")
