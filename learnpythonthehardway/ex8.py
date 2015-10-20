# _*_ coding:utf-8 _*_
# 打印，打印

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one","two","three","four")
print formatter % (True, False, False, True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
	"I had this thing,",
	"That you could ytpe up right.",
	"But it didn't sing",
	"So I said goodnight."
)

#最后一行既输出单引号又有双引号，是因为双引号那一行里边有单引号，为了区分。
