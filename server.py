# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 08:46:55 2018

@author: Emilio
"""

import os
import socket
from threading import Thread
newPort=1999
allFiles=[]
users=[]
def RX(conn,ip,addr):
    lista=[]
    while True:
        msg=str(conn.recv(10000))
        if msg.split()[0]=="-i":
            lista=[]
            for i in msg[3:].split("###")[1:-1]:
                allFiles.append([i,conn,ip,addr])
        elif msg.split()[0]=="-s":
            lista=[]
            for i in allFiles:
                if i[0].count(msg[3:])>=1:
                    lista.append(i)
            string="-r "        
            for i in lista:
                string+="###"+str(i[0])
            conn.send(string)
        elif msg.split()[0]=="-d":
            global newPort
            newPort+=1
            index=int(msg[3:])-1
            string="-c "+str(newPort)+" "+str(lista[index][0])
            conn.send(string)
            string="-u "+str(newPort)+" "+str(lista[index][2])+" "+str(lista[index][0])
            lista[index][1].send(string)
            
            
                    
            
            
            
        
    
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
    print "Se ha conectado el cliente: ",ip," en [",addr,"]"
    try:
        Thread(target=RX,args=(c,ip,addr,)).start()
    except:
        print "Threading error"
    