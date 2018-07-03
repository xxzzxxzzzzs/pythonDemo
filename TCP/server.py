import  socket

# UDP 获取本机IP
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
# 创建一个socket、
server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定IP、
print(get_host_ip())
server.bind((get_host_ip(),8084))
#监听
server.listen(5)
print("server--start---success")
#等待链接
clientSocket, clientAddress = server.accept()
print("waiting--link")
while True:
    data=clientSocket.recv(1024)
    print("get"+str(clientSocket)+"data:"+data.decode("utf-8"))
    clientSocket.send(data+"success".encode("utf-8"))



