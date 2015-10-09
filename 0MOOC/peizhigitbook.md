# 配置Gitbook

## 为什么要使用Gitbook ？

>  由于 Github 本身的目录结构并不一定符合阅读的习惯，而且没有提供 pdf , ePUB, MOBI 等格式的转换下载。于是大家也还是习惯离线看文档。GitBook 就是解决这一问题。 GitBook 让你在保持在 Github 的书写习惯外，稍加配置，就能自动发布到GitBook 上，形成界面漂亮的电子书了（支持 html, pdf , ePUB, MOBI 等）。

## 安装gitbook环境
首先安裝好：   

- [Node](https://nodejs.org/en/)  
- npm(安装完Node后就有了)   
 

### 通过npm安装gitbook

1. 安装前，需要注意的是Mac需要获取root权限  
`sudo －s` 

2. 安装gitbook-cli  
   如果之前安装了旧版gitbook并出现错误信息的话，记得先执行  
   `npm uninstall -g gitbook`

   而后执行  
   `npm install gitbook-cli -g`  
   
   等待转圈圈一会儿～

3. 安装完后执行  
   `gitbook -V`(区分大小写～)

   会显示  
   `0.3.6`

   如果执行  
   `gitbook versions`

   显示      	
	 
   ```
   GitBook Versions Installed:
        2.4.2
   ``` 

**至此，gitbook环境安装成功！撒花～**

![image](http://7xn3v1.com1.z0.glb.clouddn.com/15-10-9/73107951.jpg)



```
9.30开坑  
10.09更新
```

参考[Gitbook中文解说](https://wastemobile.gitbooks.io/gitbook-chinese/content/)