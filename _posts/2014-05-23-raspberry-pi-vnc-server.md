---
title: "【学习】树莓派 Raspberry Pi开机启动 VNC server "
date: 2014-05-23
tags:
  - "Raspberry PI"
  - "学习"
  - "树莓派"
---

<span style="background-color: white;"><span style="font-family: inherit; line-height: 21px;">给我一个家里没电视 又没电脑屏幕的我</span></span><br />
<span style="background-color: white;"><span style="font-family: inherit; line-height: 21px;">即使购买的时候给了我一条不错的hdmi cable 和vga converter 也是没用...</span></span><br />
<span style="font-family: inherit;">SSH 和 VNC 远程遥控的方式成为了我操控树莓的常用途径，</span><br />
<span style="font-family: inherit;">为了不每次都链接 SSH 来打开vnc server 的遥控页面</span><br />
<span style="font-family: inherit;">根据我自己脑中的观念</span><br />
<span style="font-family: inherit;">特地找了个教程给我自己学习</span><br />
<span style="font-family: inherit;"><br />
这次要达到的是</span><br />
<span style="font-family: inherit;">开机自动启动VNC server</span><br />
<span style="background-color: white;"><span style="font-family: inherit; line-height: 21px;">请注意 在这之前必须设置了<b>自动登入和启动startx&nbsp;</b><br />否则即使自动启动VNCserver&nbsp;</span></span><br />
<span style="background-color: white;"><span style="font-family: inherit; line-height: 21px;">还是没办法直接进入遥控界面的。</span></span><br />
<span style="background-color: white; color: #444444; font-family: inherit;"><span style="font-size: 14px; line-height: 21px;"></span></span><br />
<a name='more'></a><span style="background-color: white; color: #444444; font-family: inherit;"><span style="font-size: 14px; line-height: 21px;"><br />以下教程原文转自&nbsp;<a href="http://bbs.shumeipai.org/thread-113-1-1.html">树莓爱好者论坛</a></span><br /><span style="font-size: 14px; line-height: 21px;">安装VNC需要使用命令行。如果需要远程操作安装VNC，就必须通过SSH登录到命令行界面。</span></span><br />
<span style="font-family: inherit;"><br />
<span style="background-color: white; color: #444444; font-size: large; word-wrap: break-word;"><span style="font-weight: 700; word-wrap: break-word;">安装</span></span></span><br />
<span style="background-color: white; color: #444444; font-family: inherit; font-size: 14px; line-height: 21px;">树莓派命令行：</span><br />
<span style="font-family: inherit;"><span style="background-color: white; color: #444444; font-size: 14px; line-height: 21px;"></span><br /></span>
<br />
<span style="background-color: white; color: #444444; font-family: inherit; font-size: 14px; line-height: 21px;"><br /></span>
<br />
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://rbstatic.shamiao.com/image/common/codebg.gif); background-position: 0px 0px; background-repeat: no-repeat repeat; border: 1px solid rgb(204, 204, 204); color: #666666; font-size: 14px; line-height: 21px; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; word-wrap: break-word; zoom: 1;">
<div id="code_GIM" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;"><span style="font-family: inherit;">sudo apt-get install tightvncserver</span></li>
</ol>
</div>
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-family: inherit; font-size: 12px; margin-left: 43px; word-wrap: break-word;">复制代码</span></div>
<hr class="l" style="background-color: #cdcdcd; border: none; clear: both; color: #cdcdcd; font-size: 14px; height: 1px; line-height: 21px; word-wrap: break-word;" />
<span style="font-family: inherit;"><br />
<span style="background-color: white; color: #444444; font-size: large; word-wrap: break-word;"><span style="font-weight: 700; word-wrap: break-word;">开机自动启动</span></span></span><br />
<span style="background-color: white; color: #444444; font-family: inherit; font-size: 14px; line-height: 21px;">安装好之后请一定先使用此命令设置一个VNC密码：</span><br />
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://rbstatic.shamiao.com/image/common/codebg.gif); background-position: 0px 0px; background-repeat: no-repeat repeat; border: 1px solid rgb(204, 204, 204); color: #666666; font-size: 14px; line-height: 21px; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; word-wrap: break-word; zoom: 1;">
<div id="code_f61" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;"><span style="font-family: inherit;">vncpasswd</span></li>
</ol>
</div>
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-family: inherit; font-size: 12px; margin-left: 43px; word-wrap: break-word;">复制代码</span></div>
<span style="background-color: white; color: #444444; font-family: inherit; font-size: 14px; line-height: 21px;">（先输入操作密码两次，然后会询问是否设置一个查看(view-only)密码，按自己喜欢，一般没必要。）</span><br />
<span style="font-family: inherit;"><br style="background-color: white; color: #444444; font-size: 14px; line-height: 21px; word-wrap: break-word;" />
<span style="background-color: white; color: #444444; font-size: 14px; line-height: 21px;">设置开机启动，需要在/etc/init.d/中创建一个文件。例如tightvncserver：</span></span><br />
<span style="background-color: white; color: #444444; font-family: inherit; font-size: 14px; line-height: 21px;">（注：启动脚本的名称，有和程序名一致的习惯）</span><br />
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://rbstatic.shamiao.com/image/common/codebg.gif); background-position: 0px 0px; background-repeat: no-repeat repeat; border: 1px solid rgb(204, 204, 204); color: #666666; font-size: 14px; line-height: 21px; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; word-wrap: break-word; zoom: 1;">
<div id="code_pcJ" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;"><span style="font-family: inherit;">sudo nano /etc/init.d/tightvncserver</span></li>
</ol>
</div>
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-family: inherit; font-size: 12px; margin-left: 43px; word-wrap: break-word;">复制代码</span></div>
<span style="background-color: white; color: #444444; font-family: inherit; font-size: 14px; line-height: 21px;">内容如下：（putty窗口中按右键=粘贴）</span><br />
<div class="quote" style="background-color: #f9f9f9; background-image: url(http://rbstatic.shamiao.com/image/common/icon_quote_s.gif); background-position: 20px 6px; background-repeat: no-repeat no-repeat; color: #666666; font-size: 14px; line-height: 21px; margin: 10px 0px; overflow: hidden; padding: 10px 10px 5px 65px; word-wrap: break-word; zoom: 1;">
<blockquote style="background-image: url(http://rbstatic.shamiao.com/image/common/icon_quote_e.gif); background-position: 100% 100%; background-repeat: no-repeat no-repeat; display: inline-block; line-height: 1.6; margin: 0px; padding: 0px 65px 5px 0px; word-wrap: break-word; zoom: 1;">
<span style="font-family: inherit; word-wrap: break-word;">#!/bin/sh<br style="word-wrap: break-word;" />### BEGIN INIT INFO<br style="word-wrap: break-word;" /># Provides:&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; tightvncserver<br style="word-wrap: break-word;" /># Required-Start:&nbsp; &nbsp; $local_fs<br style="word-wrap: break-word;" /># Required-Stop:&nbsp; &nbsp;&nbsp;&nbsp;$local_fs<br style="word-wrap: break-word;" /># Default-Start:&nbsp; &nbsp;&nbsp;&nbsp;2 3 4 5<br style="word-wrap: break-word;" /># Default-Stop:&nbsp; &nbsp;&nbsp; &nbsp;0 1 6<br style="word-wrap: break-word;" /># Short-Description: Start/stop tightvncserver<br style="word-wrap: break-word;" />### END INIT INFO<br style="word-wrap: break-word;" /><br style="word-wrap: break-word;" /># More details see:<br style="word-wrap: break-word;" />#&nbsp;<a href="http://www.penguintutor.com/linux/tightvnc" style="color: #336699; word-wrap: break-word;" target="_blank">http://www.penguintutor.com/linux/tightvnc</a><br style="word-wrap: break-word;" /><br style="word-wrap: break-word;" />### Customize this entry<br style="word-wrap: break-word;" /># Set the USER variable to the name of the user to start tightvncserver under<br style="word-wrap: break-word;" />export USER='pi'<br style="word-wrap: break-word;" />### End customization required<br style="word-wrap: break-word;" /><br style="word-wrap: break-word;" />eval cd ~$USER<br style="word-wrap: break-word;" /><br style="word-wrap: break-word;" />case "$1" in<br style="word-wrap: break-word;" />&nbsp;&nbsp;start)<br style="word-wrap: break-word;" />&nbsp; &nbsp; # 启动命令行。此处自定义分辨率<span style="font-size: x-small; word-wrap: break-word;">、控制台<span style="font-size: x-small; word-wrap: break-word;">号码或其它参数</span></span>。<br style="word-wrap: break-word;" />&nbsp; &nbsp; su $USER -c '/usr/bin/tightvncserver -depth 16 -geometry 800x600 :1'<br style="word-wrap: break-word;" />&nbsp; &nbsp; echo "Starting TightVNC server for $USER "<br style="word-wrap: break-word;" />&nbsp; &nbsp; ;;<br style="word-wrap: break-word;" />&nbsp;&nbsp;stop)<br style="word-wrap: break-word;" />&nbsp; &nbsp; # 终止命令行。此处控制台号码与启动一致。<br style="word-wrap: break-word;" />&nbsp; &nbsp; su $USER -c '/usr/bin/tightvncserver -kill :1'<br style="word-wrap: break-word;" />&nbsp; &nbsp; echo "Tightvncserver stopped"<br style="word-wrap: break-word;" />&nbsp; &nbsp; ;;<br style="word-wrap: break-word;" />&nbsp;&nbsp;*)<br style="word-wrap: break-word;" />&nbsp; &nbsp; echo "Usage: /etc/init.d/tightvncserver {start|stop}"<br style="word-wrap: break-word;" />&nbsp; &nbsp; exit 1<br style="word-wrap: break-word;" />&nbsp; &nbsp; ;;<br style="word-wrap: break-word;" />esac<br style="word-wrap: break-word;" />exit 0</span></blockquote>
</div>
<span style="font-family: inherit;"><br style="background-color: white; color: #444444; font-size: 14px; line-height: 21px; word-wrap: break-word;" />
<span style="background-color: white; color: #444444; font-size: 14px; line-height: 21px;">注：</span><span style="background-color: white; color: #444444; font-size: 14px; line-height: 21px; word-wrap: break-word;">少数朋友默认用户不是pi的请自行更改</span><span style="background-color: white; color: #444444; font-size: 14px; line-height: 21px;">USER变量</span></span><br />
<span style="background-color: white; color: #444444; font-family: inherit; font-size: 14px; line-height: 21px;">按Ctrl+X，回答Y（存盘）退出nano编辑器。</span><br />
<span style="background-color: white; color: #444444; font-family: inherit; font-size: 14px; line-height: 21px;">然后给tightvncserver文件加执行权限，并更新开机启动列表。</span><br />
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://rbstatic.shamiao.com/image/common/codebg.gif); background-position: 0px 0px; background-repeat: no-repeat repeat; border: 1px solid rgb(204, 204, 204); color: #666666; font-size: 14px; line-height: 21px; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; word-wrap: break-word; zoom: 1;">
<div id="code_UmU" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;"><span style="font-family: inherit;">sudo chmod 755 /etc/init.d/tightvncserver</span></li>
<li style="font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;"><span style="font-family: inherit;">sudo update-rc.d tightvncserver defaults</span></li>
<li style="font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;"></li>
</ol>
</div>
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-family: inherit; font-size: 12px; margin-left: 43px; word-wrap: break-word;">复制代码</span></div>
<span style="font-family: inherit;"><br />
<span style="background-color: #f9f9f9; color: #666666; font-size: large; font-weight: 700; line-height: 38.400001525878906px; word-wrap: break-word;">手工启动与参数</span></span><br />
<span style="background-color: #f9f9f9; color: #666666; font-family: inherit; font-size: large; font-weight: 700; line-height: 38.400001525878906px; word-wrap: break-word;"><span style="font-size: x-small; font-weight: normal; word-wrap: break-word;">以下用处不大，没兴趣<span style="font-size: x-small; word-wrap: break-word;">请略</span>过。</span><br style="font-size: 14px; font-weight: normal; line-height: 22.399999618530273px; word-wrap: break-word;" /><span style="font-size: x-small; font-weight: normal; word-wrap: break-word;">使用此命令手工启动VNC服务器程序：</span></span><br />
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://rbstatic.shamiao.com/image/common/codebg.gif); background-position: 0px 0px; background-repeat: no-repeat repeat; border: 1px solid rgb(204, 204, 204); color: #666666; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; word-wrap: break-word; zoom: 1;">
<div id="code_Fz9" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;"><span style="font-family: inherit;">tightvncserver -geometry 800x600 :1</span></li>
</ol>
</div>
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-family: inherit; font-size: 12px; margin-left: 43px; word-wrap: break-word;">复制代码</span></div>
<span style="background-color: #f9f9f9; color: #666666; font-weight: 700; line-height: 38.400001525878906px; word-wrap: break-word;"><span style="font-family: inherit; font-weight: normal; word-wrap: break-word;">如果首次启动，并且未曾使用vncpasswd命令设置密码，程序会要求设置一个。<br style="word-wrap: break-word;" /><br style="word-wrap: break-word;" />开机启动很方便。如果没理由，真的不推荐手工启动。<br style="word-wrap: break-word;" /><br style="word-wrap: break-word;" />命令行参数说明：<br style="word-wrap: break-word;" />一、:1，指定控制台的号码。<br style="word-wrap: break-word;" />启动多个控制台，可以提供互不影响的多个桌面环境。（大多数人不用多用户操作所以没意义）<br style="word-wrap: break-word;" />可以不加此参数，tightvncserver会自动寻找从1开始的下一个空闲控制台。<br style="word-wrap: break-word;" />加上此参数，会强制使用指定的控制台，如果此控制台已经启动则报错。加此参数可有效防止无意多次启动程序（会启动多个控制台）白白浪费系统资源。<br style="word-wrap: break-word;" /><br style="word-wrap: break-word;" /><span style="color: red; font-size: large; word-wrap: break-word;"><span style="font-weight: 700; word-wrap: break-word;">特殊的0号控制台</span><br style="word-wrap: break-word;" />0号控制台就是连接真实显示器真正输出图像的那个桌面。<br style="word-wrap: break-word;" />对于VNC客户端，不输入端口号登录，默认就登录到0号控制台，方便。<br style="word-wrap: break-word;" />但是因为0号是真正的桌面，所以和开机启动桌面环境，或者自己用startx命令，都存在啰嗦的冲突。<br style="word-wrap: break-word;" />到头来是个麻烦。因此自动启动的配置教程中，一律使用1号控制台。</span><br style="word-wrap: break-word;" /><br style="word-wrap: break-word;" /><span style="font-size: large;">二、-geometry 800x600，分辨率。可以不加。</span><br style="word-wrap: break-word;" /><br style="word-wrap: break-word;" /><span style="font-size: large;">终止VNC控制台：</span></span></span><br />
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://rbstatic.shamiao.com/image/common/codebg.gif); background-position: 0px 0px; background-repeat: no-repeat repeat; border: 1px solid rgb(204, 204, 204); color: #666666; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; word-wrap: break-word; zoom: 1;">
<div id="code_w14" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;"><span style="font-family: inherit;">tightvncserver -kill :1</span></li>
</ol>
</div>
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-family: inherit; font-size: 12px; margin-left: 43px; word-wrap: break-word;">复制代码</span></div>
<span style="background-color: #f9f9f9; color: #666666; font-size: large; font-weight: 700; line-height: 38.400001525878906px; word-wrap: break-word;"><span style="font-family: inherit; font-size: x-small; font-weight: normal; word-wrap: break-word;">查看正在运行的控制台列表：</span></span><br />
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://rbstatic.shamiao.com/image/common/codebg.gif); background-position: 0px 0px; background-repeat: no-repeat repeat; border: 1px solid rgb(204, 204, 204); color: #666666; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; word-wrap: break-word; zoom: 1;">
<div id="code_toF" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;"><span style="font-family: inherit;">ps ax | grep Xtightvnc | grep -v grep</span></li>
</ol>
</div>
<em style="color: rgb(51, 102, 153) !important; cursor: pointer; font-size: 12px; font-style: normal; margin-left: 43px; word-wrap: break-word;"><span style="font-family: inherit;">复制代码</span></em></div>
