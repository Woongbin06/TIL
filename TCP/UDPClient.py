from socket import *

s_ip = "localhost"
s_port = 12346
s_addr = (s_ip, s_port)

c_sock = socket(AF_INET, SOCK_DGRAM)


data = "세원아 제발"
c_sock.sendto(data.encode("utf-8"), s_addr)

c_sock.close()
