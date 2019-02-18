
import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime
from pyecharts import Kline,Line,Overlap, Grid ,Bar,Page
import math

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

    volume= table.col_values(5)
    volume.reverse()
    volume.pop()
    volume_n = []
    for i in range(len(volume)):

        if volume[i][-1] == "K":
            volume_n.append(float(volume[i][:-1]) * 1000)
        elif volume[i][-1] == "M":
            volume_n.append(float(volume[i][:-1]) * 10000)
        else:
            volume_n.append(0)
    print("导入交易量：",volume_n)

    return date,open,close,low,high,volume_n

def ImportAddress():
    data = xlrd.open_workbook("比特币新增地址数.xls")
    table = data.sheets()[0]          #通过索引顺序获取

    time=table.col_values(0)  #获取日期指
    num=table.col_values(1)   #
    time.reverse()
    time.pop()
    num.reverse()
    num.pop()
    date = []
    for i in range(len(time)):
        date.append(datetime(*xldate_as_tuple(time[i], 0)).strftime('%Y/%m/%d'))

    print("导入时间：", date)
    print("导入地址增量",num)
    return date,num
ImportAddress()

