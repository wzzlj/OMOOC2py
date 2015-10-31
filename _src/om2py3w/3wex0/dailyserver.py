# encoding:utf-8

import socket
import sys
from thread import *
import os
import time

def wrc(command, data): #文件处理
    if os.path.isfile('daily.log') == False:    #检查daily.log，没有就创建
        f = open('daily.log','w')
        f.close()
    
    elif command.lower() == '-r':
        f = open('daily.log','r')
        reply =  '-'*10+'读取日记'+'-'*10+'\n'+f.read()+'-'*28
        print reply
        return reply
    elif command.lower() == '-c':
        f = open('daily.log','w')

    else:
        f = open('daily.log','a')
        f.write(data + '\n')
        f.close()

def readlog():
    f = open('daily.log','r')
    reply = f.read()
    return reply
    f.close()

def createserver():
    port = 8888
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print '服务器启动中...'
    try:
        s.bind(("",port))    #创建服务器，开始监听端口
    except socket.error, msg:
        print str(msg[0])
        sys.exit()
    print '端口开放：',port

    while 1:
        data, addr = s.recvfrom(1024)   #接收内容并打印到屏幕上
        localtime = '['+time.asctime(time.localtime(time.time()))+']'
        data2 = localtime + '\n----> ' + data
        print data2
        wrc(data, data2)

    s.close()

def main():
    createserver()

if __name__ == "__main__":
    main()
