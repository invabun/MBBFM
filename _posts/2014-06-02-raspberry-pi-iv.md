---
title: "【Raspberry PI 学习 IV】树莓派 安装NO-IP 免费域名服务+开机自动启动软件（英文版）"
date: 2014-06-02
tags:
  - "Raspberry PI"
  - "树莓派"
---

<h3 class="post-title entry-title" itemprop="name" style="background-color: white; margin: 0px; position: relative;">
</h3>
<h3 class="post-title entry-title" itemprop="name" style="background-color: white; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 18px; font-weight: normal; margin: 0px; position: relative;">
中文资源有限，或许是很多中国网站我根本上不去吧。</h3>
<div>
好不容易混进去的百度贴吧也总出现断线的问题，</div>
<div>
只好参考英文教程了。</div>
<div>
由于都是很基本的英文，我可以看懂。<br />
所以没有朋友要求我就不翻译了。</div>
<div>
这个教程主要说的是如何开机启动软件（start up）</div>
<div>
<br /></div>
<h3 class="post-title entry-title" itemprop="name" style="background-color: white; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 18px; font-weight: normal; margin: 0px; position: relative;">
Raspberry Pi - run program at start-up<br /><a name='more'></a></h3>
<div class="post-header" style="background-color: white; color: #959595; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 14px; line-height: 1.6; margin: 0px 0px 1.5em;">
<div class="post-header-line-1">
</div>
</div>
<div class="post-body entry-content" id="post-body-2840285712861801216" itemprop="description articleBody" style="background-color: white; font-family: Arial, Tahoma, Helvetica, FreeSans, sans-serif; font-size: 15px; line-height: 1.4; position: relative; width: 598px;">
Anyway, I wanted to get my Raspberry Pi to start&nbsp;<a href="http://www.no-ip.com/" style="color: #0e197e; text-decoration: none;">no-ip dynamic dns service</a>&nbsp;when it started-up, so I wouldn't have to remember to start it every time it was powered up.&nbsp; For details on how to&nbsp;<a href="http://stuffaboutcode.blogspot.co.uk/2012/06/raspberry-pi-access-from-internet-using.html" style="color: #0e197e; text-decoration: none;">install no-ip on the Pi</a>, see this&nbsp;<a href="http://stuffaboutcode.blogspot.co.uk/2012/06/raspberry-pi-access-from-internet-using.html" style="color: #0e197e; text-decoration: none;">post</a>.<br />
<br />
There are loads of ways of running a command at start-up in&nbsp;Linux&nbsp;but my favoured approach is to create an initialisation script in /etc/init.d and register it using&nbsp;update-rc.d. &nbsp;This way the application is started and stopped automatically when the system boots / shutdowns.<br />
<br />
<b>Create script in /etc/init.d</b><br />
<div style="border: 1px solid black;">
<span style="font-family: 'Courier New', Courier, monospace;">sudo nano /etc/init.d/NameOfYourScript</span></div>
<br />
The following is an example based on starting up the no-ip service [/usr/local/bin/noip], but change the name of the script and the command to start and stop it and it would work for any command.<br />
<br />
<div style="border: 1px solid black;">
<span style="color: #38761d; font-family: 'Courier New', Courier, monospace;">#! /bin/sh</span><br />
<span style="color: #38761d; font-family: 'Courier New', Courier, monospace;"># /etc/init.d/noip</span>&nbsp;<span style="color: #38761d; font-family: 'Courier New', Courier, monospace;"></span><br />
<span style="font-family: 'Courier New', Courier, monospace;"></span><br />
<span style="color: #38761d; font-family: 'Courier New', Courier, monospace;">### BEGIN INIT INFO<br /># Provides:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; noip<br /># Required-Start:&nbsp;&nbsp;&nbsp; $remote_fs $syslog<br /># Required-Stop:&nbsp;&nbsp;&nbsp;&nbsp; $remote_fs $syslog<br /># Default-Start:&nbsp;&nbsp;&nbsp;&nbsp; 2 3 4 5<br /># Default-Stop:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0 1 6<br /># Short-Description: Simple script to start a program at boot<br /># Description:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A simple script from&nbsp;</span><a href="http://www.stuffaboutcode.com/" style="color: #0e197e; text-decoration: none;"><span style="color: #38761d; font-family: 'Courier New', Courier, monospace;">www.stuffaboutcode.com</span></a><span style="color: #38761d; font-family: 'Courier New', Courier, monospace;">which will start / stop a program a boot / shutdown.<br />### END INIT INFO</span><br />
<span style="color: #38761d;"></span><br />
<span style="color: #38761d; font-family: 'Courier New', Courier, monospace;"># If you want a command to always run, put it here</span><br />
<br />
<span style="color: #38761d; font-family: 'Courier New', Courier, monospace;"># Carry out specific functions when asked to by the system</span><br />
<span style="font-family: 'Courier New', Courier, monospace;"><span style="color: blue;">case&nbsp;</span><span style="color: #990000;">"$1"</span>&nbsp;<span style="color: blue;">in</span></span><br />
<span style="font-family: 'Courier New', Courier, monospace;">&nbsp; start)</span><br />
<span style="font-family: 'Courier New', Courier, monospace;">&nbsp; &nbsp;&nbsp;<span style="color: blue;">echo&nbsp;</span><span style="color: #990000;">"Starting noip"</span></span><br />
<span style="font-family: 'Courier New', Courier, monospace;">&nbsp; &nbsp;&nbsp;<span style="color: #38761d;"># run application you want to start</span></span><br />
<span style="font-family: 'Courier New', Courier, monospace;">&nbsp; &nbsp; /usr/local/bin/noip2</span><br />
<span style="font-family: 'Courier New', Courier, monospace;">&nbsp; &nbsp; ;;</span><br />
<span style="font-family: 'Courier New', Courier, monospace;">&nbsp; stop)</span><br />
<span style="font-family: 'Courier New', Courier, monospace;">&nbsp; &nbsp;&nbsp;<span style="color: blue;">echo&nbsp;</span><span style="color: #990000;">"Stopping noip"</span></span><br />
<span style="font-family: 'Courier New', Courier, monospace;">&nbsp; &nbsp;&nbsp;<span style="color: #38761d;"># kill application you want to stop</span></span><br />
<span style="font-family: 'Courier New', Courier, monospace;">&nbsp; &nbsp; killall noip2</span><br />
<span style="font-family: 'Courier New', Courier, monospace;">&nbsp; &nbsp; ;;</span><br />
<span style="font-family: 'Courier New', Courier, monospace;">&nbsp; *)</span><br />
<span style="font-family: 'Courier New', Courier, monospace;">&nbsp; &nbsp;&nbsp;<span style="color: blue;">echo</span>&nbsp;<span style="color: #990000;">"Usage: /etc/init.d/noip {start|stop}"</span></span><br />
<span style="font-family: 'Courier New', Courier, monospace;">&nbsp; &nbsp;&nbsp;<span style="color: blue;">exit</span>&nbsp;1</span><br />
<span style="font-family: 'Courier New', Courier, monospace;">&nbsp; &nbsp; ;;</span><br />
<span style="color: blue; font-family: 'Courier New', Courier, monospace;">esac</span><br />
<span style="font-family: 'Courier New', Courier, monospace;"><br /></span><span style="font-family: 'Courier New', Courier, monospace;"><span style="color: blue;">exit</span>&nbsp;0</span></div>
<br />
<span style="color: red;">Warning</span>&nbsp;- its important you test your script first and make sure it doesn't need a user to provide a response, press "y" or similar, because you may find it hangs the raspberry pi on boot waiting for a user (who's not there) to do something!<br />
<div>
<br />
<b>Make script executable</b><br />
<div style="border: 1px solid black;">
<span style="font-family: 'Courier New', Courier, monospace;">sudo chmod 755 /etc/init.d/NameOfYourScript</span></div>
<br />
<b>Test starting the program</b><br />
<div style="border: 1px solid black;">
<span style="font-family: 'Courier New', Courier, monospace;">sudo /etc/init.d/NameOfYourScript start</span></div>
<br />
<b>Test stopping the program</b><br />
<div style="border: 1px solid black;">
<span style="font-family: 'Courier New', Courier, monospace;">sudo /etc/init.d/NameOfYourScript stop</span></div>
<br />
<b>Register script to be run at start-up</b><br />
To register your script to be run at start-up and shutdown, run the following command:<br />
<br />
<div style="border: 1px solid black;">
<span style="font-family: 'Courier New', Courier, monospace;">sudo update-rc.d NameOfYourScript defaults</span></div>
</div>
<br />
Note - The header at the start is to make the script LSB compliant and provides details about the start up script and&nbsp;you should only need to change the name.&nbsp; If you want to know more about creating LSB scripts for managing services, see&nbsp;<a href="http://wiki.debian.org/LSBInitScripts" style="color: #0e197e; text-decoration: none;">http://wiki.debian.org/LSBInitScripts</a><br />
<br />
If you ever want to remove the script from start-up, run the following command:<br />
<br />
<div style="border: 1px solid black;">
<span style="font-family: 'Courier New', Courier, monospace;">sudo update-rc.d -f&nbsp;</span>&nbsp;<span style="font-family: 'Courier New', Courier, monospace;">NameOfYourScript</span>&nbsp;<span style="font-family: 'Courier New', Courier, monospace;">remove</span></div>
</div>
