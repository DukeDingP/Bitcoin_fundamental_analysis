import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime
data = xlrd.open_workbook("Bitcoin - 比特币历史数据_历史行情,价格,走势图表.xlsx")
table = data.sheets()[0]          #通过索引顺序获取
volume = table.col_values(5)
volume.reverse()
volume.pop()
print("导入交易量：", volume)

print(float(volume[0][:-1]))

volume_n=[]
for i in range(len(volume)):

    if volume[i][-1]=="K":
        volume_n.append(float(volume[i][:-1])*1000)
    elif volume[i][-1]=="M":
        volume_n.append(float(volume[i][:-1])*10000)
    else:
        volume_n.append(0)

print(volume_n)