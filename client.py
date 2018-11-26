# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 09:02:39 2018

@author: Emilio
"""
import os
import socket
from threading import Thread

def RX(s):
    while True:
        msg=s.recv(10000)
        if msg.split()[0]=="-r":
            print "archivos encontrados:\n"
            lista=msg[3:].split("###")
            counter=1
            for i in lista[1:]:
                print "[",counter,"] ",i
                counter+=1
        if msg.split()[0]=="-c":
            filename=msg[8:]
            print msg
            #Thread(target=Download,args=(msg.split()[1],filename)).start()
        
        if msg.split()[0]=="-u":
            #filename=msg[]
            print msg
            #Thread(target=Seed,args=(msg.split()[1],filename)).start()
            
            

        
def TX(s):
    string="-i ###"
    for i in os.listdir("myFiles"):
        string+=i+"###"
    s.send(string)
    while True:
        a=raw_input("input:")
        s.send(a)
        
def Download(port,filename):
    ds=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host=socket.gethostname()
    ds.bind((host,int(port)))
    ds.listen(1)
    seed, address=ds.accept()
    f=open(filename,'wb')
    while True:
        msg=seed.recv(1024)
        f.write(msg)
        
def Seed(port,ip,filename):
    ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host=ip
    ss.connect((host,port))
    path="/myFiles/"+filename
    f=open(path,'rb')
    while True:
        l=f.read(1024)
        ss.send(l)
        
    
host=socket.gethostname()
port=1995

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
if(not os.path.exists("myFiles")):
    os.mkdir("myFiles")
Thread(target=TX,args=(s,)).start()
Thread(target=RX,args=(s,)).start()
    