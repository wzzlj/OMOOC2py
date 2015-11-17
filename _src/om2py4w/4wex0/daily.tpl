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