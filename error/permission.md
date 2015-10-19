# commit 的时候出现 permission 错误
````
error: insufficient permission for adding an object to repository database .git/objects  
error: insufficient permission for adding an object to repository database .git/objects  
error: Error building trees
````
- 问题出现时间：2015年10月11日
- 问题描述
	- 在 gitbook 的时候，移动了几个文件到新的文件夹下，重新优化了目录结构
	- 在 commit 的时候报错
	![](http://7xn3v1.com1.z0.glb.clouddn.com/15-10-11/73969181.jpg)

- 解决办法
	- 把错误信息直接输入 google 进行搜索。
	- 搜索结果大部分是在 push 中出现问题，要更改.git 的目录权限，不懂之。并且我是在 commit 的时候出的错啊。
	- 在一个搜索结果中发现一句话
	> 在linux下，一般error中出现permission 关键字的，均是权限不足造成的。
	- 改目录权限不会，但是切换用户权限我会啊！故 `sudo -s`
	- 重新 commit，然后 push，成功！ 	 

