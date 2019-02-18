import xlrd
import matplotlib.pyplot as plt
import math
data = xlrd.open_workbook("Bitcoin - 比特币历史数据_历史行情,价格,走势图表.xlsx")
table = data.sheets()[0]          #通过索引顺序获取

print(table.row_values(1))

nrows = table.nrows#行
ncols = table.ncols#列

print(nrows,ncols)

a=table.col_values(0)  #获取日期指
a.reverse()  #反转
a.pop()      #去掉最后一个字符
a=[float(x) for x in a]   #字符转数字
a=[x-40376 for x in a]    #1开始
print("导入时间：",a)

b=table.col_values(1)
b.reverse()
b.pop()
print("导入开盘价：",b)

logb=[math.log10(x) for x in b]

plt.plot(a,b)

#MA(30)
#a表示时间,b表示价格 c表示几日移动平均线
def MA(a,b,c):
    ma=[]
    time=[]
    for i in range(len(b)-c):
        sum = 0
        for j in range(c):
            sum+=b[i+j]
        ma.append(sum/c)
    for i in range(len(a)):
        time.append(a[i])
    #time=a
    del time[0:c]
    plt.plot(time,ma)

MA(a,b,30)  #30日均线
MA(a,b,5)   #5日均线
MA(a,b,10)   #10日均线
plt.show()  #历史曲线


plt.plot(a,logb)
plt.show()  #指数曲线



