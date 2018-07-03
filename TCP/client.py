import socket

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((get_host_ip(),8084))
count=0
while True:
    count+=1;
    data=input("input data to sever")
    client.send(data.encode("utf-8"))
    info=client.recv(1024)
    print("server call black"+info.decode("utf-8"))