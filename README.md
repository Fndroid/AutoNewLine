## 简介
一个**SublineText3**的插件，主要作用是结束当前行，直接进入下一行，作用类似于IntellijIDEA的next line。

简单来说就是在行末添加**一个分号**，并且**换行**

## 使用
### 下载

在Releases页面下载后，重命名文件夹为**AutoNewLine**

### 安装

打开**SublineText3->Preferences->Browse Packages**，将下载的文件夹复制进去即可。

### 设置

在任意文件中按下**右键**，选择**自动换行**，即可看到设置界面。

某些代码文件是不带分号的，可以在设置中设置后缀，遇到此类文件只会换行，默认为：**"py", "html", "wxml", "js", "json"**，有需要自行添加即可。

快捷键默认为**alt+m**。

## BUG

1.快捷键暂时只适配了Windows的，其他两个平台，可以自己设置一下（。。。偷懒）。

2.关于中括号：
```java
// 对如下写法不友好：
While(true)
{
  xxx
}

// 而采用
While(true){
  xxx
}
```
