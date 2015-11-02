
# encoding:utf-8

from bottle import route,run,view

@route('/hello')
@view('hello')
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