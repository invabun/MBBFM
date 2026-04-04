---
title: "【Raspberry PI 学习 III】把树莓派默认的自动分配IP 改为固定IP 以方便工作"
date: 2014-05-30
tags:
  - "Raspberry PI"
  - "学习"
  - "树莓派"
---

<span style="font-family: inherit;">之前弄好了基本内容</span><br />
<div>
<span style="font-family: inherit;">包括安装系统，安装VNC，杂七杂八软件</span></div>
<div>
<span style="font-family: inherit;">是时候面对现实往前迈进了</span></div>
<div>
<span style="font-family: inherit;">现在开始弄网络链接计划如此这般...</span></div>
<div>
<span style="font-family: inherit;"><br /></span></div>
<div>
<span style="font-family: inherit;">1 先让树莓派IP 变固定，树莓派默认是dhcp 自动分配的每次搜索实在太麻烦了</span></div>
<div>
<span style="font-family: inherit;">2 然后给树莓架上一个简单的网站</span></div>
<div>
<span style="font-family: inherit;">3 要让树莓派的网站确实透过网络能查看（这就是传说中的架站了吧）</span></div>
<div>
<span style="font-family: inherit;">4 ok以后估计就是最复杂的内容了，由于涉及工作暂时就不透露·</span></div>
<div>
<span style="font-family: inherit;"><br /></span></div>
<div>
<span style="font-family: inherit;">今天要看的教程就是如何链接和让树莓派IP变成静态...</span></div>
<div>
<a name='more'></a><span style="font-family: inherit;">链接方式可以有很多方法实现</span></div>
<div>
<span style="font-family: inherit;">我这里用的是 家里Wifi&gt;笔记本 &gt;Lan cable &gt;树莓派</span></div>
<div>
<span style="font-family: inherit;">联网后先在电脑做一下电脑搭桥的设置</span></div>
<div>
<span style="font-family: inherit;">目的是让电脑的wifi 能够透过lan share 到树莓派</span></div>
<div class="separator" style="clear: both; text-align: center;">
<span style="font-family: inherit;"><br /></span></div>
<div>
<span style="font-family: inherit;">这里以window8 为例(方法还有很多大家可以自行搜索)</span></div>
<div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="font-family: inherit;"><br /></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="font-family: inherit;">当有些情况下我们不想扫描ip那么可以考虑将树莓派的ip设为固定ip这样我们每次就能准确访问</span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="font-family: inherit;">而不需要扫描ip</span></div>
</div>
<div>
<span style="font-family: inherit;"><br /></span></div>
<div>
<span style="font-family: inherit;">1 先将树莓派和笔记本用网线接好 开机~ 你会看到电脑有显示链接了ethenet</span></div>
<div>
<span style="font-family: inherit;"><br /></span></div>
<div>
<span style="font-family: inherit;">2 滑鼠右键点桌面右下角的这个<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh43K7wNAZsUDRvy13A35cgxVT5R0GveMLULh2WW3t7qHcAq3XFZmBYRYP-Nkc5dCg-nBr6P_5X1bFBO4JmLmhz6l9vLVvBje9nQWvLqDCfvE7K-vYK5iL1mwh-A3KT4vxhDZlNVpC7r_c/s1600/1.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em; text-align: center;"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh43K7wNAZsUDRvy13A35cgxVT5R0GveMLULh2WW3t7qHcAq3XFZmBYRYP-Nkc5dCg-nBr6P_5X1bFBO4JmLmhz6l9vLVvBje9nQWvLqDCfvE7K-vYK5iL1mwh-A3KT4vxhDZlNVpC7r_c/s1600/1.JPG" /></a>标志 选择network &amp; sharing center</span></div>
<div>
<div class="separator" style="clear: both; text-align: center;">
<span style="font-family: inherit;"><br /></span></div>
<span style="font-family: inherit;">3 进入以下页面 点Change adapter settings</span></div>
<div>
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZ9TvSkMptVDPAAyZD09V7NZ6-VPTUNw7VGfbo3uY6YXmUgMpTFzZJpzrNnoXXB3P7zJhDDiUh5P6ql3ZgA-h2aUhf2BGhUO5qQDqC1AcCmJLYoGAaUnv6IdIrKXRZR0bkHGhNjpPgM2g/s1600/2.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em; text-align: center;"><span style="font-family: inherit;"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZ9TvSkMptVDPAAyZD09V7NZ6-VPTUNw7VGfbo3uY6YXmUgMpTFzZJpzrNnoXXB3P7zJhDDiUh5P6ql3ZgA-h2aUhf2BGhUO5qQDqC1AcCmJLYoGAaUnv6IdIrKXRZR0bkHGhNjpPgM2g/s1600/2.JPG" height="344" width="640" /></span></a></div>
<div>
<span style="font-family: inherit;"><br /></span></div>
<div>
<span style="font-family: inherit;">4.选择链接中的wifi 和 ethernet 滑鼠右键选择 Bridge network.完成以后会多一个Network Bridge&nbsp;</span></div>
<div>
<span style="font-family: inherit;">如下图</span></div>
<div class="separator" style="clear: both; text-align: center;">
<span style="font-family: inherit;"><br /></span></div>
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5XE-RowkguR9pcfQ0TDVuIMRECWipeAN9ar53dPJraUibDju9mTusWsXOGFWd2526v9e6loIrqhKryojHKVkPOktC0AvKAShHAu04ffsamkrgtYET7XY5QHgG6nPtUN4V0Z5zSI14ty0/s1600/3.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><span style="font-family: inherit;"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5XE-RowkguR9pcfQ0TDVuIMRECWipeAN9ar53dPJraUibDju9mTusWsXOGFWd2526v9e6loIrqhKryojHKVkPOktC0AvKAShHAu04ffsamkrgtYET7XY5QHgG6nPtUN4V0Z5zSI14ty0/s1600/3.JPG" height="162" width="640" /></span></a></div>
<div>
<span style="font-family: inherit;"><br /></span></div>
<div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="font-family: inherit;">5.到这里基本上树莓派只要网线插上笔记本就能联网了（当然笔记本要已经联网），</span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<a href="http://ahbundance.blogspot.com/2014/05/blog-post.html"><span style="font-family: inherit;">树莓派基础回顾：【Raspberry PI 学习 I】初夜必备~树莓派+一根网线+笔记本电脑，低成本基础教程。</span></a></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="font-family: inherit;"><br /></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="font-family: inherit; font-size: large;"><b>开始进入固定IP设置</b></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
以下教程我也是参考的，如果要查看原文 可以进入<a href="http://blog.csdn.net/liang890319/article/details/8646125">这里</a></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="font-family: inherit;">设置树莓派为静态ip的方法和debian linux修改是一样的</span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="font-family: inherit;">只需要修改文件sudo vi /etc/network/interfaces文件即可</span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="font-family: inherit;">我的pi操作系统是2013-02-09-wheezy-raspbian.img</span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="font-family: inherit;"><br /></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="font-family: inherit;">/etc/network/interfaces原文件为dhcp获取ip，内容为</span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red; line-height: 23.981483459472656px;"><span style="font-family: inherit;">auto lo</span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="font-family: inherit;"><span style="color: red; line-height: 23.981483459472656px;">iface lo inet loopback</span><br style="color: red; line-height: 23.981483459472656px;" /><span style="color: red; line-height: 23.981483459472656px;">iface eth0 inet dhcp</span><br style="color: red; line-height: 23.981483459472656px;" /><span style="color: red; line-height: 23.981483459472656px;">allow-hotplug wlan0</span><br style="color: red; line-height: 23.981483459472656px;" /><span style="color: red; line-height: 23.981483459472656px;">iface wlan0 inet manual</span><br style="color: red; line-height: 23.981483459472656px;" /><span style="color: red; line-height: 23.981483459472656px;">wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf</span><br style="color: red; line-height: 23.981483459472656px;" /><span style="color: red; line-height: 23.981483459472656px;">iface default inet dhcp</span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red; line-height: 23.981483459472656px;"><span style="font-family: inherit;"><br /></span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="line-height: 23.981483459472656px;"><span style="color: #000099;"><strong><span style="font-family: inherit;">修改此文件的办法：</span></strong></span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red; line-height: 23.981483459472656px;"><span style="font-family: inherit;">1，树莓派接显示器，用键盘鼠标打开终端 修改文件</span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red; line-height: 23.981483459472656px;"><span style="font-family: inherit;">2，用ssh/VNC登录树莓派修改此文件</span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red; line-height: 23.981483459472656px;"><span style="font-family: inherit;">3，在linux下直接用读卡器读取SD卡 修改/etc/network/interfaces文件</span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red; line-height: 23.96666717529297px;"><span style="font-family: inherit;">（你可以先备份这个文件sudo cp /etc/network/interfaces /etc/network/interfaces.bk）</span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red;"><span style="line-height: 23.96666717529297px;"><span style="font-family: inherit;">想设置为静态ip需要这么做</span></span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red;"><span style="line-height: 23.96666717529297px;"><span style="font-family: inherit;">直接将iface eth0 inet dhcp</span></span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red;"><span style="line-height: 23.96666717529297px;"><span style="font-family: inherit;">替换为</span></span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="line-height: 23.96666717529297px;"><span style="font-family: inherit;"><span style="color: #006600;">iface eth0 inet static<br />address 192.168.1.88<br />netmask 255.255.255.0<br />gateway 192.168.1.1</span></span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red;"><span style="line-height: 23.96666717529297px;"><span style="font-family: inherit;">然后删除这一行 &nbsp;iface default inet dhcp(否则&nbsp;ip是固定的但是无法连外网)</span></span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red; line-height: 23.96666717529297px;"><span style="font-family: inherit;">修改后的文件为</span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="font-family: inherit;">auto lo<br />iface lo inet loopback<br />iface eth0 inet static<br />address 192.168.1.88<br />netmask 255.255.255.0<br />gateway 192.168.1.1<br />allow-hotplug wlan0<br />iface wlan0 inet manual<br />wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf</span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="font-family: inherit;"><br /></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red;"><span style="line-height: 23.96666717529297px;"><span style="font-family: inherit;">然后重启服务或系统</span></span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red;"><span style="line-height: 23.96666717529297px;"><span style="font-family: inherit;">sudo reboot</span></span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red;"><span style="line-height: 23.96666717529297px;"><span style="font-family: inherit;">root@raspberrypi:~# sudo service networking restart</span></span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red;"><span style="line-height: 23.96666717529297px;"><span style="font-family: inherit;">树莓派为静态ip而且可以连接外网</span></span></span></div>
<div style="background-color: white; color: #333333; line-height: 26px;">
<span style="color: red;"><span style="line-height: 23.96666717529297px;"><span style="font-family: inherit;"><br /></span></span></span></div>
<div style="background-color: white;">
好了今天就到这里，实际上我的进度已经把状态哎查询的网页架设好了<br />
尽快更新~</div>
</div>
