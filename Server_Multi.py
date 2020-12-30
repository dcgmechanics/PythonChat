import time
import socket
import subprocess
import threading

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = "192.168.43.114"
port = 1234

s.bind((ip,port))
print("Server Is Ready To Receive Texts\n")

def a():
 while True:
   x = s.recvfrom(32)
   clientip = x[1][0]
   data = x[0].decode()
   t = subprocess.getstatusoutput("date +%r")
   print("["+clientip + "] [" + t[1] + "] : " + data)
   time.sleep(10)
  

x1 = threading.Thread(target=a)
x2 = threading.Thread(target=a)
x3 = threading.Thread(target=a)

x1.start()
x2.start()
x3.start()

