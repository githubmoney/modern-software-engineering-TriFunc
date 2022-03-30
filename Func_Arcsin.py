from decimal import Decimal
def arcsinx(x):
     x=float(x)
     #arcsin定义域为[-1,1]，大于1或者小于-1超出定义域
     if x>1 or x<-1:
         #print('错误，请输入-1到1间的数')
          return print('错误，请输入-1到1间的数')

     if x>=0 and x<=1:
          arcsinx=0
          n = 0
          #定义计算精度
          delta = 0.000000001
          #泰勒展开近似计算
          while (Decimal(factorial(2*n))*Decimal(x)**Decimal((2*n+1))/(4**Decimal(n)*Decimal(factorial(n))*Decimal(factorial(n))*Decimal((2*n+1))) >= delta):
                arcsinx += Decimal(factorial(2*n))*Decimal(x)**Decimal((2*n+1))/(4**Decimal(n)*Decimal(factorial(n))*Decimal(factorial(n))*Decimal((2*n+1)))
                n = n + 1
          return print(format(arcsinx, '.9f'))
     if x>=-1 and x<0:
          arcsinx = 0
          n = 0
          #定义计算精度
          delta = 0.000000001
          x=-x
          #泰勒展开近似计算
          while (Decimal(factorial(2*n))*Decimal(x)**Decimal((2*n+1))/(4**Decimal(n)*Decimal(factorial(n))*Decimal(factorial(n))*Decimal((2*n+1))) >= delta):
                arcsinx += Decimal(factorial(2*n))*Decimal(x)**Decimal((2*n+1))/(4**Decimal(n)*Decimal(factorial(n))*Decimal(factorial(n))*Decimal((2*n+1)))
                n = n + 1
          arcsinx = -arcsinx
          return print(format(arcsinx, '.9f'))

def factorial(m):    #阶乘
     if m == 0:
         return 1
     else:
         result = 1
         for i in range(2,m+1):
             result = result*i
         return result
x = float(input('请输入x:'))
y = arcsinx(x)

