# bottle 框架学习(一)

## 前言

去琢磨了一下 Flask，有些理解不能，先尝试一下 bottle。

## 安装bottle：

`pip install bottle`

## 静态路由

```python
from bottle import route, run

@route('/start')
def start():
	return "<h1>hello, this is my first bottleprocess</h1>"
run(host='0.0.0.0', port=8000)	#开启服务，端口是8000，允许任何ip地址访问
```

保存并执行文件 `python hello.py`

在浏览器中输入 `http://0.0.0.0:8000/start`

注释：  
Route()是一个修饰器的函数名，它可以将一段代码绑定到一个 URL，这里就是将 start() 函数绑定给了 /start。

## 动态路由

动态路由就是可以用 url 传递不同额内容或参数到网页上：

```python
@route('/start/<sth>')
def start(sth):
   return "<h1>hello, this is my %s bottleprocess</h1>" % sth
```

在 url 中，输入不同的值，就会出现不同的内容。

## HTTP 请求方法

HTTP 协议有很多请求方法。route 默认使用 GET 方法，只响应 GET 请求。method 参数可以给 route() 函数指定使用哪种方法。或用 get()，post()，put()或delete()等函数来代替 route()函数

POST 方法一般用于 HTML 表单的提交。下面是一个使用 POST 来实现用户登录的例子：

## 静态文件映射

Bottle 不会处理像图片或 CSS 文件的静态文件请求。你需要给静态文件提供一个 route，一个回调函数（用于查找和控制静态文件的访问）。

```python
@route('/static/<filename:path>')
def server_static(filename):
	return static_file(filename,root='./static/')
```

需要在根目录下新建一个 static 文件夹，并把静态文件放在这个目录下面。

## 错误页面

如果页面出错，Bottle 会显示一个默认的错误页面，提供足够的 debug 信息。当然也可以用 error() 函数自定义错误页面：

```python
@error(404)
def error_page(error):
	return '没有你要访问的页面!'
```

## 模板的使用

Bottle 内置了一个快速强大的模板引擎，称为 SimpleTemplate 模板引擎。可通过 template() 函数或 view() 修饰器来渲染一个模板。只需提供模板的名字和传递给模板的变量。

文件结构：

```
\templ.py
\views
	\hello.tpl
```

```python
@route('/hello')
def hello():
	return template('hello')
```


```html
#hello.tpl
<html>
	<head>
	<title>hello page!</title>
	</head>
	<body>
	<h1>hello world!</h1>
	<h2>hello world!</h2>
	<h3>hello world!</h3>
	</body>
</html>
```

默认情况下，Bottle 会再 ./views/ 目录查找模板文件（或当前目录）。也可以使用 `bottle.TEMPLATE_PATH.append('目录地址')` 的方式来增加更多的模板路径。

## 使用 view() 修饰器来渲染模板

view() 修饰器允许你在回调函数中返回一个字典，并将其传递给模板，和 template() 函数做同样的事情。

```python
@route('/aboutme')
@view('hello')
def aboutme():
	name = "wzzlj"
	blog = "http://wzzlj.github.io"
	myhome = "Wenzhou"
	myinfodir = {'age':27, 'weight':175, 'hight':181}
	info = {'name':name,'age':myinfodir,'weight':myinfodir,'blog':blog,
			'myhome':myhome, 'hight':myinfodir}
	return info
```

```html
#hello.tpl
<html>
	<head>
	<title>My Information</title>
	</head>
	<body>
	<h1>我的信息</h1>
	<p>姓名：{{ name }}</p>
	<p>年龄：{{ age.get('age') }}</p>
	<p>体重：{{ weight.get('weight') }}</p>
	<p>身高：{{ hight.get('hight') }}</p>
	<p>家乡：{{ myhome }}</p>
	<p>博客：{{ blog }}</p>
	</body>
</html>
```

## 给模板传递数据

```python
@route('/hello')
def hello():
	name = "wzzlj"
	myinfodir = {'age':27, 'weight':175, 'hight':181}
	blog = "http://wzzlj.github.io"
	myhome = "Wenzhou"
	return template('hello',name=name,age=myinfodir, weight=myinfodir,
					hight=myinfodir, blog=blog, myhome=myhome)
```
