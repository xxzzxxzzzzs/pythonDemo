import socket

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data=input("fdsfdsafsadffdsa")
    client.sendto(data.encode("utf-8"),(get_host_ip(),8900))
    data, address = client.recvfrom(1024)
    print(data.decode("utf-8"))

