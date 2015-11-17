# encoding:utf-8

import dailyserver
from bottle import route, run, template, debug, request

@route('/daily')			#<---路由，默认为 GET
def daily():
    return template('daily', daily=open('daily.log','r').read())	#<---输入框

@route('/daily', method='POST')
def postdaily():
	d_add = request.forms.get('d_input')
	open('daily.log','a').write(d_add+'\n')		#<---写入到日记文件
	return template('daily', daily=open('daily.log','r').read())		#<---返回数据

dailyserver.main()

run(host='localhost', port=8080, debug=True, reloader=True)


