# 简单日记本2.0思路

> 在基于第一个版本的基础上，进行优化，一是在界面和布局上，二是在功能上。

## 0. 代码优化

- 将每一个组建转化为单独的函数，然后在 createwight 函数内导入。
- 将打包组建的命令集中在一个函数内，使得更改布局更加方便。

## 1. 实时显示日记内容

- 刚开始在 Label 用变量的方式，一直行不通
- 转换思维，用 Text 的 Insert 命令实现实时显示（伪）

``` python
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
```

- ​