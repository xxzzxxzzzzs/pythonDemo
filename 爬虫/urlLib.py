import  urllib.request


# response=urllib.request.urlopen("http://www.baidu.com")
#
# data=response.read()

# data=response.readline()
#
# data=response.readlines()
# print(data)


# with open("/Users/zzs/Desktop/python/爬虫/urlLib.html","wb") as f:
#     f.write(data)
# //返回当前环境的有关信息
# print(response.info())
#返回码
# print(response.getcode())
# 爬虫的Url
# print(response.geturl())

newurl="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&ch=15&tn=56060048_4_pg&wd=%E7%9A%84%E6%92%92&oq=github&rsv_pq=ddf2e2140001ae80&rsv_t=2272ieCXe0UrB%2FHPXvtso%2FKKZDCy%2BoUaYrsMPH36ZBDTx%2BhNENgwujf1o0JPzoilTtG%2BlA&rqlang=cn&rsv_enter=0&inputT=6257&rsv_sug3=43&rsv_sug1=34&rsv_sug7=100&rsv_sug4=6257"
neuUrl=urllib.request.unquote(newurl)
print(neuUrl)
neuUrl=urllib.request.quote(newurl)
print(neuUrl)

