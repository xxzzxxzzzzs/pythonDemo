
# 1 时间戳
# 2 元组
# 3 字符串
import  time
import datetime
c=time.time()
print(c)
# 时间戳转换为UTC时间元组
t=time.gmtime(c)
print(t)
# 本地时间元组
b=time.localtime(c)
print(b)
# 本地时间转为时间戳
m=time.mktime(b)
print(m)
# 将时间元组转为字符串
s=time.asctime()
print(s)
# 将时间戳转为字符串
p=time.ctime()
print(p)
# 格式化时间字符串
q=time.strftime("%Y:%m:%d %H:%M:%S")
print(q)
#时间字符串 转元组
w=time.strptime(q,"%Y:%m:%d %H:%M:%S")
print(w)

# time.clock()
# sum=0
# for i in range(100000000):
#     sum +=i
# print(time.clock())




