# encoding:utf-8
# __author__:zhulijian

from sys import argv
import socket
script, IP = argv
print IP

def write():
    line = raw_input('输入> ')
    return line

def createudp():
    port = 8888
    host = IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("",0))
    while 1:    #连续发送文字
        inp = write()
        s.sendto(inp, (host,port))


def main():
    createudp()

if __name__ == "__main__":
    main()
