---
title: "【Raspberry PI 学习 II】树莓派如何安装软件和中文"
date: 2014-05-24
tags:
  - "Raspberry PI"
  - "学习"
  - "树莓派"
---

<span style="background-color: white; color: #444444; font-family: inherit; font-size: 14px; line-height: 21px; word-wrap: break-word;"><b>上回已经安装过VNCserver</b></span><br />
<span style="color: #444444; font-family: inherit;"><span style="background-color: white; font-size: 14px; line-height: 21px;"><b>我大概也猜到了以下command 就是安装软件用的</b></span></span><br />
<span style="color: #444444; font-family: inherit;"><span style="background-color: white; font-size: 14px; line-height: 21px;"><b>sudo apt-get install</b></span></span><br />
<span style="color: #444444;"><span style="background-color: white; font-size: 14px; line-height: 21px;"><b>下面两个例子也是以</b></span></span><b style="color: #444444; font-size: 14px; line-height: 21px;">sudo apt-get install 作为安装</b><br />
<br />
<span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; font-weight: 700; line-height: 21px; word-wrap: break-word;"><br /></span>
<span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; font-weight: 700; line-height: 21px; word-wrap: break-word;">下面我找的教程主要是安装软件的方法</span><br />
<span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; font-weight: 700; line-height: 21px; word-wrap: break-word;">1。显示中文和中文输入法,</span><br />
<span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; font-weight: 700; line-height: 21px; word-wrap: break-word;">2. 安装 google Chrome</span><br />
<span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; font-weight: 700; line-height: 21px; word-wrap: break-word;"><br /></span>

