
import urllib.request
import urllib.parse
import json
# //get    请求\
url="https://leancloud.cn:443/1.1/classes/Todo/5a7d398a9f5454005e90d040"
header={
    "X-LC-Id": "d7p3nG3FsaM5JDeUnmyree95-gzGzoHsz",
    "X-LC-Key":"2AkrxjjipVJKCF2UL0pkcs9R",
    "Content-Type": "application/json"

}

req=urllib.request.Request(url,headers=header)
res=urllib.request.urlopen(req)
data=res.read().decode("utf-8")
print(data)

jsonData=json.loads(data)
print(jsonData)
print(type(jsonData))
print(jsonData["name"])

json2=json.dumps(jsonData)
print(json2)
print(type(json2))

# post
postUrl="https://leancloud.cn:443/1.1/classes/Todo"
data2={
  "content": "fdsafasdfasd",
  "name": "雍正",
}
# 发送数据打包
# postData=urllib.parse.urlencode(data)
postData=json.dumps(data2).encode(encoding='UTF8')
req2=urllib.request.Request(postUrl,data=postData,headers=header)

# opener = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
# res2 = opener.open(req2)
res2=urllib.request.urlopen(req2)
data2=res2.read().decode("utf-8")
print(data2)
