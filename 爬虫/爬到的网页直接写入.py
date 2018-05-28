import  urllib.request
urllib.request.urlretrieve("http://www.baidu.com",filename=r"C:\Users\Administrator\Desktop\python\pythonDemo\爬虫\pa.html")

# 清除缓存 比较耗费缓存
urllib.request.urlcleanup()