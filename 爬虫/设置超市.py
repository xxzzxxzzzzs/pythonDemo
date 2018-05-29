import  urllib.request

# 判断超时
for i in range(1,100):
    try:
         response=urllib.request.urlopen("http://www.baidu.com",timeout=0.05)
         print(len(response.read().decode("utf-8")))
    except:
        print("超时")