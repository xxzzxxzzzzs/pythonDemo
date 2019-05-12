import  urllib.request
import  random
import  ssl

url="https://www.pexels.com"
# 模拟请求头
headers={
    "User-Agent":"Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
}
# 设置一个请求体
# req=urllib.request.Request(url,headers=headers)
# # 发起请求
# response=urllib.request.urlopen(req)
#
# data=response.read().decode("utf-8")
# print(data)

agentList=["Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1","Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"]
# headers={
#     "User-Agent":random.choice(agentList) 
# }
agent=random.choice(agentList)
req2=urllib.request.Request(url)
req2.add_header("User-Agent",agent)
# 创建未验证的上下文
context=ssl._create_unverified_context()
response2=urllib.request.urlopen(req2,context=context)
data2=response2.read().decode("utf-8")
print(data2)