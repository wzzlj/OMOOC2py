# encoding:utf-8

import socket
import sys
from thread import *

# 绑定Socket
HOST = ""   
PORT = 8888 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Created.'

try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print str(msg[0])
    sys.exit()

print 'Socket bind complete.'

# 连续侦听
s.listen(10)    #限制10个连接，意味着第11个连接会被拒绝
print 'Socket now listening'

# 接受连接
def clientthread(conn):
    conn.send('Welcome to the server.Tpye something and hit enter\n')
    while True:
        data = conn.recv(1024)
        reply = '收到！' + data
        if not data:
            break

        conn.sendall(reply)

    conn.close()
   
while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    
    start_new_thread(clientthread,(conn,))

s.close()
