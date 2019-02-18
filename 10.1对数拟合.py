#对数拟合 提示: Covariance of the parameters could not be estimated ategory=OptimizeWarning)
from scipy.optimize import curve_fit

import matplotlib.pyplot as plt

import numpy as np


def func(x, a, b, c):
    return a * np.exp(-b * x) + c


xdata = np.linspace(0,332,332)
print(len(xdata))
y = func(xdata, 2.5, 1.3, 0.5)

ydata = y + 0.2 * np.random.normal(size=len(xdata))

plt.plot(xdata, y, 'b-')

popt, pcov = curve_fit(func, xdata, ydata)

# popt数组中，三个值分别是待求参数a,b,c

y2 = [func(i, popt[0], popt[1], popt[2]) for i in xdata]

plt.plot(xdata, y2, 'r--')
plt.show()

print(popt)


def fund(x, a, b):
    return x ** a + b


xdata = np.linspace(0, 4, 50)

y = fund(xdata, 2.5, 1.3)

ydata = y + 4 * np.random.normal(size=len(xdata))

plt.plot(xdata, ydata, 'b-')

popt, pcov = curve_fit(fund, xdata, ydata)

# popt数组中，三个值分别是待求参数a,b,c

y2 = [fund(i, popt[0], popt[1]) for i in xdata]

plt.plot(xdata, y2, 'r--')

plt.show()
print(popt)
