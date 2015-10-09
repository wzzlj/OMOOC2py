# 配置Gitbook

#### 为什么要使用Gitbook ？

>  由于 Github 本身的目录结构并不一定符合阅读的习惯，而且没有提供 pdf , ePUB, MOBI 等格式的转换下载。于是大家也还是习惯离线看文档。GitBook 就是解决这一问题。 GitBook 让你在保持在 Github 的书写习惯外，稍加配置，就能自动发布到GitBook 上，形成界面漂亮的电子书了（支持 html, pdf , ePUB, MOBI 等）。

## 注册gitbook和github并关联
## 安装gitbook环境
### 安装node环境 


### 通过npm安装gitbook

安装前，需要注意的是Mac需要获取root权限  
`sudo －s` 

> 接下来，网上找到的gitbook教程貌似有点过时了

如果我通过执行   
`npm install gitbook -g`
  
安装完后执行  
`gitbook`

会显示：

```
You need to install 'gitbook-cli' to have access to the gitbook command anywhere on your system.   
If you've installed this package globally, you need to uninstall it.  
Run 'npm uninstall -g gitbook' then 'npm install -g gitbook-cli'
```
所以我们其实是安装gitbook-cli  
如果之前安装了gitbook的话，记得先执行  
`npm uninstall -g gitbook`

而后执行  
`npm install gitbook-cli -g`  

如果执行  
`gitbook -V`

会显示  
`0.3.6`

如果执行  
`gitbook version`

显示      	
	 
```
GitBook Versions Installed:
     2.4.2
``` 

至此，gitbook环境安装成功！




## SUMMARY.md
## 编译、运行和发布

@wzzlj 9.30开坑