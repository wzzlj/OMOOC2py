# encoding:utf-8
import socket
import sys

# 创建 socket
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #创建 IPv4，TCP 传输协议
except socket.error, msg:
    print 'Faild to create socket'
    sys.exit();
print 'socket Created'

# 连接主机
host = 'www.github.com'
port = 80
try:
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print 'Hostname could not be resolved.'
    sys.exit()

print 'Connecting ' + host + ':' + ip 

s.connect((ip, port))
print 'Socket Connected to ' + ip

# 发送消息
message = 'GET / HTTP/1.1\r\n\r\n'

try:
    s.sendall(message)
except socket.error:
    print 'Send Failed'
    sys.exit()

print 'Message Send Successfully.'

# 接收消息
reply = s.recv(4096)

print reply

# 关闭 socket
s.close()
