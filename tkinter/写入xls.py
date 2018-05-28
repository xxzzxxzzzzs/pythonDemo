from  collections import OrderedDict

from pyexcel_xls import save_data

def  makeXls(path,data):
    dic=OrderedDict()
    for sheetName,sheetValue in data.items():
        d={}
        d[sheetName]=sheetValue
        dic.update(d)
    save_data(path,dic)


path="/Users/zzs/Desktop/python/tkinter/zzs3.xls"
makeXls(path,{"表1":[[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]],"表2":[[2,2,3],[1,2,3]]})