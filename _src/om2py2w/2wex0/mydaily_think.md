# python桌面化——Tinker

## 一、什么是 Tinker？
> Tkinter 是Python的标准GUI库。Python使用Tkinter可以快速的创建GUI应用程序。
由于Tkinter是内置到python的安装包中、只要安装好Python之后就能import Tkinter库、而且IDLE也是用Tkinter编写而成、对于简单的图形界面Tkinter还是能应付自如。

## 二、最小的 Tinker 框架

```python
from Tkinter import *  # 首先把 Tkinter 模块导入

class Application(Frame):  # 基本框架

    def __init__(self, master=None):
    Frame.__init__(self, master)
    self.pack()
    self.createWidgets()

    def createWidgets(self):   # 组件

root = Tk()
app = Application(master=root)
# 设置窗口标题:
app.master.title('简单日记本')
# 主消息循环:
app.mainloop()
```

## 三、添加组件

### 写入日记需要的组件
> 写入日记，必然需要一个可以输入的地方，输入后可以被传送到日记本里。

#### 0. 实现中文输入
```python
import sys
reload(sys)
sys.setdefaultencoding('utf8')
```
#### 1. Entry 组件

> 用于接受用户Entry小窗口部件单行文本字符串。
> - 如果你想显示多行文本可以编辑，那么你应该使用文本部件。
> - 如果你想显示一个或多个行文本不能由用户修改，那么你应该使用标签部件。  


- 设置一个窗口用于输入文字


```python
self.label1 = Label(self, text='输入文字:').pack(side=LEFT)
self.Input = Entry(self, width=43)
self.Input.pack(side=LEFT)
```

#### 2. Button 组件

- 设置一个 Button 用来执行保存一行文本的命令
- 其中，get( ):Returns the entry's current text as a string.
- 保存后清空组件内文字

```python
# 设置一个用来保存的 Button
self.saveButton = Button(self)
self.saveButton['text'] = '保存'
self.saveButton['command'] = self.write
self.saveButton.pack(side=LEFT)

# 定义一个函数写入日记本
def write(self):
    target = open('daily.log','a')
    line = self.Input.get()
    self.Input.delete(0,END) # 保存后清空文字框
    target.write('\n' + line)
    target.close()
```

### 读取日记需要的组件

####  Button 组件 + tkMessageBox 函数

- 先定义一个函数读取日记文件

```python
# 读取日记
def read(self):
    tkMessageBox.showinfo('读日记',open('daily.log','r').read())

# 添加读取按钮
self.readbutton = Button(self, text='读日记',command=self.read)
self.readbutton.pack(side=RIGHT)
```


### 初始化日记和退出

#### Menu 组件

```python
# 定义一个初始化的函数
def clear(self):
    target = open('daily.log','w')
    target.close()

# 设置菜单栏
menubar = Menu(self)  # 定义菜单栏
self.filemenu = Menu(menubar, tearoff=0)  # 第一个菜单栏
self.filemenu2 = Menu(menubar, tearoff=1) # 第二个菜单栏
menubar.add_cascade(label='File', menu=self.filemenu) # 第一个菜单栏参数
self.filemenu.add_command(label='初始化',command=self.clear) # 下拉菜单栏设置
self.filemenu.add_command(label='退出',command=self.quit)
self.master.config(menu = menubar)  # 让主窗口显示菜单栏
```

## 效果
![](http://7xn3v1.com1.z0.glb.clouddn.com/15-10-25/42243092.jpg)
![](http://7xn3v1.com1.z0.glb.clouddn.com/15-10-25/23173296.jpg)

- 虽然丑了点！但是这是我第一个有界面的程序啊！！\(^o^)/

---

# 迭代
- 20151025 初步完成
