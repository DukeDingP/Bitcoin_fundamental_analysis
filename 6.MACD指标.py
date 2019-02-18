#Ma 回测平台 策略
import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime
from pyecharts import Kline,Line,Overlap, Grid ,Bar,Page

grid = Grid()
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

#MA(30)
#a表示时间,b表示价格 c表示几日移动平均线
def MA(close,datenumber):
    ma=[]
    for i in range(len(close)-datenumber):
        sum = 0
        for j in range(datenumber):
            sum+=close[i+j]
        ma.append(sum/datenumber)
    return ma

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

#将数据包装成 Kline形式
def K_line(date,v1,name):
    kline = Kline(name)
    kline.add("日K", date, v1,is_datazoom_show=True,)
    return kline
#将MA数据包装成echarts Line形式
def L_ine(date,close,datenumber):
    time=[]
    ma=MA(close,datenumber)
    line=Line()
    for i in range(len(date)):
        time.append(date[i])
    #time=a
    del time[0:datenumber]
    line.add("比特币{}日均线".format(datenumber),time,ma)
    return line

#添加交易量
def Volume_bar(date,volume):
    bar = Bar(title_pos="40%")
    bar.add(
        "交易量",
        date,
        volume,
       # yaxis_formatter=" ml",
       yaxis_max=2000000,
       #  legend_pos="85%",
       #  legend_orient="vertical",
       #  legend_top="45%",
    )
    return bar

date,open,close,low,high,volume=Import()
v1=V1(open,close,low,high)
#5日均线
ma_5=L_ine(date,close,5)
#10日均线
ma_10=L_ine(date,close,10)
#20日均线
ma_20=L_ine(date,close,20)
#5日均线
ma_30=L_ine(date,close,30)
#日K线
kline=K_line(date,v1,"比特币历史行情-MA以及交易量")
#交易量
bar=Volume_bar(date,volume)

overlap = Overlap(width=1500, height=600)
overlap.add(kline)
overlap.add(ma_5)
overlap.add(ma_10)
overlap.add(ma_20)
overlap.add(ma_30)
overlap.add(bar,is_add_yaxis=True, yaxis_index=1)

page = Page()         # 第一个图表
page.add(overlap)

#MACD指标
#DIF=MA(12)-MA(26)  a=12,b=16
#EDA=9日EMA    c=9
#macd=DIF-EDA bar

def DIF(a,b):
    dif = []
    ma_a=MA(close,a)
    ma_b=MA(close,b)
    #让ma_a和ma_b具有相同维度
    ma_a=ma_a[b-a:]
    for i in range(len(ma_a)):
        dif.append(ma_a[i]-ma_b[i])
    print("dif:",dif)
    return dif

def EDA(a,b,c):
    dif=DIF(a,b)
    eda = []
    for i in range(len(dif) - c):
        sum = 0
        for j in range(c):
            sum += dif[i + j]
        eda.append(sum / c)
    print("eda:", eda)
    return eda

def MACD(a,b,c):
    dif=DIF(a,b)
    eda=EDA(a,b,c)
    dif=dif[len(dif)-len(eda):]
    macd=[]
    for i in range(len(dif)):
        macd.append(dif[i]-eda[i])
    return macd

#将dif数据包装成echarts Line形式
def DIF_Line(date,quick_ma,slow_ma):   #快均线 慢均线
    time=[]
    dif=DIF(quick_ma,slow_ma)
    line=Line()
    date=date[len(date)-len(dif):]
    line.add("DIF均线",date,dif,legend_top="50%",is_datazoom_show=True,datazoom_xaxis_index=[0, 1])
    return line
#将eda数据包装成echarts Line形式
def EDA_Line(date,quick_ma,slow_ma,dif_ma):   #快均线 慢均线
    time=[]
    eda=EDA(quick_ma,slow_ma,dif_ma)
    line=Line()
    date=date[len(date)-len(eda):]
    line.add("EDA均线",date,eda,legend_top="50%",is_datazoom_show=True,line_color="green")
    return line
#将macd数据包装成echarts Bar形式
def MACD_Bar(date,quick_ma,slow_ma,dif_ma):
    macd=MACD(quick_ma,slow_ma,dif_ma)
    bar = Bar("bitcoin macd",title_pos="50%")
    date = date[len(date) - len(macd):]
    bar.add(
        "macd",
        date,
        macd,
       # yaxis_formatter=" ml",
       #yaxis_max=2000000,
       #  legend_pos="85%",
       #  legend_orient="vertical",
       #  legend_top="45%",
    )
    return bar

kline=K_line(date,v1,"比特币macd指标")
overlap_uper = Overlap()
overlap_uper.add(kline)
overlap_uper.add(L_ine(date,close,12))
overlap_uper.add(L_ine(date,close,26))


#dif曲线 grid 下面的图
dif_line=DIF_Line(date,12,26)
eda_line=EDA_Line(date,12,26,9)
macd_bar=MACD_Bar(date,12,26,9)

overlap_down = Overlap()
overlap_down.add(dif_line)
overlap_down.add(eda_line)
overlap_down.add(macd_bar)

grid = Grid(width=1500, height=600)
grid.add(overlap_down, grid_top="60%")
grid.add(overlap_uper, grid_bottom="60%")

#第二幅画
page.add(grid)
page.render()