<span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; font-weight: 700; line-height: 21px; word-wrap: break-word;">1. Q:如何让树莓派显示中文？</span><br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixKbermeMPRV69HFVSF0lRATiyd2z1byEB3kHemYF5uoeS1P_IbJ4dcEQ-YDVgBl5i2Sssl4WtkoDYLA7Mn1bxrwgR0DybISPAapAjQuXcWcj-U0MgDv2IS75SP33dSI2MixSKHwC2zjc/s1600/111.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixKbermeMPRV69HFVSF0lRATiyd2z1byEB3kHemYF5uoeS1P_IbJ4dcEQ-YDVgBl5i2Sssl4WtkoDYLA7Mn1bxrwgR0DybISPAapAjQuXcWcj-U0MgDv2IS75SP33dSI2MixSKHwC2zjc/s1600/111.JPG" height="490" width="640" /></a></div>
<ignore_js_op style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px; text-align: -webkit-center; word-wrap: break-word;">&nbsp;</ignore_js_op><span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px; text-align: -webkit-center;">&nbsp;&nbsp;</span><br />
<ignore_js_op style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px; text-align: -webkit-center; word-wrap: break-word;"></ignore_js_op><br />
<a name='more'></a><br />
<span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">&nbsp; &nbsp; A:树莓派默认是采用英文字库的，而且系统里没有预装中文字库，所以即使你在locale中改成中文，也不会显示中文，只会显示一堆方块。因此需要我们手动来安装中文字体。好在有一个中文字体是免费开源使用的。ssh中输入以下命令</span><br />
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://www.eeboard.com/bbs/static/image/common/codebg.gif); background-position: 0px 0px; background-repeat: no-repeat repeat; border: 1px solid rgb(204, 204, 204); color: #666666; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; word-wrap: break-word; zoom: 1;">
<div id="code_llT" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-family: Monaco, Consolas, 'Lucida Console', 'Courier New', serif; font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;">sudo apt-get install ttf-wqy-zenhei</li>
</ol>
</div>
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-size: 12px; margin-left: 43px; word-wrap: break-word;">复制代码</span></div>
<span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">安装过程中如果碰到(Y/n)，都选择y</span><br />
<span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">中文字库安装完成之后，还需要安装一个中文输入法。输入如下命令</span><br />
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://www.eeboard.com/bbs/static/image/common/codebg.gif); background-position: 0px 0px; background-repeat: no-repeat repeat; border: 1px solid rgb(204, 204, 204); color: #666666; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; word-wrap: break-word; zoom: 1;">
<div id="code_9Mk" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-family: Monaco, Consolas, 'Lucida Console', 'Courier New', serif; font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;">sudo apt-get install scim-pinyin</li>
</ol>
</div>
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-size: 12px; margin-left: 43px; word-wrap: break-word;">复制代码</span></div>
<span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">一样的安装过程</span><br />
<span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">_____________</span><br />
<span style="background-color: white; color: #444444; font-family: Tahoma, Microsoft Yahei, Simsun; font-size: 14px; line-height: 21px;">(如果平时需要用中文系统的话 那就看这段吧 一</span><br />
<span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">选择change_locale，在Default locale for the system environment:中选择zh_CN.UTF-8,配置完成之后，输入命令</span><br />
<span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">_____________</span><br />
<span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; line-height: 21px;">安装完毕后</span><span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; line-height: 21px;">然输入 sudo raspi-config 后选择change_locale，在Default locale for the system environment:中选择zh_CN.UTF-8,配置完成之后，输入命令</span><br />
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://www.eeboard.com/bbs/static/image/common/codebg.gif); background-position: 0px 0px; background-repeat: no-repeat repeat; border: 1px solid rgb(204, 204, 204); color: #666666; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; word-wrap: break-word; zoom: 1;">
<div id="code_K15" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-family: Monaco, Consolas, 'Lucida Console', 'Courier New', serif; font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;">sudo raspi-config</li>
</ol>
</div>
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-size: 12px; margin-left: 43px; word-wrap: break-word;">复制代码</span><br />
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-size: 12px; margin-left: 43px; word-wrap: break-word;"><br /></span></div>
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://www.eeboard.com/bbs/static/image/common/codebg.gif); background-position: 0px 0px; background-repeat: no-repeat repeat; border: 1px solid rgb(204, 204, 204); color: #666666; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; word-wrap: break-word; zoom: 1;">
<div id="code_6RZ" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-family: Monaco, Consolas, 'Lucida Console', 'Courier New', serif; font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;">sudo reboot</li>
</ol>
</div>
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-size: 12px; margin-left: 43px; word-wrap: break-word;">复制代码</span></div>
<span style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">重启完成好就可以在VNC连接上去后使用中文显示和中文输入法了，切换中文输入法一样也是ctrl+space</span><br />
<br />
<div align="center" style="background-color: white; color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; line-height: 21px; word-wrap: break-word;">
<div style="font-size: 14px;">
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUxxqsCvbCPcO8Y3mMsI20Ac2sC1xVMA9dNdrXefV5Gd_AIOna7zbvDQi_Aiy6nI8R1uAFtWjBb-_TKqev0PTKlqCF2CjU-xeqDfXWSKOhEchP5_ekQzYMjbEhIVoPKW0kzypgmRJtQNM/s1600/111.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUxxqsCvbCPcO8Y3mMsI20Ac2sC1xVMA9dNdrXefV5Gd_AIOna7zbvDQi_Aiy6nI8R1uAFtWjBb-_TKqev0PTKlqCF2CjU-xeqDfXWSKOhEchP5_ekQzYMjbEhIVoPKW0kzypgmRJtQNM/s1600/111.JPG" height="490" width="640" /></a></div>
<br /></div>
<div style="font-size: 14px;">
<ignore_js_op style="word-wrap: break-word;"><br /></ignore_js_op>
</div>
<div style="font-size: 14px;">
<ignore_js_op style="word-wrap: break-word;"><br /></ignore_js_op></div>
<div style="color: black; font-family: 'Times New Roman'; line-height: normal; text-align: start;">
<span style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-weight: 700; line-height: 21px; word-wrap: break-word;">2. Q:如何在树莓派上安装谷歌的开源浏览器<span style="font-family: Tahoma, Helvetica, SimSun, sans-serif; word-wrap: break-word;">Chromium?</span></span></div>
<div style="color: black; font-family: 'Times New Roman'; font-size: medium; line-height: normal; text-align: start;">
<span style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">&nbsp; &nbsp; A:连接ssh,输入如下命令&nbsp;</span></div>
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://www.eeboard.com/bbs/static/image/common/codebg.gif); background-position: 0px 0px; border: 1px solid rgb(204, 204, 204); color: #666666; font-size: 14px; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; text-align: start; word-wrap: break-word; zoom: 1;">
<div id="code_PpR" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-family: Monaco, Consolas, 'Lucida Console', 'Courier New', serif; font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;">sudo apt-get install chromium-browser</li>
</ol>
</div>
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-size: 12px; margin-left: 43px; word-wrap: break-word;">复制代码</span></div>
<div style="color: black; font-family: 'Times New Roman'; font-size: medium; line-height: normal; text-align: start;">
<span style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">（</span><span style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">注意 那个是 L10 不是110 我自己就犯过这个错误）</span><br />
<span style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">提示是否安装，输入y,等待安装完成</span></div>
<div style="color: black; font-family: 'Times New Roman'; font-size: medium; line-height: normal; text-align: start;">
<span style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">完成之后，进入桌面 选择菜单-〉互联网-〉Chromium网页浏览器，就可以打开熟悉的chrome浏览器了</span></div>
<div align="center" style="font-size: 14px; word-wrap: break-word;">
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeASIePnFAkI22prLHFK_E_35qf5gQjsZndQDa0-6mnrd9tqSOergdMUuLIi12-VUDd0h65qgN8NQQYVh1o1WrxRvjtlUpI760IU56AaLwvy91cdcUEoOlWVImXEwH_cN52vKkblw53S8/s1600/Capture.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeASIePnFAkI22prLHFK_E_35qf5gQjsZndQDa0-6mnrd9tqSOergdMUuLIi12-VUDd0h65qgN8NQQYVh1o1WrxRvjtlUpI760IU56AaLwvy91cdcUEoOlWVImXEwH_cN52vKkblw53S8/s1600/Capture.JPG" height="490" width="640" /></a></div>
<br /></div>
<div style="color: black; font-family: 'Times New Roman'; font-size: medium; line-height: normal; text-align: start;">
<br style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px; word-wrap: break-word;" /></div>
<div style="color: black; font-family: 'Times New Roman'; font-size: medium; line-height: normal; text-align: start;">
<br style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px; word-wrap: break-word;" /></div>
<div style="color: black; font-family: 'Times New Roman'; font-size: medium; line-height: normal; text-align: start;">
<span style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">还有一种方式，是在系统发行版软件库里没有chrome的时候来安装chrome浏览器的</span></div>
<div style="color: black; font-family: 'Times New Roman'; font-size: medium; line-height: normal; text-align: start;">
<span style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">打开ssh，输入如下命令</span></div>
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://www.eeboard.com/bbs/static/image/common/codebg.gif); background-position: 0px 0px; border: 1px solid rgb(204, 204, 204); color: #666666; font-size: 14px; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; text-align: start; word-wrap: break-word; zoom: 1;">
<div id="code_84O" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-family: Monaco, Consolas, 'Lucida Console', 'Courier New', serif; font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;">wget http://goo.gl/go5yx -O install.sh</li>
</ol>
</div>
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-size: 12px; margin-left: 43px; word-wrap: break-word;">复制代码</span></div>
<div style="color: black; font-family: 'Times New Roman'; font-size: medium; line-height: normal; text-align: start;">
<span style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">成功后，打入：</span></div>
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://www.eeboard.com/bbs/static/image/common/codebg.gif); background-position: 0px 0px; border: 1px solid rgb(204, 204, 204); color: #666666; font-size: 14px; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; text-align: start; word-wrap: break-word; zoom: 1;">
<div id="code_3yz" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-family: Monaco, Consolas, 'Lucida Console', 'Courier New', serif; font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;">chmod a+x install.sh</li>
</ol>
</div>
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-size: 12px; margin-left: 43px; word-wrap: break-word;">复制代码</span></div>
<div style="color: black; font-family: 'Times New Roman'; font-size: medium; line-height: normal; text-align: start;">
<span style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">然后，输入（注意一定要加上前面的”点斜杆”）：</span></div>
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://www.eeboard.com/bbs/static/image/common/codebg.gif); background-position: 0px 0px; border: 1px solid rgb(204, 204, 204); color: #666666; font-size: 14px; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; text-align: start; word-wrap: break-word; zoom: 1;">
<div id="code_WKt" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-family: Monaco, Consolas, 'Lucida Console', 'Courier New', serif; font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;">./install.sh</li>
</ol>
</div>
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-size: 12px; margin-left: 43px; word-wrap: break-word;">复制代码</span></div>
<div style="color: black; font-family: 'Times New Roman'; font-size: medium; line-height: normal; text-align: start;">
<span style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">就开始下载和安装一些必要的包，还有下载整个Chrome并安装，整个过程速度飞快。</span></div>
<div style="color: black; font-family: 'Times New Roman'; font-size: medium; line-height: normal; text-align: start;">
<span style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">这个方式参考了这个链接里的教程http://www.leiphone.com/raspberry-pi-hands-on.html</span></div>
<div style="color: black; font-family: 'Times New Roman'; font-size: medium; line-height: normal; text-align: start;">
<span style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">不过这种安装方式在菜单里就没有选项可以让你点了，VNC连接后，在中端里输入</span></div>
<div class="blockcode" style="background-color: #f7f7f7; background-image: url(http://www.eeboard.com/bbs/static/image/common/codebg.gif); background-position: 0px 0px; border: 1px solid rgb(204, 204, 204); color: #666666; font-size: 14px; margin: 10px 0px; overflow: hidden; padding: 10px 0px 5px 10px; text-align: start; word-wrap: break-word; zoom: 1;">
<div id="code_uRL" style="word-wrap: break-word;">
<ol style="margin: 0px 0px 0px 10px !important; padding: 0px !important; word-wrap: break-word;">
<li style="font-family: Monaco, Consolas, 'Lucida Console', 'Courier New', serif; font-size: 12px; line-height: 1.8em; list-style-type: decimal-leading-zero; margin: 0px 0px 0px 2em; padding: 0px 0px 0px 10px; word-wrap: break-word;">chrome -disable-ipv6 &amp;</li>
</ol>
</div>
<span style="color: rgb(51, 102, 153) !important; cursor: pointer; font-size: 12px; margin-left: 43px; word-wrap: break-word;">复制代码</span></div>
<div style="font-size: 14px;">
<ignore_js_op style="word-wrap: break-word;"></ignore_js_op><br /></div>
<div style="color: black; font-family: 'Times New Roman'; font-size: medium; line-height: normal; text-align: start;">
<span style="color: #444444; font-family: Tahoma, 'Microsoft Yahei', Simsun; font-size: 14px; line-height: 21px;">就可以启动浏览器了</span></div>
<div style="color: black; font-family: 'Times New Roman'; font-size: medium; line-height: normal; text-align: start;">
<br /></div>
</div>
