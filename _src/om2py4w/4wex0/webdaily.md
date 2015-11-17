# WebDaily 开发记录

## 理清概念

### 什么是框架？为什么有框架？

> 软件框架（Software framework），通常指的是为了实现某个业界标准或完成特定基本任务的软件组件规范，也指为了实现某个软件组件规范时，提供规范所要求之基础功能的软件产品。
> 
> 框架的功能类似于基础设施，与具体的软件应用无关，但是提供并实现最为基础的软件架构和体系。软件开发者通常依据特定的框架实现更为复杂的商业运用和业务逻辑。这样的软件应用可以在支持同一种框架的软件系统中运行。
> 
> 简而言之，框架就是制定一套规范或者规则（思想），大家（程序员）在该规范或者规则（思想）下工作。或者说就是使用别人搭好的舞台，你来做表演。

『使用别人搭好的舞台，你来做表演。』这句应该说的非常形象了。也就是我在进行 web 开发时，不需要进行底层的代码编写，而是使用框架这个舞台，更方便的去实现我想实现的东西。

### Python 世界中有哪些框架？

- **Django**:这是一个被广泛应用的框架，如果看官在网上搜索，会发现很多公司在招聘的时候就说要会这个，其实这种招聘就暴露了该公司的开发水平要求不高。框架只是辅助，真正的程序员，用什么框架，都应该是根据需要而来。当然不同框架有不同的特点，需要学习一段时间。
- Flask：一个用Python编写的轻量级Web应用框架。基于Werkzeug WSGI工具箱和Jinja2模板引擎。
- Web2py：是一个为Python语言提供的全功能Web应用框架，旨在敏捷快速的开发Web应用，具有快速、安全以及可移植的数据库驱动的应用，兼容Google App Engine（这是google的元计算引擎，后面我会单独介绍）。
- Bottle: 微型Python Web框架，遵循WSGI，说微型，是因为它只有一个文件，除Python标准库外，它不依赖于任何第三方模块。
- Tornado：全称是Torado Web Server，从名字上看就可知道它可以用作Web服务器，但同时它也是一个Python Web的开发框架。最初是在FriendFeed公司的网站上使用，FaceBook收购了之后便开源了出来。
- webpy: 轻量级的Python Web框架。webpy的设计理念力求精简（Keep it simple and powerful），源码很简短，只提供一个框架所必须的东西，不依赖大量的第三方模块，它没有URL路由、没有模板也没有数据库的访问。

摘自http://blog.jobbole.com/72306/

### 为什么大妈推荐 Bottle？

前面已经说到了，因为 Bottle 是一个微型的 Python Web 框架，小到只有一个3000多行代码的文件，不需要依赖任何第三方模块，并且可以实现绝大部分的功能。

## 用 Bottle 快速完成原型

### Bottle 框架的安装和教程

Install Bottle with `pip install bottle` or download the source package at PyPI.

教程参考：http://bottlepy.org/docs/dev/index.html

### 发布一个网站

Here is the simple example:

```python
from bottle import route, run, template

@route('/hello/<name>')			#<---路由
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)	#<---html 代码作为文本导入并识别，并可以导入变量 name

run(host='localhost', port=8080, debug=True)
```

### HTTP 请求方法

#### POST方法通常用于 HTML 表单的提交。

```python
from bottle import get, post, request # or route

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
```

这里例子中 /login URL关联了两个截然不同的回调函数，一个用于GET请求，另一个用于POST请求。第一个请求为用户展示了一个HTML表单，当表单提交的时候调用第二个请求，用于验证用户所输入的登录凭证。

所以我的思路是：

- 先为用户展示一个『文本框』是读取日记文件后的输出。
- 而后将『输入框』的内容作为表单提交到服务器，并添加到日记文件内。
- 并实时更新『文本框』。

完成代码如下：

```python
from bottle import route, run, template, debug, request

@route('/daily')			#<---路由，默认为 GET
def daily():
    return template('daily', daily=open('daily.log','r').read())	#<---输入框

@route('/daily', method='POST')
def postdaily():
	d_add = request.forms.get('d_input')
	open('daily.log','a').write(d_add+'\n')		#<---写入到日记文件
	return template('daily', daily=open('daily.log','r').read())		#<---返回数据

run(host='localhost', port=8080, debug=True)
```

模板文件

```html
<!--简单日记本的模板文件-->
<!DOCTYPE html>
<html>
<body>
<div id="banner" style="width:1024px" align="center">
<div id="header" style="background-color:#FFA500">
<h1 style="margin-bottom: 0;">简单日记本 WEB 版</h1></div>
</div>
<div id="content" style="background-color: #EEEEEE;height: 800px;width: 1024px" align="center">
<p> </p>
<form action="/daily" method="post">
	日记输入: <input name="d_input" type="text" />
	<input value="save" type="submit" />
</form>
	<textarea cols=50 rows=50>{{ daily }}
   	</textarea>
</div>
</div>
</body>
</html>
```

这样基本上完成了初步功能。

