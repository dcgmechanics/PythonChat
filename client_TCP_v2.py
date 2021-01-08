import socket
s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
ip=input("Enter Server IP Address: ")

try:
    s.connect((ip,1235))
    print("Connection Established")
    print("Chat Program Started")
    
    while True:
        t1=input("You: ")
        if "bye" in t1:
            s.send(t1.encode())
            s.close()
            exit()
        s.send(t1.encode())
        x=s.recv(1024)
        print(ip + ": " + x.decode())
        if b"bye" in x:
            print("Server Has Shutdown, Bye")
            s.close()
            exit()
        
except ConnectionRefusedError :
    print("Connection Failed")
    
except ConnectionAbortedError:
    print("Server Has Been Logout")
    
except ConnectionResetError:
    print("Server Lost")
    
finally:
    print("Thank You For Using This Program")

s.close()