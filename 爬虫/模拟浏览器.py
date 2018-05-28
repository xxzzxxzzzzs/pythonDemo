import  urllib.request
import  random

url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&ch=15&tn=56060048_4_pg&wd=%E7%9A%84%E6%92%92&oq=github&rsv_pq=ddf2e2140001ae80&rsv_t=2272ieCXe0UrB%2FHPXvtso%2FKKZDCy%2BoUaYrsMPH36ZBDTx%2BhNENgwujf1o0JPzoilTtG%2BlA&rqlang=cn&rsv_enter=0&inputT=6257&rsv_sug3=43&rsv_sug1=34&rsv_sug7=100&rsv_sug4=6257"
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
response2=urllib.request.urlopen(req2)
data2=response2.read().decode("utf-8")
print(data2)