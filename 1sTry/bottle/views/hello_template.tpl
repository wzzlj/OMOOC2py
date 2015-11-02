
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