# encoding: UTF-8
# __author__ = 'zhulijian'

from Tkinter import *
import os 
from PIL import Image, ImageTk  # easy_install pil 识别其他图片
import socket

# 确保中文输入能正确传送
import sys
reload(sys)
sys.setdefaultencoding('utf8')

root = Tk()
root.geometry('400x420+400+400')

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master, bg='white')    # 一个 frame 框架
        self.pack()
        self.createWidgets()
        self.createudp()

    def createudp(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(("",0))
        self.s.sendto('-r', ('127.0.0.1', 8888))    #立即从服务器获取消息
        self.rectext = self.s.recv(1024) + '\n'
        self.readtext.config(state = NORMAL)
        self.readtext.insert(END, self.rectext, "center")
        self.readtext.see(END)
        self.readtext.config(state = DISABLED)

    def sendhost(self, self2):
        self.inp = self.input.get()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.sendto(self.inp, ('127.0.0.1', 8888))
        self.rectext = self.s.recv(1024)
        self.readtext.config(state = NORMAL)
        self.readtext.insert(END, self.rectext + '\n', "center")
        self.readtext.see(END)
        self.readtext.config(state = DISABLED)       
        self.input.delete(0,END)

# 创建组件
    def createWidgets(self):
        self.banner()
        self.readtext()
        #self.inputhost()
        self.inputtext() 
        self.menu()
        self.gridWidgets()

    def gridWidgets(self):     # 布局
        self.banner.grid     (row=0, column=0, columnspan=5)

        #self.label_host.grid (row=1, column=0)
        #self.entry_host.grid (row=1, column=1)
        #self.label_port.grid (row=1, column=2)
        #self.entry_port.grid (row=1, column=3)
        #self.button_link.grid(row=1, column=4)
        self.readtext.grid   (row=2, column=0, columnspan=5, sticky=W)

        self.label1.grid     (row=3, column=0)
        self.input.grid      (row=3, column=1, columnspan=4)

    def banner(self):
        self.banner = Canvas(self, width=350, height=70, bg='white')
        self.banner.create_image(175,40,image=im)

    def readtext(self):        
        self.readtext = Text(self,width=51, height=20)
        self.readtext.tag_configure('center',justify='left')
        #self.readtext.config(bg='gray')
        #self.readtext.config(state = NORMAL)
        #self.readtext.insert(END, self.rectext, "center")
        #self.readtext.see(END)
        self.readtext.config(state = DISABLED)
    
    def inputtext(self):
        self.label1 = Label(self, text=' 输入', anchor='w')
        #self.label1.config(bg='red')
        self.input = Entry(self, width=35)
        #self.input.config(bg='bule')
        self.input.bind("<Return>", self.sendhost)
        self.input.focus_set()
        
    def menu(self):
        menubar = Menu(self)
        self.filemenu = Menu(menubar, tearoff=0)
        self.filemenu2 = Menu(menubar, tearoff=1)
        menubar.add_cascade(label='File', menu=self.filemenu)
        menubar.add_cascade(label='Author:xmuzlj@gmail.com', menu=self.filemenu2)
        self.filemenu.add_command(label='退出',command=self.quit)
        self.master.config(menu = menubar)

'''
    def inputhost(self):
        self.label_host = Label(self, text='IP')
        self.entry_host = Entry(self)
        self.label_port = Label(self, text='PORT')
        self.entry_port = Entry(self)
        self.button_link = Button(self, text='连接', command=self.createudp)
'''

def main():
    global im
    image = Image.open("banner.png")
    im = ImageTk.PhotoImage(image)
    if os.path.isfile('daily.log')==False:  # 检查是否存在 daily 文件
        f = open('daily.log','w')
        f.close()
    app = Application(master = root)
    app.master.title('简单日记本客户端')
    app.mainloop()

if __name__ == "__main__":
     # 图片显示需要全局变量

    main()

