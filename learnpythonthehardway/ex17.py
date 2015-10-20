# _*_ coding:utf-8 _*_
# 习题17：更多文件操作

from sys import argv
from os.path import exists

script,from_file, to_file =argv

print "Copying from %s to %s" % (from_file,to_file)

# we could do these two on one line too ,how ?
in_file = open(from_file)
indata = in_file.read()

print "The inpuy file is %d bytes long" % len(indata)
print "Ready,hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file,'w') # 以写入模式打开文件
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
