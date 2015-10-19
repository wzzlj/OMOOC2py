# 简单日记本编程思路

## 初步思路

- 命令后参数write 和 read 分别对应『写日记』和『读日记』两个功能
- 即输入 `python main.py write` 进入写日记模式
  - 提示输入一行日记
  - 输入一行日记
  - 输入完成后将内容输出到文件 `daily.txt` 中
  - 接受命令
    - 保存 or 放弃？
    - 继续 or 退出？
- 输入 `python main.py read` 则进入读日记模式
  - 打开日记文件并读取
  - 将内容打印到屏幕

## 逐步完成

### 0. 中文编码

`# _*_ coding:utf-8 _*_`

### 1. 读取外部命令

使用 `from sys import argv` 读取外部命令

### 2. 根据命令不同，指向不同语句
自然是用到 `if...elif...else...` 了

- 打造初步框架

```python

# _*_ coding:utf-8 _*_

from sys import argv #获取外部命令的参数

script,  writeread = argv

if writeread == 'write':
    print "It's write."

elif writeread == 'read':
    print "It's read."
```

- 运行结果
![](http://7xn3v1.com1.z0.glb.clouddn.com/15-10-19/15179897.jpg)

### 3. 初步实现『写日记』功能

- 首先以追加模式打开 `daily.txt`
  - 追加模式`'a'`确保每次写入的是新的一行
```python
if writeread == 'write':
    target = open('daily.txt','a') #以追加的模式打开文件
    print "请记录日记内容："
    write(target)
    target.close()
```

- 定义`write()`函数
```python
# 写日记功能
def write(target):
    line = raw_input('> ')

    print "是否保存？",
    save = raw_input('(y/n?) ')

    if save == 'y' or save == 'Y':  # 输入 y 则保存日记
        target.write(line)
        target.write('\n')  # 保存完后换行
        print "保存完毕！"
    else:
        print "不保存..."
```
- 运行
![](http://7xn3v1.com1.z0.glb.clouddn.com/15-10-19/69000263.jpg)
![](http://7xn3v1.com1.z0.glb.clouddn.com/15-10-19/83364070.jpg)

### 4. 初步实现『读日记』功能

- 关键是`read`
```python
elif writeread == 'read':
    target = open('daily.txt','r') #以读取的模式打开文件
    print "读取日记......"
    print "-" * 40
    print target.read()
    target.close()
```
- 运行结果

![](http://7xn3v1.com1.z0.glb.clouddn.com/15-10-19/88378122.jpg)

### 5.持续交互

> 在记录一行日记后可以选择继续写还是退出。

- 执行完『写日记』后，提示继续还是退出
  - 选择继续，重新循环一次『写日记』
  - 选择退出，则结束
- 选择使用 `while` 循环
```python
ct = 'y' # 初始化 ct
while ct == 'y' or ct == 'Y': # 当输入不是 y 的时候退出循环
    write(target)
    ct = raw_input("是否继续写日记(y/n)？")
```

- 运行结果

![](http://7xn3v1.com1.z0.glb.clouddn.com/15-10-19/58103628.jpg)

---
# 迭代

- [1wd1]完成初步设想
