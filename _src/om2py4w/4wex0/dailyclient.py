# encoding:utf-8
# __author__:zhulijian

import sys
import socket

reload(sys)  
sys.setdefaultencoding('utf-8') 


def write():
    line = raw_input('输入> ')
    return line

def createudp():
    port = 8888
    host = raw_input('输入服务器的IP地址：')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("",0))
    s.sendto('-r', (host, port))    #立即从服务器获取消息
    print s.recv(1024)
    while 1:    #连续发送文字
        inp = write()
        s.sendto(inp, (host, port))
        print s.recv(1024)
        
def main():
    createudp()

if __name__ == "__main__":
    main()
