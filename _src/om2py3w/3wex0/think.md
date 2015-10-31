# 网络版简单日记本思路整理

## 一、如何进行网络开发?

[参考文档](https://docs.python.org/2.7/library/socket.html)

英文还是有点纠结~╮(╯▽╰)╭，于是我先对着一个中文教程入个门！

- 首先最简单的就是创建一个 Socekt
  
  ``` python
  import socket   
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  ```
  
  上述代码用了下面两个属性来创建 Socket：
  
  - 地址簇：AF_INET(IPv4)
  - 类型：SOCK_STREAM(使用 TCP传输控制协议)
  - 如果函数失败，还需要处理异常。当当当当~try 隆重登场！
  
  ``` python
  import socket
  import sys
  
  try:
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  except socket.error, msg:
      print 'Faild to create socket'
      sys.exit();
  print 'socket Created'
  ```
  
  ​
  
- 下一步就是使用这个 Socket 来连接到服务器
  
  - 首先要获取远程主机的 IP 地址，指定 port。
  - python 里获取主机地址 ip 的方法是`socket.gethostbyname(name)`相当的简单啊~
  
  ``` python
  host = 'www.iomooc.com'
  port = 80
  try:
      ip = socket.gethostbyname(host)
  except socket.gaierror:
      print 'Hostname could not be resolved.'
      sys.exit()
  
  print 'Connecting ' + host + ':' + ip 
  ```
  
  - 运行一下
  
  ![](http://7xn3v1.com1.z0.glb.clouddn.com/15-10-30/91591815.jpg)
  
  - **小提示**
  
  > 使用 SOCK_STREAM/TCP 套接字才有“连接”的概念。连接意味着可靠的数据流通讯机制，可以同时有多个数据流。可以想象成一个数据互不干扰的管道。另外一个重要的提示是：数据包的发送和接收是有顺序的。
  > 
  > 其他一些 Socket 如 UDP、ICMP 和 ARP 没有“连接”的概念，它们是无连接通讯，意味着你可从任何人或者给任何人发送和接收数据包。
  
- 发送数据：`sandal` 函数用于简单的发送数据
  
  ``` python
  message = 'GET / HTTP/1.1\r\n\r\n' # 用来获取网站首页的内容
  
  try:
      s.sendall(message)
  except socket.error:
      print 'Send Failed'
      sys.exit()
  
  print 'Message Send Successfully.'
  ```
  
- 接收数据：`recv` 函数用于从 socket 接收数据
  
  ``` python
  reply = s.recv(4096)
  
  print reply
  ```
  
  - 运行一下~看看芝麻星的首页是啥~
  
  ![](http://7xn3v1.com1.z0.glb.clouddn.com/15-10-30/18614593.jpg)
  
  - 貌似失败鸟~但是大概可能也许接收到消息了吧
  
- 最后是关闭 socket
  
  ``` python
  s.close()
  ```
  
- 回顾一下：
  
  1. 创建 Socket
  2. 连接到远程服务器
  3. 发送数据
  4. 接收回应



### 服务器端编程

- 绑定 Socket

`bind` 函数用于将 Socket 绑定到一个特定的地址和端口，它需要一个类似 connect 函数所需的 sockaddr_in 结构体。

``` python
import socket
import sys

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
```

- 连续侦听：`listen` 函数用于实现侦听模式

``` python
s.listen(10)    #限制10个连接，意味着第11个连接会被拒绝
print 'Socket now listening'
```

- 接受连接：

``` python
conn, addr = s.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])
```

运行起来，程序开始等待连接进入，端口是8888，通过 telnet 程序进行测试。

在终端中输入：

``` 
└─[$]> telnet localhost 8888
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Connection closed by foreign host.
```

服务器端窗口显示：

``` 
└─[$]> python server.py
Socket Created.
Socket bind complete.
Socket now listening
Connected with 127.0.0.1:63207
```

显示客户端已经成功连接到服务器~然而不发送点东西过去似乎并没有什么卵用

- 让服务端给客户端发送数据：`sendall`

``` python
data = conn.recv(1024)
conn.sendall(data)

conn.close()
s.close()
```

运行一下：

``` 
└─[$]> telnet localhost 8888
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
hello
hello
Connection closed by foreign host.
```

第一个 hello 是客户端发出的，第二个 hello 是服务端接收到回馈给客户端的。

- 一直运行的服务器：上面的例子里，服务器端回应后就立即退出了，其他服务器就连接不进来了，而真正的服务器应该一直运行着的才行。为了让服务器端能够一直运行，最简单的方法就是把接受的代码循环起来~

``` python
while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    data = conn.recv(1024)
    reply = '收到！' + data
    if not data:
        break

    conn.sendall(reply)

conn.close()
s.close()
```

打开三个客户端进行连接，服务端显示：

``` 
└─[$]> python server.py
Socket Created.
Socket bind complete.
Socket now listening
Connected with 127.0.0.1:63279
Connected with 127.0.0.1:63281
Connected with 127.0.0.1:63283
```

- 处理多个连接：我们需要服务器可以同时处理多个请求。使用线程来处理连接请求。

``` python
from thread import *
#...
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
```

运行一下（一个客户端可以一直发送和接受而不被关闭了）

``` 
└─[$]> telnet localhost 8888
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Welcome to the server.Tpye something and hit enter
hehe
收到！hehe
haha
收到！haha
nice
收到！nice
```





## 二、什么是 UDP 协议?

- 缩写是：User Datagram Protocol
- 是一个简单的面向数据包的传输层协议，只提供数据的不可靠传递，它一旦把应用程序发给网络层的数据发送出去，就不保留数据备份。
- 允许一定量的丢包，出错和复制粘贴





## 三、用 Python 完成一对最简单的 UDP 服务器/客户端

- 上述 `SOCK_STREAM` 是 TCP 协议，改成 `SOCK_DGRAM` 就是 UDP 协议了
- 一对最简单的 UDP 服务器/客户端：

``` python
# server.py
import socket
port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))
print "waiting on port:", port
while 1:
    data, addr = s.recvfrom(1024)
    print data
---

# client.py
import socket
port = 8888
host = "localhost"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 0))
s.sendto("Holy Guido! It's working.", (host, port))
```





## 四、简单日记本网络版

- s.recvfrom

> socket.recvfrom(*bufsize*[, *flags*])
> 
> Receive data from the socket. The return value is a pair (string, address) where *string* is a string representing the data received and *address* is the address of the socket sending the data. See the Unix manual page *recv(2)* for the meaning of the optional argument *flags*; it defaults to zero. (The format of *address* depends on the address family — see above.)

- s.sendto

> socket.sendto(*string*, *address*)
> 
> socket.sendto(*string*, *flags*, *address*)
> 
> Send data to the socket. The socket should not be connected to a remote socket, since the destination socket is specified by *address*. The optional *flags* argument has the same meaning as for [recv()](https://docs.python.org/2.7/library/socket.html#socket.socket.recv) above. Return the number of bytes sent. (The format of*address* depends on the address family — see above.)s



### 从最简单的框架开始...

- 客户端

最简单的输入、发送框架

``` python
# encoding:utf-8
# __author__:zhulijian

from sys import argv
import socket

script, IP = argv
print IP

def write():
    line = raw_input('输入>')
    return line

def createudp():
    port = 8888
    host = IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("",0))
    inp = write()
    s.sendto(inp, (host,port))

def main():
    createudp()

if __name__ == "__main__":
    main()
```

- 服务端

``` python
# encoding:utf-8

import socket
import sys
from thread import *
import time

port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print '服务器启动中...'
try:
    s.bind(("",port)    #创建服务器，开始监听端口
except socket.error, msg:
    print str(msg[0])
    sys.exit()
print '端口开放：',port

while 1:
    data, addr = s.recvfrom(1024)   #接收内容并打印到屏幕上
    localtime = '['+time.asctime(time.localtime(time.time()))+']'
    data2 = localtime + '\n----> ' + data2

    print data2

s.close()
```



### 增加新的功能

> ——发送中文、连续发送、服务器保存文件

- 客户端

中文发送和接受经测试没有问题。

连续发送只要把输入和发送循环起来就可以咯：

``` python
while 1:    #连续发送文字
        inp = write()
        s.sendto(inp, (host,port))
```

- 服务器

服务器接收到文字后，自动追加到 daily.log 文件内，如果没有，生成一个！

``` python
# encoding:utf-8

import socket
import sys
from thread import *
import os

def writelog(data): #写入到 daily.log 
    if os.path.isfile('daily.log') == False:    #检查daily.log，没有就创建
        f = open('daily.log','w')
        f.close()
    f = open('daily.log','a')
    f.write(data + '\n')
    f.close()

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
    writelog(data)	#把 data 传入 daily.log
    print data
    
s.close()
```



### 继续增加新的功能

> ——启动时从服务端获取消息，和输入命令获取消息

- 客户端

``` python
    s.sendto('-r', (host, port))    #立即从服务器获取消息
    print s.recv(1024)
    while 1:    #连续发送文字
        inp = write()
        s.sendto(inp, (host, port))
        print s.recv(1024)
```

- 服务器

``` python
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
        data2 = localtime + ' ' + data
        re = wrc(data, data2)   #得到文件处理函数返回的内容
        s.sendto(re, addr)  #将返回的内容推送回客户端
        print re    #打印到服务端的屏幕上，用以检查

    s.close()

def main():
    createserver()

if __name__ == "__main__":
    main()
```



### 测试

- 多个客户端发送消息，对服务器无影响，可以反复获得历史消息。
- 中文测试通过
- 服务器生成文件通过



---

# 迭代

- 20151031 完成初步功能