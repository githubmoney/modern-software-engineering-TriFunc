# 泰勒展开式计算arctanx
def arctan(x):
    
    x = x
    n = 0
    m = 0
    while (n < 100):
        m += (-1) ** n * x ** (2 * n + 1) / (2 * n + 1)
        n = n + 1

    m = format(m, '.9f')

    return m

