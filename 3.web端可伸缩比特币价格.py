import xlrd
import matplotlib.pyplot as plt
from xlrd import xldate_as_tuple
from datetime import datetime
from pyecharts import Kline,Line,Overlap

#导入 开 收 低 高
def Import():
    data = xlrd.open_workbook("Bitcoin - 比特币历史数据_历史行情,价格,走势图表.xlsx")
    table = data.sheets()[0]          #通过索引顺序获取

    time=table.col_values(0)  #获取日期指
    time.reverse()  #反转
    time.pop()      #去掉最后一个字符
    #将日期转化为 %Y/%m/%d 形式
    date = []
    for i in range(len(time)):
        date.append(datetime(*xldate_as_tuple(time[i], 0)).strftime('%Y/%m/%d'))

    print("导入时间：",date)

    close=table.col_values(1)
    close.reverse()
    close.pop()
    print("导入收盘价：",close)

    open = table.col_values(2)
    open.reverse()
    open.pop()
    print("导入开盘价：", open)

    high = table.col_values(3)
    high.reverse()
    high.pop()
    print("导入最高价：", high)

    low = table.col_values(4)
    low.reverse()
    low.pop()
    print("导入最低价：", low)

    return date,open,close,low,high

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

#构造 pyecharts Klines 数据格式
def V1(open,close,low,high):
    v1=[]
    for i in range(len(open)):
        #构造一个OHLC列表结构
        OHLC=[]
        OHLC.append(open[i])
        OHLC.append(close[i])
        OHLC.append(low[i])
        OHLC.append(high[i])
        v1.append(OHLC)
    print("klines构造完毕：",v1)
    return v1

#实现kline画图
def K_line(date,v1):
    kline = Kline("比特币历史价格")
    kline.add("日K", date, v1,is_datazoom_show=True,)
    overlap = Overlap()
    overlap.add(kline)
    overlap.render()

date,open,close,low,high=Import()
v1=V1(open,close,low,high)
K_line(date,v1)
# logb=[math.log10(x) for x in b]
# plt.plot(a,b)
# MA(a,b,30)  #30日均线
# MA(a,b,5)   #5日均线
# MA(a,b,10)   #10日均线
# plt.show()  #历史曲线


# plt.plot(a,logb)
# plt.show()  #指数曲线



