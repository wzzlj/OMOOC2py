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

    app = Application()
# 设置窗口标题:
    app.master.title('Hello World')
# 主消息循环:
    app.mainloop()
```

## 三、添加组件

### 写入日记需要的组件
> 写入日记，必然需要一个可以输入的地方，输入后可以被传送到日记本里。

#### 1. Entry 组件

> 用于接受用户Entry小窗口部件单行文本字符串。
> - 如果你想显示多行文本可以编辑，那么你应该使用文本部件。
> - 如果你想显示一个或多个行文本不能由用户修改，那么你应该使用标签部件。  

- 其中：get( ):Returns the entry's current text as a string.
- 设置一个窗口用于输入文字

```python
    self.Input = Entry(self)
    self.Input.pack()
		```

#### 2. Button 组件

- 设置一个 Button 用来执行保存一行文本的命令

```python
# 设置一个用来保存的 Button
	self.saveButton = Button(self, text='保存', command=self.write)
	self.saveButton.pack()

# 定义一个函数写入日记本
def write(self):
    target = open('daily.log','a')    # 以追加模式打开日记
    line = self.Input.get()    # 获取输入的文字
    target.write(line + '\n')    # 将文字写入
    target.close()    # 关闭日记本
	```

### 读取日记需要的组件

#### 1. Label 组件
Label 组件用来在窗口上显示文字内容。
- 先定义一个函数读取日记文件
```python
def read(self):
    target = open('daily.log','r')
    content = target.read()
    return content
			```

- 用 Label 取出读取的内容，打印在主窗口上

```python
    self.label1 = Label(self, text = self.read())
    self.label1.pack()
```
