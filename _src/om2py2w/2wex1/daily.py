# encoding: UTF-8
# __author__ = 'zhulijian'

from Tkinter import *
import os 
from PIL import Image, ImageTk  # easy_install pil

# 确保中文输入能正确传送
import sys
reload(sys)
sys.setdefaultencoding('utf8')

root = Tk()
root.geometry('400x420+400+400')

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master, bg='white')
        self.pack()
        self.createWidgets()

# 写入日记
    def write(self, sefl2):
        target = open('daily.log','a')
        line = self.Input.get() + '\n'
        self.Input.delete(0,END) # 保存后清空文字框
        self.readtext.config(state = NORMAL)
        self.readtext.insert(END,line,'center')
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
        self.inputtext() 
        self.menu()
        self.banner()
        self.gridWidgets()
    
    def banner(self):
        
        self.banner = Canvas(self, width=350, height=70, bg='white')
        self.banner.create_image(175,40,image=im)

    
    def gridWidgets(self):     # 布局
        self.Input.grid(row=2,column=2)
        self.readtext.grid(row=1, column=1, columnspan=2, sticky=W)
        self.label1.grid(row=2, column=1)
        self.banner.grid(row=0, column=1, columnspan=2)

    def readtext(self):        
        self.readtext = Text(self,width=51, height=20)
        self.readtext.tag_configure('center',justify='center')
        #self.readtext.config(bg='gray')
        self.readtext.config(state = NORMAL)
        self.readtext.insert(END, open('daily.log','r').read(),"center")
        self.readtext.see(END)
        self.readtext.config(state = DISABLED)
    
    def inputtext(self):
        self.label1 = Label(self, text=' 输入', anchor='w')
        #self.label1.config(bg='red')
        self.Input = Entry(self, width=35)
        #self.Input.config(bg='bule')
        self.Input.bind("<Return>", self.write)
        self.Input.focus_set()
        

    def menu(self):
        menubar = Menu(self)
        self.filemenu = Menu(menubar, tearoff=0)
        self.filemenu2 = Menu(menubar, tearoff=1)
        menubar.add_cascade(label='File', menu=self.filemenu)
        menubar.add_cascade(label='Author:xmuzlj@gmail.com', menu=self.filemenu2)
        self.filemenu.add_command(label='初始化',command=self.clear)
        self.filemenu.add_command(label='退出',command=self.quit)
        self.master.config(menu = menubar)

def main():
    global im
    image = Image.open("banner.png")
    im = ImageTk.PhotoImage(image)
    if os.path.isfile('test.txt')==False:  # 检查是否存在 daily 文件
        f = open('daily.log','w')
        f.close()
    app = Application(master = root)
    app.master.title('简单日记本2.0')
    app.mainloop()

if __name__ == "__main__":
     # 图片显示需要全局变量

    main()

