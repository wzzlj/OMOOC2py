# encoding: UTF-8
# __author__ = 'zhulijian'

from Tkinter import *
import tkMessageBox

import sys
reload(sys)
sys.setdefaultencoding('utf8')

root = Tk()
root.geometry('600x30+400+400')

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

# 写入日记
    def write(self):
        target = open('daily.log','a')
        line = self.Input.get()
        self.Input.delete(0,END) # 保存后清空文字框
        target.write('\n' + line)
        target.close()

# 读取日记
    def read(self):
        tkMessageBox.showinfo('读日记',open('daily.log','r').read())

# 清除日记
    def clear(self):
        target = open('daily.log','w')
        target.close()



# 创建组件
    def createWidgets(self):

        self.readbutton = Button(self, text='读日记',command=self.read)
        self.readbutton.pack(side=RIGHT)

        self.label1 = Label(self, text='输入文字:').pack(side=LEFT)
        self.Input = Entry(self, width=43)
        self.Input.pack(side=LEFT)

        self.saveButton = Button(self)
        self.saveButton['text'] = '保存'
        self.saveButton['command'] = self.write
        self.saveButton.pack(side=LEFT)

        menubar = Menu(self)
        self.filemenu = Menu(menubar, tearoff=0)
        self.filemenu2 = Menu(menubar, tearoff=1)
        menubar.add_cascade(label='File', menu=self.filemenu)
        menubar.add_cascade(label='Author:xmuzlj@gmail.com', menu=self.filemenu2)
        self.filemenu.add_command(label='初始化',command=self.clear)
        self.filemenu.add_command(label='退出',command=self.quit)
        self.master.config(menu = menubar)

def main():
    app = Application(master = root)
    app.master.title('简单日记本')
    app.mainloop()

if __name__ == "__main__":
    main()
