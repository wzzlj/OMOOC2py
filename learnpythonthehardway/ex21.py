# _*_ coding:utf-8 _*_
# 习题21：函数可以返回某些东西

def jia(a, b):
	print "做加法 %d + %d" % (a, b)
	return a + b

def jian(a, b):
	print "做减法 %d - %d" % (a, b)
	return a - b

def cheng(a, b):
	print "做乘法 %d * %d" % (a, b)
	return a * b

def chu(a, b):
	print "做除法 %d / %d" % (a, b)
	return a / b

print "我们可以做一些四则运算了~："

age = jia(30, 5)
height = jian (78, 4)
weight = cheng(90, 2)
iq = chu(100, 2)

print "年龄：%d, 身高：%d, 体重：%d, 智商：%d" % (age,height,weight,iq)

print "这是一个疑问。"

what = jia(age,jian(height,cheng(weight,chu(iq,2))))

print "结果是：%d " % what
