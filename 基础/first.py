#-*- coding:utf-8 -*-
import math
import random
# print("abcde")
# age=input("sss")
# print(int(random.randrange(100)))
a="  a  bc  a "
# print  a
# print('''
# 1
# 2
# 3
# 4
# 5
# ''')
# print(r"\n")
# print a.count("a",0,a.__len__())
# print(a.find("d",))
# if a.find("w")==-1:
#     print('没有')
# print(a.index("f",2))

# print(a.lstrip(" "))
# print(a.rstrip(" "))
# print(a.strip(" "))
# num =1
# sum=0
# while num<=100:
#
#     sum += num
#     num+=1
#
# print(sum)

a=["ac","asd","wqew"]
b="sdflkmas"
# for x in a:
#     print(x)
#
# for y in b:
#     print(y)

# for index in  range(len(a)):
#     print(index)
#     print(a[index])
# for num in range(10,20):  # 迭代 10 到 20 之间的数字
#    for i in range(2,num): # 根据因子迭代
#       if num%i == 0:      # 确定第一个因子
#          j=num/i          # 计算第二个因子
#          print '%d 等于 %d * %d' % (num,i,j)
#          break            # 跳出当前循环
#    else:                  # 循环的 else 部分
#       print num, '是一个质数'
# for num in  range(20):
#     for i in  range(2,num):
#         if num%i==0:
#             j=num/i
#             print("%d=%d *%d"%(num,i,j))
#             break
#     else:
# #         print num, '是一个质数'
# for i,j in enumerate (a):
#     print(i,j)
# prime = []
# for num in range(2,100):  # 迭代 2 到 100 之间的数字
#    for i in range(2,num): # 根据因子迭代
#       if num%i == 0:      # 确定第一个因子
#          break            # 跳出当前循环
#    else:                  # 循环的 else 部分
#       prime.append(num)
# print prime
# s = 'qazxswedcvfr'
# for i in range(0,len(s),2):
#     print s[i]
# for (index, char) in enumerate(s):
#      print "index=%s ,char=%s"  % (index, char)

arays = [1,8,2,6,3,9,4]
# for i in range(len(arays)):
#     for j in range(i+1):
#         if arays[i] < arays[j]:
#             # 实现连个变量的互换
#             arays[i],arays[j] = arays[j],arays[i]
# print arays

print(sorted(arays))