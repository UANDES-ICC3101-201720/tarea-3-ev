# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 08:46:55 2018

@author: Emilio
"""

import os
import socket
from threading import Thread
allFiles=[]
users=[]
def RX(conn,ip,addr):
    while True:
        msg=str(conn.recv(10000))
        if msg.split()[0]=="-i":
            for i in msg[3:].split("###")[1:-1]:
                allFiles.append([i,conn,ip,addr])
        elif msg.split()[0]=="-s":
            lista=[]
            for i in allFiles:
                if i[0].count(msg[3:])>=1:
                    lista.append(i[0])
            string="-r "        
            for i in lista:
                string+="###"+str(i)
            conn.send(string)
                    
            
            
            
        
    
host=socket.gethostname()
port=1995

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
users=[]
print "running..."
while True:
    c, address=s.accept()
    ip=address[0]
    addr=address[1]
    users.append([c,ip,addr])
    try:
        Thread(target=RX,args=(c,ip,addr,)).start()
    except:
        print "Threading error"
    