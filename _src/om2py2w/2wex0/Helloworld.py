# encoding: UTF-8
# __author__ = 'zhulijian'

from Tkinter import *
import tkMessageBox

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def write(self):
        target = open('daily.log','a')
        line = self.Input.get()
        line = line.decode('gbk')

        target.write('\n' + line)
        target.close()
        self.update(self.label1())
    
    def read(self):
        target = open('daily.log','r')
        content = target.read()
        return content


    def createWidgets(self):

        self.label1 = Label(self, text = self.read())
        self.label1.pack()

        self.Input = Entry(self)
        self.Input.pack()

        self.saveButton = Button(self, text= '保存', 
                                command = self.write)
        self.saveButton.pack()

        self.quitButton = Button(self, text = '退出', 
                                command = self.quit)
        self.quitButton.pack()





app = Application()
app.master.title('Hello World')
app.mainloop()
