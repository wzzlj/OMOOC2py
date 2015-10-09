#安装插件plugin和主题theme

一旦你发现你需要的插件`gitbook-plugin-Name`或主题`gitbook-theme-Name`，在 `book.json` 添加:
   
    {
      "plugins": ["Name"]
    }
    
- 对于 gitbook-plugin-Name 的插件，请这样安装 :

  `book-dir $ gitbook install`  或者   
   `npm install gitbook-plugin-Name`

- 对于 gitbook-theme-X 的插件，请这样安装 :

	    book-dir $ npm install gitbook-theme-Name && mv node_modules/gitbook-theme-Name node_modules/gitbook-plugin-Name
	
> PS : 具体插件请参照具体插件的文档