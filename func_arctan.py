# 泰勒展开

print('本程序计算arcsin(x)的值.')

x=float(input('请输入x:'))

delta=float(input('请输入delta:'))

n =0

arcsinx = 0

 

def factorial(m):    #阶乘

    if m == 0:

        return 1

    else:

        result = 1

        for i in range(2,m+1):

            result = result*i

        return result

 

while(factorial(2*n)*x**(2*n+1)/(4**n*factorial(n)*factorial(n)*(2*n+1))>=delta):

    arcsinx += factorial(2*n)*x**(2*n+1)/(4**n*factorial(n)*factorial(n)*(2*n+1))

    n=n+1
 
print('arcsinx的近似值为：',arcsinx)

# arctanx..............

