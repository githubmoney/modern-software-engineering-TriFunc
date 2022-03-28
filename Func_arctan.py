pi = 3.1415926535897932
def arctan(x):
        if x > 1 and x < -1:
            return print("幅度和角度分别是：", None)
        else:
            if x >= -1 and x <= 1:
                x = x
                n = 0
                m = 0
                while (n < 100):
                    m += (-1) ** n * x ** (2 * n + 1) / (2 * n + 1)
                    n = n + 1
                result = m * 180 / pi
                m = format(m, '.9f')
                w = format(result, '.9f')
                return m, w
    #return m
m = float(input('请输入x:'))
print("幅度和角度分别是：", arctan(m))

"""print("输出幅度：", format(arctan(m), '.9f'))
result = arctan(m) * 180 / pi
print("输出角度:", format(result, '.9f'))"""