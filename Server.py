import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = "localhost"
port = 1234

s.bind((ip,port))

while True:
    x = s.recvfrom(10)
    clientip = x[1][0]
    data = x[0].decode()
    print(clientip + " : " + data) 