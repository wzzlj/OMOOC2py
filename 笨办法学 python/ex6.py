# _*_ coding:utf-8 _*_

x = "这儿有 %d 种人。" % 10
binary = 'binary'
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not)

print x
print y

print "I said: %s." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious # 还能这样啊，这个屌炸天

w = "This is the left side of..."
e = "a string with a right side."

print w + e 