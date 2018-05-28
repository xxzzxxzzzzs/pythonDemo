# 有序字典
from  collections import OrderedDict
# 读取数据
from  pyexcel_xls import  get_data

def readXlsAndXlsx(path):
    dic=OrderedDict()
    # 抓取数据
    xdata=get_data(path)
    for sheet in xdata:
        dic[sheet]=xdata[sheet]
        return dic

path="/Users/zzs/Desktop/文档/Batch外部仕様書.xls"
print(readXlsAndXlsx(path))

