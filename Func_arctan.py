# 泰勒展开式计算arctanx
def arctan(x):
    print("\n")
    print("==========输入ｘ的取值（|x| < 1）===============")
    print('本程序计算arctan(x)的值:')
    x = float(input('请输入x:'))
    n = 0
    m = 0
    while (n < 100):
        m += (-1) ** n * x ** (2 * n + 1) / (2 * n + 1)
        n = n + 1

    m = format(m, '.9f')

    return m
print(arctan(0.015))
