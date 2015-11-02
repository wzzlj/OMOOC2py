# bottle 框架学习（二）

## 模板的进阶使用

### 内嵌语句

只要在 {{...}} 中的 Python 语句返回一个字符串或有一个字符串的表达形式，它就是一个有效的语句。

```python
>>>from bottle import template
>>>template('hello {{name}}', name='ju')
u'helloju'
>>>template('hello {{name if name else "world!"}}', name=None)
u'helloworld!'
>>>template('hello {{name if name else "world!"}}',name="feige")
u'hellofeige'
```

{{}} 中的 Python  语句会在渲染的时候被执行，可访问传递给 SimpleTemplate.render() 方法的所有参数。默认情况下，自动转义 HTML 标签以防止 XSS 攻击。可在语句前加上 `!` 来关闭自动转义。

```python
>>>template('hello {{name if name else "world!"}}',name="<b>feige</b>")
u'hello&lt;b&gt;feige&lt;/b&gt;'
>>>template('hello {{!name if name else "world!"}}',name="<b>feige</b>")
u'hello<b>feige</b>'
```

### 在模板中嵌入 Python 代码

以 % 开头，表明这一行是 Python 代码。它和真正的 Python 代码唯一的区别是需要在末尾添加 %end 语句，表明一个代码的结束。这样就不用担心 Python 代码中得缩进问题，SimpleTemplate 模板引擎的 parser 帮你处理了。以 % 开头的行，被当做普通文本来渲染。只有在行首的 % 字符才有意义，可以使用 %% 来转义。%% 表示以 % 开头的行，%%% 表示以 %% 开头的一行。

```python
# encoding:utf-8

from bottle import route,run,view

@route('/hello')
@view('hello_template')
def hello():
	name = "wzzlj"
	blog = "http://wzzlj.github.io"
	myfriend = {'一二三','四五六','七八九'}
	myinfodir = {'age':29,'weight':138}
	info = {'name':name,'age':myinfodir,
			'weight':myinfodir,'blog':blog,
			'SNS':myfriend}
	return info

run(host='0.0.0.0',port=8000,debug=True)
```

```html
<html>
	<head>
	<title>My Information!</title>
	</head>
	<body>
	<h1>My Information:</h1>
	<p>姓名：
	%if name:
		Hi <b>{{ name }}</b>
	%else:
		<i>Hello world</i>
	%end
	</p>
	<p>年龄：{{ age.get('age') }}</p>
	<p>体重：{{ weight.get('weight') }}</p>
	<p>博客：{{ blog }}</p>
	<p>朋友圈：
	%for i in SNS:
		{{ i }}
	%end
	</p>
	</body>
</html>
```

### 模板继承

模板继承主要使用 %include 和 %rebase 两个语句实现。

使用 %include sub_template [kwargs] 语句来包含其他模板。
sub_template 参数是模板的文件名或路径。  
[kwargs] 部分是以逗号分开的键值对，是传给其他模板的参数。  
**kwargs 这样的语法来传递一个字典也是允许的。

(这一节有点儿复杂，知道有这回事就可以了)

## 文件的下载与上传

### 下载文件

Bottle 文件下载是 static_file 这个模块，多加了一个参数：  
`download = True`

```python
# encoding=utf-8

from bottle import route,run,view,static_file

@route('/download/<filename:path>')
def download(filename):
	return static_file(filename,root='./static/',download=True)
run(host='0.0.0.0',port=8000,debug=True)
```

上面的方法是用 URL 直接下载，下面演示使用链接下载：

```python
# encoding=utf-8

from bottle import route,run,view,static_file,template

@route('/download/<filename:path>')
def download(filename):
	return static_file(filename,root='./static/',
						download=True)

@route('/hello')
def hello():
	return template('hello')

run(host='0.0.0.0',port=8000,debug=True)
```

```html

<html>
	<head>
	<title>下载页</title>
	</head>
	<body>
	<a href="/download/paojie.jpg">下载文件</a>
	</body>
</html>
```

### 上传文件

上传文件时在前端 form 表单中，要添加 enctype="multipart/form-data" 属性，enctpye="multipart/form-data" 的意思，是设置表单的 MIME 编码。默认情况，这个编码格式是 application/x-www-form-urlencoded，不能用于文件上传，只有使用 multipart/form-data，才能完整的传递文件数据。

在后端，用 request.files 方法，获取到表单传上来的文件，首先把对象赋值给一个变量名，如 uploadfile，然后用 save() 的方法来保存到服务器中。
uploadfile.save(save_path,overwrite=True),save_path是保存文件的路径，overwrite=True 是指如果服务器的上传目录已有同名文件存在，则覆盖。

```python
upload_path='./static/'
@route('/upload')
def upload():
	return template('upload')

@route('/upload',method='POST')
def do_upload():
	uploadfile=request.files.get('data')
	uploadfile.save(upload_path,overwrite=True)

	return u"上传成功，文件名为： %s，文件类型为：%s" % (uploadfile.filename, 
												uploadfile.content_type)
```

```html
# upload.tpl
<html>
	<head>
	<title>上传文件</title>
	</head>
	<body>
	<form action="upload" method="POST" enctype="multipart/form-data">
	<input type="file" name="data" />
	<input type="submit" value="Upload" />
	</form>
	</body>
</html>			
```
