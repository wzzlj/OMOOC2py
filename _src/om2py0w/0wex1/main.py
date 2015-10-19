# _*_ coding:utf-8 _*_

from sys import argv #获取外部命令的参数

script,  writeread = argv

# 写日记功能
def write(target):
    line = raw_input('> ')

    print "是否保存？",
    save = raw_input('(y/n?) ')

    if save == 'y' or save == 'Y':  # 输入 y 则保存日记
        target.write(line)
        target.write('\n')  # 保存完后换行
        print "保存完毕！",
    else:
        print "不保存...",

# 主程序


if writeread == 'write':
    target = open('daily.txt','a') #以追加的模式打开文件
    print "请记录日记内容："
    ct = 'y' # 初始化 ct
    while ct == 'y' or ct == 'Y': # 当输入不是 y 时退出循环
        write(target)
        ct = raw_input("是否继续写日记(y/n)？")
    target.close()


elif writeread == 'read':
    target = open('daily.txt','r') #以读取的模式打开文件
    print "读取日记......"
    print "-" * 40
    print target.read()
    target.close()


else:
    print "写日记请输入 write，读日记请输入 read"
