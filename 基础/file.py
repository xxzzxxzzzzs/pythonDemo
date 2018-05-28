# -*- coding: UTF-8 -*-

path="/Users/zzs/Desktop/python/基础/filetes3"
# try:
#
    # f=open(path,"r",encoding="utf-8",errors="ignore")
# f2=open(path,"r")
#     print(f.read())
#     f.seek(20)
#     print(f.read())
# finally:
#     if f:
#         f.close()
#
# print(f.readline())

# print(f.readlines())

# with open( path,"r",encoding="utf-8") as f2:
#     print(f2.read())

f = open(path, "w", encoding="utf-8", errors="ignore")
f.write("2017款科迈罗")
# while 1:
    # f.write("2017款科迈罗")


f.closed