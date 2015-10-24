# __author__ = 'zhulijian'
# _*_ coding: utf-8 _*_

from Tkinter import *
import tkMessageBox


root = Tk()

l1 = root.Label(top, text = "请输入：").pack({"side" : "left"})


e1 = root.Entry(top, bd = 5).pack({"side" : "right"})

def helloCallBack():
	tkMessageBox.showinfo("人生苦短，Python 当歌！","今天天气不错~")

w = root.Button(top,text="我要学 Python！！！！！！",command = helloCallBack())

w.pack()
# 进入消息循环
top.mainloop()
