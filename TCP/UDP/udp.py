import socket

import time

udp=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp.sendto("12dasdasewqe3".encode("gbk"),("192.168.1.2", 2425))