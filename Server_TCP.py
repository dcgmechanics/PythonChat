import socket
s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
ip="localhost"
port=1234
s.bind((ip,port))
s.listen()
c,addr=s.accept()
print("Connection Established")
while True:
    x=c.recv(1024)
    print(x.decode())
    if b"bye" in x:
            print("Client Has Been Logout")
            s.close()
            exit()
    t1=input()
    if "bye" in t1:
        print("Thank You For Using, Bye")
        s.close()
        exit()
    c.send(t1.encode())