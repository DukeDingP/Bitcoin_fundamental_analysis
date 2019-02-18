#解决xlrd 读取日期为一串数字
import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime
data = xlrd.open_workbook("Bitcoin - 比特币历史数据_历史行情,价格,走势图表.xlsx")
table = data.sheets()[0]          #通过索引顺序获取

time=table.col_values(0)  #获取日期指
del time[0]

date = datetime(*xldate_as_tuple(time[0], 0))
cell = date.strftime('%Y/%m/%d')
print(cell)

print("导入时间：",time)