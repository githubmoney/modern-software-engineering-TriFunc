# 泰勒展开式计算arctanx
print("\n")
print("==========输入ｘ的取值（|x| < 1）===============")
print('本程序计算arctan(x)的值:')
x = float(input('请输入x:'))
n = 0
arctanx = 0
while (n < 100):
    arctanx += (-1)**n*x**(2*n+1)/(2*n+1)
    n = n+1

arctanx = format(arctanx, '.9f')
print('arcsinx的近似值为：', arctanx)
