# 快速入门

## 一个最小的应用

```python
from flask import flask  #导入了类Flask
app = Flask(__name__)    #创建类的实例

@app.route('/')          #使用装饰器route()告诉Flask哪个URL才能触发函数
def hello_world():		 #给特定函数生成URLs，并且返回我们要显示在浏览器上的信息
    return 'Hello World!'

if __name__ == '__main__':
    app.run()			 #最后用run()启动本地服务器来运行应用
```

把它保存成.py文件，然后用 Python 解释器运行它。不要起名叫 flask.py，因为会与 Flask 本身冲突。

```
python hello.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

进到浏览器浏览 http://127.0.0.1:5000/，哈哈，Hello World！

* `if __name__ == '__main__':` 

确保服务器只会在该脚本被 Python 解释器直接执行的时候才会运行，而不是作为模块导入的时候。

* 外部可见服务器，只要改变 run() 的调用对象如下这样：

`app.run(host = '0.0.0.0')`

让操作系统去监听所有公开的 IP。

## 调试模式

Flask 启用调试支持后，可以让代码修改的时候服务器能够自动加载，更加直观便携，而不用每次都要手动重启服务器。

```python
#1
app.debug = True
app.run()
#2
app.run(debug = True)
```

以上两种方法的效果是一样的。  
参考[使用调试器](http://www.pythondoc.com/flask/errorhandling.html#working-with-debuggers)

## 路由

route() 装饰器是用于把一个函数banding到一个 URL 上。

```python
@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello():
	return 'Hello World'
```

但是不仅如此，我们还可以动态地构造 URL 的特定部分，也可以在一个函数上附加多个规则。

## 变量规则

为了给 URl 增加变量的部分，你需要把特定的字段标记成<variable_name>。着些特定的字段将作为参数传入函数。也可以通过转换器传入。

```python
@app.route('/user/<username>')
def show_usr_profile(username):
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %d' % post_id
```

转换器：

- **int**：接受整数
- **float**：接受浮点数
- **path**：和默认的相似，但也接受斜线

## 构建 URL

用函数 **url_for()** 来针对一个特定的函数构建一个 URL。接受函数名作为第一参数，以及一些关键字参数，每个关键字参数对应于 URl 规则的变两部分。未知变两部分被插入到 URL 中作为查询参数。

```python
>>> from flask import Flask, url_for
>>> app = Flask(__name__)
>>> @app.route('/')
... def index(): pass
...
>>> @app.route('/login')
... def login(): pass
...
>>> @app.route('/user/<username>')
... def profile(username): pass
...
>>> with app.test_request_context():
...  print url_for('index')
...  print url_for('login')
...  print url_for('login', next='/')
...  print url_for('profile', username='John Doe')

/
/login
/login?next=/
/user/John%20Doe
```

## HTTP 方法

web 应用协议有不同的方法来访问 URLs。默认情况下，路由只会响应 GET 请求，但是能够通过给 route() 装饰器提供 methods 参数来改变。

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
```

> 什么是 HTTP 方法  

>	- GET：通知服务器只获取页面的信息并且发送回来。最常用。
>	- HEAD：告诉服务器获取信息，但是只对头信息感兴趣，不需要整个页面的内容。
>	- POST：浏览器通知服务器它要在 URL 上提交一些信息，服务器必须保证数据被存储且只存储一次。这是 HTML 表单通常发送数据到服务器的方法。
> 	- PUT：同 POST 类似，但是服务器可能触发了多次存储过程，多次覆盖掉旧值。
> 	- DELETE：移除给定位置的信息。
>	- OPTIONS：给客户端提供一个快速地途径来指出这个 URL 支持哪些 HTTP 方法。

## 静态文件

只要在你的包中或模块旁边创建一个名为 static 的文件夹，在应用中使用 /static 即可访问。

给静态文件生成 URL，使用特殊的 'static' 端点名：

`url_for('static', filename = 'style.css')`

这个文件应该存储在文件系统上称为 static/style.css

## 渲染模板

在 Python 中生成 HTML 相当的繁琐，因为必须自行做好 HTML 转义以保持应用程序的安全。由于这个原因，FLask 自动为你配置好 Jinja2 模板。

你可以使用方法 render_template() 来渲染模板。所有你需要做得就是提供模板的名称以及你想要作为关键字参数传入模板的变量。这里有个渲染模板的简单例子：

```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

文件结构：

- Case 1:一个模块：

```
/app.py
/templates
	/hello.html
```

- Case 2:一个包：

```
/app
	/__init__.py
	/templates
		/hello.html
```

这里是一个模板的例子：

```html
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello World!</h1>
{% endif %}
```

## 接收请求数据

对于 web 应用来说，对客户端发送给服务器的数据做出反应至关重要。在 Flask 中由全局对象 request 来提供这些信息。

例子：

```python
from flask import request

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
```

