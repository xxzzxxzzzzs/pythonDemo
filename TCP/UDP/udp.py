import socket
# 飞Q发送消息报文的格式
mystr = "1_lbt4_10#32899#002481627512#0#0#0:1289671407:512312:你的hello:288:你好"

# socket.AF_INET  网络通信，Windows AF_INET
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # SOCK_DGRAM表示UDP，SOCKET_STREAM表示TCP
udp.connect(("192.168.1.2", 2425))  # connect函数的参数是一个元组，括号不能少(2425)是飞Q的端口号
udp.send(mystr.encode("gbk"))  # 报文是以二进制的形式发送的
udp.close()
