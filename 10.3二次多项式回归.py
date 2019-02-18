from scipy.optimize import curve_fit
import numpy as np
def func(x,a,b):
    return np.log(x)/np.log(a)+b

b1= 116.99245672871578
c1= -1.41611047980905
b2= 556.7015756855221
c2= 1.7001965056173347
b3= 1791.844638955089
c3= 5.614204268644582

popt,pcov = curve_fit(func,[b1,b2,b3],[c1,c2,c3])