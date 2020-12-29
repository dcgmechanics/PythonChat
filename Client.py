import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = input("Enter Server IP Address: ")
port= 1234

while True:
 text = input("Enter The Text You Want To Send: ")
 s.sendto(text.encode(),(ip,port))