import math

pi = 3.1415926535897932
angle =          [pi/4,pi/8,pi/16,
                  pi/32,pi/64,pi/128,
                  pi/256,pi/512,pi/1024,
                  pi/2048,pi/4096,pi/8192,pi/16384]

tang =        [1,0.4142135623731,0.19891236737966,
               0.098491403357164,0.049126849769467,
               0.024548622108925,0.012272462379566,
               0.0061360001576234,0.0030679712014227,
               0.0015339819910887,0.00076699054434309,
               0.00038349521577144,0.00019174760083571]

def Func_Cos(a):
    #把a的范围取到0-2pi
    if a <= (pi/16384):
        return format(1-a, '.9f')
    else:
        #negitive = a < 0
        negitive = a > pi/2
        x = 10
        y = 0
        theta = 0
        for i in range(12):
            while(theta < a):
                orix = x
                oriy = y
                x = orix - tang[i] * oriy
                y = tang[i] * orix + oriy
                theta += angle[i]
            if(theta == a):
                if(negitive):
                    return format((x/math.sqrt((x*x+y*y))), '.9f')
                else:
                    return format(-(x/math.sqrt((x*x+y*y))), '.9f')
            else:
                theta -= angle[i]
                x = orix
                y = oriy
        if(negitive):
            return format(x/math.sqrt((x*x+y*y)), '.9f')
        else:
            return format(-(x/math.sqrt((x*x+y*y))), '.9f')


cos_in = float(input('cos_in = '))
print("cos_out = ", Func_Cos(cos_in))
