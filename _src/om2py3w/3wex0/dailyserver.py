# encoding:utf-8

import socket
import sys
from thread import *
import os
import time

reload(sys)  
sys.setdefaultencoding('utf-8') 

def wrc(command, data): #文件处理
    if os.path.isfile('daily.log') == False:    #检查daily.log，没有就创建
        f = open('daily.log','w')
        f.close()
        return '---创建daily.log---'
    
    elif command.lower() == '-r':   #输入-r命令后读取日记
        f = open('daily.log','r')
        reply =  '-'*10+'读取日记'+'-'*10+'\n'+f.read()+'-'*28
        return reply
    
    elif command.lower() == '-c':   #输入-c命令后初始化日记
        f = open('daily.log','w')
        return '---初始化完毕---!'

    else:                           #没有命令则执行写入文件
        f = open('daily.log','a')
        f.write(data + '\n')
        f.close()
        return data

def createserver():
    port = 8888
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print '服务器启动...'
    try:
        s.bind(("",port))    #创建服务器，开始监听端口
    except socket.error, msg:
        print str(msg[0])
        sys.exit()
    print '按 control+c 退出服务器，，，'

    while 1:
        data, addr = s.recvfrom(1024)   #接收内容并打印到屏幕上
        localtime = time.asctime(time.localtime(time.time()))
        localtime = localtime.split(' ')
        data2 = '['+localtime[4]+'] '+data
        re = wrc(data, data2)   #得到文件处理函数返回的内容
        s.sendto(re, addr)  #将返回的内容推送回客户端
        print re    #打印到服务端的屏幕上，用以检查

    s.close()

def main():
    createserver()

if __name__ == "__main__":
    main()
