import socket	
from os import popen
from multiprocessing import Process
s = socket.socket()		
ip=(popen("hostname -I | awk '{print $1}'").read()).strip()
port = 15450			
b = "\033[35m"
w = "\033[0m"
s.bind((ip, port))		

s.listen(5)	
print ("Started listening")		
while True:
    c, addr = s.accept()	
    print ('Got connection from', addr )
    x=""
    def recive():
        while True:
            print(b+c.recv(1024).decode()+"\n"+w)
    p1 = Process(target = recive)
    p1.start()
    while x!="exit server":
        x=input()
        c.send(x.encode())
    c.close()
    break
