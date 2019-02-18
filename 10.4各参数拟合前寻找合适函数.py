import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import leastsq
a=[8.647840722195095e-05,1.0260452073204255e-05,4.023404606469743e-06,2.538070543559161e-06]
b=[116.99245672871578,556.7015756855221,1791.844638955089,3411.5351319750976]
c=[-1.41611047980905,1.7001965056173347,5.614204268644582,8.222363426949228]

x=[1,2,3]
def func(x, a, b, c):
    return a*(x-b)**2+c
def func1(x,a,b):
    return a*x+b
def func_ex(x, a, b):
    return x**a+b
popt, pcov = curve_fit(func,a,[1,2,3])
a4=[func_ex(i, popt[0], popt[1]) for i in x]
popt, pcov = curve_fit(func,b,[1,2,3])
b4=[func(i, popt[0], popt[1], popt[2]) for i in x]
popt, pcov = curve_fit(func1,c,[1,2,3])
c4=[func1(i, popt[0], popt[1]) for i in x]


#二次拟合



plt.plot(x,a)
plt.plot(x,a4)
plt.show()
plt.plot(x,b)
plt.plot(x,b4)
plt.show()
plt.plot(x,c)
plt.plot(x,c4)
plt.show()

