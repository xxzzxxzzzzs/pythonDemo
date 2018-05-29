
import urllib.request
import json
# //get    请求\
url="https://leancloud.cn:443/1.1/classes/Todo/5a7d398a9f5454005e90d040"
header={
    "X-LC-Id": "d7p3nG3FsaM5JDeUnmyree95-gzGzoHsz",
    "X-LC-Key":"2AkrxjjipVJKCF2UL0pkcs9R",
    "Content-Type": "text/plain"
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