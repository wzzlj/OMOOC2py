# _*_ coding:utf-8 _*_
# 习题38：列表的操作

ten_things = "Apples Oranges Crow Telephone Light Suger"
print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding:", next_one
    stuff.append(next_one)
    print more_stuff
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop() #移除并返回被删除的对象，默认参数是最后一个对象
print stuff
print '|'.join(stuff)
print '#'.join(stuff[3:5])
