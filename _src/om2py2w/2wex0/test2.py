#coding:utf-8__author__ = 'zhulijian'import Tkinterimport tkMessageBoxroot = Tk()li = ['哈哈','写入日记','清空日记']li2 = ['休息一下','睡你妈逼起来嗨']list = Listbox(root)list2 = Listbox(root)for item in li:	list.insert(0,item)for item in li2:	list2.insert(0,item)w = Button(root)w.pack()list.pack()list2.pack()root.mainloop()