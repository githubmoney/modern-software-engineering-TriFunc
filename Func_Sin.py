import math
import random
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

def sin(a):  #a是弧度
    #把a的范围取到0-2pi
    if a <= (pi/16384):
        return a
    else:
        negitive = a < 0
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
                    return -(y/math.sqrt((x*x+y*y)))
                else:
                    return (y/math.sqrt((x*x+y*y)))
            else:
                theta -= angle[i]
                x = orix
                y = oriy
        if(negitive):
            return -(y/math.sqrt((x*x+y*y)))
        else:
            return (y/math.sqrt((x*x+y*y)))



# def test(angle):
#     mySin = sin(angle)           
#     systemSin = math.sin(angle)  
#
#     minus = systemSin - mySin    
#
#     return minus


# for i in range(100):
#     angleIn = random.uniform(0, 100) 
#     ans = test(angleIn)              
#     flag = True
#     if ans > 0.001:
#         flag = False
#     print('input: %.5f' %angleIn, "minus:", '%.5f' %ans, flag)
