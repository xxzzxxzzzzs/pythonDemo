
# -*- coding: UTF-8 -*-
import time;  # 引入time模块

# ticks = time.time()
# print "当前时间戳为:", ticks
# str='''sdasda123
# 123]@@!3
# 213!@
# @!31#12#12'''
# list=str.split("@");
# print str.split("@")
# c=0
# for s in list:
#     if len(s)>0:
#         c+=1
# print c
# list2=str.splitlines()
# print list2
# str3= " ".join(list2)
# print str3
#
# print  str3.replace("2","22222")
#
# str4=str.maketrans("good","nice")
# str5="good  good  man nice"
# str6=str5.translate(str4)
# print str6
# d={}
# str="dasdas asdasda adasdas asd asd asdas dasd asd sad asd as"
# list= str.split(" ")
# # print  list
# for v in  list:
#     c=d.get(v)
#     if c==None:
#         d[v]=1
#     else:
#         d[v]+=1
# print  d
#
# s4=set([1,2,2,2,3,4,5])
# print  s4
# s4.add(6)
# print  s4
# s4.add((1,5,8))
# print  s4
# s4.update([10,22])
# print  s4
# !/usr/bin/python
# -*- coding: UTF-8 -*-

def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print b  # 结果是 2


# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print "函数内取值: ", mylist
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print "函数外取值: ", mylist