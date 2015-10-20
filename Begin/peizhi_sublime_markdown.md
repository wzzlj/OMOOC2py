# 确实是近乎完美的 markdown 写作体验
### ——Sublime Text 下 markdown 写作环境的配置

> 今天 macdown 的实时预览突然显示不了图片，一直找不到原因。  
之前被安利过 Sublime text 对 markdown 的写作怎么怎么好。
索性，直接换 Sublime text 吧。

安装后发现，Sublime text 上原生并不支持 Markdown 语法高亮以及实时预览。

故 google 之，找到几个不错的教程：

## 一、实现 Markdown 语法高亮的教程：[地址](http://frank19900731.github.io/blog/2015/04/13/zai-sublime-zhong-pei-zhi-markdown-huan-jing/)

- 1.安装 Package Control
	- 在 Sublime text 中使用 control+` 调出控制台
	- 输入如下代码，回车安装  

```
		import urllib.request,os,hashlib; h = 'eb2297e1a458f27d836c04bb0cbaf282' + 'd0e7a3098092775ccb37ca9d6b2e4b7d'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```
	
- 2.安装Monokai Extended & Markdown Extended	
	- Shift + Command + P 调出 Command Palette，输入 `pci`（模糊匹配），找到 `Package Control: Install Package`，回车;
	- 分别输入两个插件名称、回车，等待安装；
	- 点击 Sublime 右下角文档格式，在列表最上方名为 Open all with current extension as 二级列表中选择 Markdown Extended；
	- 在 Preferences——Color Scheme——Mononkai Extended 下选择一个皮肤，如图：
	![](http://7xn3v1.com1.z0.glb.clouddn.com/15-10-17/65551351.jpg)


- OK，效果如图：  
		![](http://7xn3v1.com1.z0.glb.clouddn.com/15-10-17/55073127.jpg)

## 二、实现实时预览的教程：[地址](http://macplay.leanote.com/post/%E8%BF%91%E4%B9%8E%E5%AE%8C%E7%BE%8E%E7%9A%84-Markdown-%E5%86%99%E4%BD%9C%E4%BD%93%E9%AA%8C-Sublime-Text-3-OmniMarkupPreviewer)

- Shift + Command + P 调出 Command Palette，输入 `pci`（模糊匹配），找到 `Package Control: Install Package`，回车;
- 找到`OmniMarkupPreviewer`，回车，安装；
- 在 markdown 文件中通过 `command+alt+o` 调出浏览器实时预览
- 通过修改OmniMarkupPreviewer插件配置文件，将第一行  
	 `"server_host": "127.0.0.1"`   
	修改为  
	` "server_host": "192.168.1.100"`  
	`192.168.1.100`是你本机局域网内的 IP 地址。

- 这样就可以实现同一局域网下 **不同设备** 的实时预览，比如在 ipad 中输入对应地址，效果炸裂！  
	![](http://7xn3v1.com1.z0.glb.clouddn.com/15-10-17/54643213.jpg)

- 通过最新的 Ei Capitan 的特性，还可以实现双屏实时预览~
	![](http://7xn3v1.com1.z0.glb.clouddn.com/15-10-17/30822344.jpg)