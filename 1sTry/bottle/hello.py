# /usr/bin/bottle python
# encoding:utf-8

from bottle import route, run, static_file, error, template, view

@route('/start/<sth>')
def start(sth):
	return "<h1>hello, this is my %s bottleprocess</h1>" % sth

@route('/static/<filename:path>')
def server_static(filename):
	return static_file(filename,root='./static/')

@error(404)
def error_page(error):
	return '没有你要访问的页面!'

@route('/hello')
def hello():
	name = "wzzlj"
	myinfodir = {'age':27, 'weight':175, 'hight':181}
	blog = "http://wzzlj.github.io"
	myhome = "Wenzhou"
	return template('hello',name=name,age=myinfodir, weight=myinfodir,
					hight=myinfodir, blog=blog, myhome=myhome)

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


run(host='0.0.0.0', port=8000)	#开启服务，端口是8000，允许任何ip地址访问
