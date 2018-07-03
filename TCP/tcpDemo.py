import  socket
# 客户端 创建TCP链接,主动创建链接叫客户端
# 服务端   接受客户端链接


# 1.创建一个socketF_INET
#参数1 指定协议 AF_INET 或者AF_INET6
#参数2 SOCK_STREAM 面向流的TCP协议
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2 建立链接
# 参数 是一个数组 第一个是地址 第二个是端口号
sk.connect(("www.yiren19.com",80))


# Request URL: http://www.sina.com.cn/
# Request Method: GET
# Status Code: 302 Found
# Remote Address: 221.180.194.208:80
# Referrer Policy: no-referrer-when-downgrade

def getHandle(Host):
    strHeader='GET / HTTP/1.1\r\nHost:%s\r\nConnection: close\r\n\r\n'%Host
    print("========="+strHeader)
    return bytes(strHeader, 'utf-8')



sk.send(getHandle("www.yiren19.com"))

# 等待接受数据
data=[]
while True:
    tem=sk.recv(1024)
    if tem :
        data.append(tem)
    else:
        break;
dataStr=(b"".join((data)).decode("utf-8"))
sk.close()
header, Html=dataStr.split("\r\n\r\n",1)

print(header)
print(Html)