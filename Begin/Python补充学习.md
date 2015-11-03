# Python 补充学习

## 模块、类和对象

### 调用模块，并访问函数

假如有一个模块名叫 mystuf.py，并且里面有一个叫 apple 的函数

- 访问函数

```python
import mystuff
mystuff.apple()
```

- 访问变量

`mystuff.variable`

### 类的导入

有一个类是这样的

```python
class Mystuff(object):
	
	def __init__(self):
		self.tangerine = "Hello world!"
	def apple(self):
		print "I am an Apple!"
```

然后导入类之前需要把类实例化：

```python
thing = Mystuff()
thing.apple()
print thing.tangerine
```

## 继承与合成

有经验的程序员知道如何躲开『继承』这东西。

> 大部分使用继承的场合都可以用合成取代，而多重继承则需要不惜一切地避免之。

### 什么是继承

`class Foo(bar)` ，代码就发生了继承：『创建一个叫 Foo 的类，并让它继承 Bar』。  
这样写后，Python 会让 Bar 的实例所具有的功能都工作在 Foo 的实例上。  
这样可以让你把通用的功能放到 Bar 里面，然后再给 Foo 特别设定一些功能。

- 隐式继承

```python
class Parent(object):
	
	def implicit(self):
		print "hahahahaha"

class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
```

child 类里面没有任何细节，但是从它的父类继承了所有行为，运行起来是这样的：

```
python test.py
hahahahaha
hahahahaha
```

可见，就算 son.implicit()调用了 Child 里面没有定义过的 implicit 函数，这个函数依然可以工作。  
需要很多类的时候，这样可以避免重复写很多代码。

- 显式覆盖

有的时候不想让子类的函数和父类的行为一样，只要在子类中定义一个相同名字的函数就可以了。

```python
class Parent(object):
	
	def override(self):
		print "hahahahaha"

class Child(Parent):
	
	def override(self):
		print "kaokaokao"

dad = Parent()
son = Child()

dad.override()
son.override()
```

运行起来就是：

```
hahahahaha
kaokaokao
```

- 在运行前或运行后覆盖

不想用父类的函数时用定义同一个名字的函数进行覆盖，  
想用的时候，用 `super(Child,self).hanshuming()`，就可以重新切换回父类的函数了。

### 合成




