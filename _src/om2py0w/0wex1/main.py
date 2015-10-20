# _*_ coding:utf-8 _*_

from sys import argv #获取外部命令的参数

import time #载入时间模组

script,  writeread = argv

# 写日记功能------------------------------------------------

def write(target):
    line = raw_input('> ')

    localtime = time.asctime( time.localtime( time.time()))

    save = raw_input('是否保存(y/n)？ ')

    if save.lower() == 'y':  # 输入 y 则保存日记
        target.write("[%s]\t" % localtime)
        target.write(line)
        target.write('\n')  # 保存完后换行
        print "保存完毕！",
    else:
        print "不保存...",


# 主程序----------------------------------------------------


if writeread.lower() == 'w':  # 如果命令参数是 w，则进入写日记模式，lower 讲字符全部转换为小写
    target =  file('daily.txt','a') #以追加的模式打开文件
    print "请记录日记内容："
    ct = 'y' # 初始化 ct
    while ct.lower() == 'y' : # 当输入不是 y 时退出循环,
        write(target)
        ct = raw_input("是否继续写日记(y/n)？")
    target.close()


elif writeread.lower() == 'r':   # 如果命令参数是 r，则进入读日记模式
    target = open('daily.txt','r') #以读取的模式打开文件
    print "读取日记......"
    print "-" * 60
    print target.read()
    target.close()


elif writeread.lower() == 'i':  # 如果命令参数是 i，则初始化日记
    
    confirm = raw_input('警告！将初始化日记！是否继续(y/n)？ ')

    if confirm.lower() == 'y':
        target = file('daily.txt','w')
        print "初始化完毕..."
        target.close()

else:
    print "写日记请输入 w，读日记请输入 r，初始化日记请输入 i"
