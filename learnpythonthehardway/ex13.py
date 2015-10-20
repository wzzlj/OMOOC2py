# _*_ coding:utf-8 _*_
# 习题13
# 将变量传递给脚本的方法

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third