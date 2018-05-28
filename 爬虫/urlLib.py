import  urllib.request


response=urllib.request.urlopen("http://www.baidu.com")

data=response.read()

# data=response.readline()
#
# data=response.readlines()
# print(data)


with open("/Users/zzs/Desktop/python/爬虫/urlLib.html","wb") as f:
    f.write(data)
# //返回当前环境的有关信息
# print(response.info())
#
print(response.getcode())