# encoding: UTF-8
# __author__ = 'zhulijian'

from Tkinter import *
import tkMessageBox

# 确保中文输入能正确传送
import sys
reload(sys)
sys.setdefaultencoding('utf8')

root = Tk()
root.geometry('400x400+400+400')

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

# 写入日记
    def write(self, sefl2):
        target = open('daily.log','a')
        line = self.Input.get() + '\n'
        self.Input.delete(0,END) # 保存后清空文字框
        self.readtext.config(state = NORMAL)
        self.readtext.insert(END,line)
        self.readtext.see(END)
        self.readtext.config(state = DISABLED)
        target.write(line)
        target.close()


# 清除日记
    def clear(self):
        target = open('daily.log','w')
        target.close()
        self.readtext.config(state=NORMAL)
        self.readtext.delete(1.0, END)
        self.readtext.config(state=DISABLED)


# 创建组件
    def createWidgets(self):

        self.readtext()

        self.label1 = Label(self, text='输入文字:').pack(side=LEFT)

        self.Input = Entry(self, width=50)
        self.Input.bind("<Return>", self.write)
        self.Input.pack(side=LEFT)



        menubar = Menu(self)
        self.filemenu = Menu(menubar, tearoff=0)
        self.filemenu2 = Menu(menubar, tearoff=1)
        menubar.add_cascade(label='File', menu=self.filemenu)
        menubar.add_cascade(label='Author:xmuzlj@gmail.com', menu=self.filemenu2)
        self.filemenu.add_command(label='初始化',command=self.clear)
        self.filemenu.add_command(label='退出',command=self.quit)
        self.master.config(menu = menubar)
        
    def readtext(self):        
        self.readtext = Text(self,width=40)
        self.readtext.config(state = NORMAL)
        self.readtext.insert(END, open('daily.log','r').read())
        self.readtext.see(END)
        self.readtext.pack()
        self.readtext.config(state = DISABLED)


def main():
    app = Application(master = root)
    app.master.title('简单日记本')
    app.mainloop()

if __name__ == "__main__":
    main()
