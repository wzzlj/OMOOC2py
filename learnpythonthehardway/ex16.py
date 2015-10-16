# _*_ coding:utf-8 _*_

from sys import argv

script, filename = argv

print "我们要去删除 %r 了。" % filename
print "如果你不想这样，请按下 ctrl + c 。"
print "如果你想继续，请按 return 。"

raw_input("?")

print "打开文件..."
target = open(filename,'w')

print "清空文件，哈哈哈哈哈哈哈哈。"
target.truncate()

print "现在我请你输入三行文字："

line1 = raw_input(" 第一行：")
line2 = raw_input(" 第二行：")
line3 = raw_input(" 第三行：")

print "我会把这三行写进文件"

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "OK，完成了，我要把文件关闭咯~"
target.close()
