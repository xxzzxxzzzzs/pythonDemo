# -*- coding: UTF-8 -*-
import  csv

# "/Users/zzs/Downloads/淘宝综合数据包.csv"
path="/Users/zzs/Desktop/python/淘宝综合数据包.csv"
def readCsv(path):
    infolist=[]
    with open(path,"r") as f:
        allFileInfo=csv.reader(f)
        for row in allFileInfo:
            infolist.append(row)
            # print(row)
        # print(allFileInfo)

    pass
def writeCsv(path,data):
    with open(path,"w")as f:
        writer=csv.writer(f)
        for rowData in data:
            writer.writerow(rowData)
    pass

# readCsv(path)

writeCsv("/Users/zzs/Desktop/python/1.csv",[["1","2","3"],[4,5,6]])