---
title: "【Raspberry PI 学习 V】树莓派 更改键盘布局 从默认UK到US"
date: 2014-06-11
tags:
  - "Raspberry PI"
  - "学习"
  - "树莓派"
---

<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
终于我无需远程遥控去控制树莓派了，</div>
<div class="separator" style="clear: both; text-align: left;">
这时才发现无视已久的教程 设置键盘格式是有用的 ...</div>
<div class="separator" style="clear: both; text-align: left;">
由于树莓派默认键盘是UK 而我们一般使用的都是US的</div>
<div class="separator" style="clear: both; text-align: left;">
我们不得不对其做一些设置，否则...也没什么大不了 就一些符号打不出来咯！</div>
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div class="separator" style="clear: both;">
更改键盘布局，命令如下：</div>
<div class="separator" style="clear: both;">
</div>
<a name='more'></a><br />
<br />
<div class="separator" style="clear: both;">
<span style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">sudo dpkg-reconfigure keyboard-configuration</span><span style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">进入后，选通用的101键PC键盘</span></div>
<div class="separator" style="clear: both; text-align: left;">
<a href="/assets/img/blog/a070478d32b4.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="/assets/img/blog/a070478d32b4.png" height="321" width="400" /></a></div>
&nbsp;<span style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">按tab键，到OK，按Enter确定</span><span style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">在键盘layout选择中，选Other</span><br />
<div class="separator" style="clear: both; text-align: left;">
<a href="/assets/img/blog/83692ff715fc.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="/assets/img/blog/83692ff715fc.png" height="321" width="400" /></a></div>
<br />
<div class="separator" style="clear: both; text-align: left;">
<a href="/assets/img/blog/272d9783e171.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="/assets/img/blog/272d9783e171.png" height="312" width="400" /></a></div>
&nbsp;<span style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">按tab键，到OK，按Enter确定</span><span style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">然后在选项中，选English(US)</span><br />
<div class="separator" style="clear: both; text-align: left;">
<a href="/assets/img/blog/73531d863720.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="/assets/img/blog/73531d863720.png" height="322" width="400" /></a></div>
<span style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">按tab键，到OK，按Enter确定</span><br />
<span style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">再选English(US, alternative international)</span><br />
<div style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">
按tab键，到OK，按Enter确定</div>
<div style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">
然后一路按OK</div>
<div style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">
退出后，重启系统</div>
<div style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">
sudo reboot</div>
<div style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">
重新启动时，由于修改了键盘布局，在读取键盘布局的阶段会比平常慢一些</div>
<div style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">
OK了， 终于可以打出所有字符了</div>
<div style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">
这一点，linux还是不太方便，windows比较人性化一些</div>
<div style="background-color: white; color: #333333; font-family: Arial; font-size: 14px; line-height: 26px;">
不过付费与免费之间的差距 这也是必然存在的<br />
理解一下吧~</div>
