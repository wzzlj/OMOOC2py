# encoding:utf-8

from bottle import run,get,post,request

@get('/login')		#或者@route('/login')，默认是GET方法
def login_form():
	return '''
	<form method="POST"action="/login">
	用户名：<input name="username" type="text"/><br>
	  密码：<input name="password" type="password"/><br>
	<input value="登录" type="submit"/>
	</form>'''

@post('/login')		#或者@route('/login',method='POST')
def login_submit():
	name = request.forms.get('username')
	passwd = request.forms.get('password')
	return "<p>用户名: %s</p><p>密码: %s</p>" % (name, passwd)

run(host='0.0.0.0', port=8000, debug=True)