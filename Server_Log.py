import socket
import subprocess

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = "192.168.43.114"
port = 1234

s.bind((ip,port))
print("Server Is Ready To Receive Texts")
print("All Texts Will be Saved as Log in the Log.Txt File\n")
f=open("log.txt", mode='w+')


while True:
   x = s.recvfrom(32)
   clientip = x[1][0]
   data = x[0].decode()
   if ("bye" in data) or ("logout" in data):
     f.write("Server Closed")
     exit()
   else:
     t = subprocess.getstatusoutput("date +%r")
     print("["+clientip + "] [" + t[1] + "] : " + data)
     f.write("["+clientip + "] [" + t[1] + "] : " + data + "\n")

f.close()

