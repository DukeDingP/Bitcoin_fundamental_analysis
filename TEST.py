import numpy as np
from scipy.optimize import leastsq

# 二次函数的标准形式
def func(params, x):
    a, b, c = params
    return a * x * x + b * x + c

# 误差函数，即拟合曲线所求的值与实际值的差
def error(params, x, y):
    return func(params, x) - y

# 输出最后的结果

def solution(x,y):
    p0 = [10, 10, 10]
    x=np.array(x)
    y=np.array(y)
    Para = leastsq(error, p0, args=(x, y))
    a, b, c = Para[0]
    print ("a=",a," b=",b," c=",c)
    print ("cost:" + str(Para[1]))
    print ("求解的曲线是:")
    print("y="+str(a)+"x*x+"+str(b)+"x+"+str(c))
    return a,b,c

y=[116.99245672871578,556.7015756855221,1791.844638955089,3411.5351319750976]
x=[1,2,3,4]
a,b,c=solution(x,y)

import matplotlib.pyplot as plt
plt.plot(x,y)
x=np.linspace(0,6,100) ##在0-15直接画100个连续点
y=a*x*x+b*x+c ##函数式
plt.plot(x,y,color="red",label="solution line",linewidth=2)
plt.show()
print(a*4*4+b*4+c)