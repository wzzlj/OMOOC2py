# virtualenv的使用和安装

**virtualenv** 用于创建独立的Python环境，多个Python相互独立，互不影响，它能够：

1. 在没有权限的情况下安装新套件
2. 不同应用可以使用不同的套件版本
3. 套件升级不影响其他应用

## 安装

使用如下命令进行安装：

`sudo easy_install virtualenv`

或者更好的

`sudo pip install virtualenv`

## 使用方法

1. 创建一个虚拟环境

`virtualenv [虚拟环境名称]`

例如 `virtualenv flask`

默认情况下，虚拟环境会依赖系统环境中的site packages，就是说系统中已经安装好的第三方package也会安装在虚拟环境中，如果不想依赖这些package，那么可以加上参数 --no-site-packages建立虚拟环境

`virtualenv --no-site-packages [虚拟环境名称]`

2. 启动虚拟环境

```
cd [虚拟环境名称]
source ./bin/activate
```

此时命令行会多出一个 `([虚拟环境名称])` ，接下来所有模块都只会安装到该目录去

3. 退出虚拟环境

`deactivate`

4. 在虚拟环境安装 Python 套件

virtualenv 附带有 pip 安装工具，因此需要安装的套件可以直接运行：

`pip install [套件名称]`

如果没有启动虚拟环境，系统也安装了pip工具，那么套件将被安装在系统环境中，为了避免发生此事，可以在 **~/.zshrc** 文件中加上：

`export PIP_REQUIRE_VIRTUALENV=true`

或者让在执行 pip 的时候让系统自动开启虚拟环境：

`export PIP_RESPECT_VIRTUALENV=true`

## 安装 Flask

在 virtualenv 环境中输入以下的命令来激活 flask：

`pip install flask`

或者考虑全局安装，尽管官方文档不太推荐：

`sudo pip install flask`	