# encoding=utf-8

from bottle import route,run,view,static_file,template,request

@route('/download/<filename:path>')
def download(filename):
	return static_file(filename,root='./static/',
						download=True)

@route('/hello')
def hello():
	return template('hello')

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

run(host='0.0.0.0',port=8000,debug=True)
