import socket
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
udpServer=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpServer.bind((get_host_ip(),8900))

while True:
    data,address=udpServer.recvfrom(1024)
    print(data.decode("utf-8"))

    udpServer.sendto(data,address)
