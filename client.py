# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 09:02:39 2018

@author: Emilio
"""

import os
import socket
from threading import Thread
import time

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
            

        
def TX(s):
    string="-i ###"
    for i in os.listdir("myFiles"):
        string+=i+"###"
    s.send(string)
    while True:
        a=raw_input("input:")
        s.send(a)

host=socket.gethostname()
port=1995

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
if(not os.path.exists("myFiles")):
    os.mkdir("myFiles")
Thread(target=TX,args=(s,)).start()
Thread(target=RX,args=(s,)).start()
    