import socket	
from os import popen
from multiprocessing import Process
s = socket.socket()		
ip=(popen("hostname -I | awk '{print $1}'").read()).strip()
port = 15450			
b = "\033[35m"
w = "\033[0m"
s.connect((ip, port))
print("connection successful!")
while True:
    def recive():
        while True:
            cmd=s.recv(1024).decode()
            print(b+cmd+"\n"+w)
            if cmd == "exit server":
                s.close()
    p1 = Process(target = recive)
    p1.start()
    x=""
    while x!="exit server":
        x=input()
        s.send(x.encode())
    s.close()
