# 获取当前时间
import  datetime
dl=datetime.datetime.now()
print(dl)
print(type(dl))
# 获取指定时间
d2=datetime.datetime(1999,10,10,2,2,2)
print(d2)

# 将时间转字符串
d3=dl.strftime("%Y:%m:%d %H:%M:%S")
print(d3)

#将格式字符串 转为datatime对象
d4=datetime.datetime.strptime(d3,"%Y:%m:%d %H:%M:%S")
print(d4)

d6=datetime.datetime.now()
d7=d6-d2
print(d7)
print(d7.days)
# 天数除外的秒
print(d7.seconds)