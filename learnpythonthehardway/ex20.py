# _*_ coding:utf-8 _*_
# 习题20:函数和文件

from sys import argv

s,infile = argv

def printall(f):
	print f.read()

def rewind(f):
	f.seek(0)

def printaline(linecount,f):
	print linecount, f.readline(),

cufile = open(infile)

print "首先让我们打印整个文件：\n"
printall(cufile)

print "现在我们将文件倒带：\n"
rewind(cufile)

print "打印三行：\n",

for i in range(1,4):
	printaline(i,cufile)
