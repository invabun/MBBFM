---
title: "【教学】如何使用Blogsspot 在HTML 以五个简单步骤做一个Code的框架(傻瓜级)"
date: 2014-08-31
tags:
  - "学习"
---

很多学习编程的朋友也会尝试制作属于自己的教程<br />
说到编程 打Code肯定少不了<br />
既然是编程教程 需要有一个code 的框架也少不了<br />
<br />
Blogspot本身原设没有支持&lt;code&gt;&lt;/code&gt;的<br />
需要自行添加<br />
但是在那个复杂的修改过程之前 我们来做个简单的傻瓜级教程。<br />
<br />
先上个效果<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">这里输入内容</code></dd></dl>
以上这个效果的code 其实是一堆code演变的<br />
看起来可能会很乱 其实有心 这就是傻瓜级的活了。<br />
<br />
<a name='more'></a><br />
<br />
1,复制下面的code<br />
<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:</dt>
<dd style="margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); display: block; height: auto; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;"><code style="border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); display: block; height: auto; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;"><span style="color: #8b8b8b; font-family: Monaco, Andale Mono, Courier New, Courier, mono;"><span style="line-height: 20.7999992370605px;">&lt;dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;"&gt;</span></span></code><code style="border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); display: block; height: auto; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;"><span style="color: #8b8b8b; font-family: Monaco, Andale Mono, Courier New, Courier, mono;"><span style="line-height: 20.7999992370605px;">&lt;dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;"&gt;CODE:&lt;/dt&gt;</span></span></code><code style="border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); display: block; height: auto; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;"><span style="color: #8b8b8b; font-family: Monaco, Andale Mono, Courier New, Courier, mono;"><span style="line-height: 20.7999992370605px;">&lt;dd style="line-height: 2em; margin: 0.5em auto;"&gt;&lt;code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;"&gt;这里输入内容&lt;/code&gt;&lt;/dd&gt;&lt;/dl&gt;</span><span style="line-height: 20.7999992370605px;">&lt;br/&gt;</span></span></code></code></dd></dl>
<b>2.在部落格发帖的左上角点HTML</b><br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmWjs5p-60L3Y_eo0zc6tBDobPlzl85zq2_0MBykKD7wp7f6wCQ5bwPqsKOFLeGBw9MQNojIvp1fthCe95pPD7jbWo34y24CfOvWSugg1hNiyy6TOE23E1Fo-TGfMV8nwZloUZ8Yr3e-k/s1600/123.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmWjs5p-60L3Y_eo0zc6tBDobPlzl85zq2_0MBykKD7wp7f6wCQ5bwPqsKOFLeGBw9MQNojIvp1fthCe95pPD7jbWo34y24CfOvWSugg1hNiyy6TOE23E1Fo-TGfMV8nwZloUZ8Yr3e-k/s1600/123.JPG" height="282" width="320" /></a></div>
<br />
<br />
<b>3.预计你要多少个框 就粘贴多少个&nbsp;</b><br />
*为了好看 在HTML粘贴完一个便空一行吧 免得自己有需要修改的时候自己乱套了<br />
<br />
效果如下：<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">这里输入内容</code></dd></dl>
<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">这里输入内容</code></dd></dl>
<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">这里输入内容</code></dd></dl>
<b>4.回到Compose 页面</b><br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1YNhPDEKFCAnrbY0iV3pZYeEAX2PbAZ0X6aiZ1hcq1Zxsz0eNsv1nBBiPxCjOT7K3uz0Uog039bVF3x2fAK5YURkGyi6DJ-sYXk6MeOZ1y4Kx35AartDThrfcOLnNAeAsBUANi_uzfUk/s1600/123.JPG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1YNhPDEKFCAnrbY0iV3pZYeEAX2PbAZ0X6aiZ1hcq1Zxsz0eNsv1nBBiPxCjOT7K3uz0Uog039bVF3x2fAK5YURkGyi6DJ-sYXk6MeOZ1y4Kx35AartDThrfcOLnNAeAsBUANi_uzfUk/s1600/123.JPG" height="320" width="282" /></a></div>
<div class="separator" style="clear: both; text-align: left;">
<b>5.直接在框框上写入 或Paste 你的code&nbsp;</b></div>
<div class="separator" style="clear: both; text-align: left;">
就这样完成啦~</div>
<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">12345</code></dd></dl>
<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">上山打老虎</code></dd></dl>
<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">结果打到小老鼠</code></dd></dl>
本次简单复制法 到此为止，<br />
欢迎大家订阅我的部落格<br />
有更好意见的朋友也欢迎和我分享<br />
<br />
9月5日添加其他款式<br />
<br />
<br />
<code style="background: url(https://sites.google.com/site/klcintwimages/Code_BG.gif) 0% 0% repeat-y rgb(240, 240, 240); border: 1px solid rgb(204, 204, 204); color: #333333; display: block; font-family: 'Courier New'; font-size: 10pt; line-height: 1.2em; max-height: 200px; overflow: auto; padding: 10px 10px 10px 21px;">type your code here</code>
<br />
<br />
<br />
在这个code 最前和最后加 &lt; 和 &lt;/code&gt;<br />
<br />
code style="background: url(https://sites.google.com/site/klcintwimages/Code_BG.gif) 0% 0% repeat-y rgb(240, 240, 240); border: 1px solid rgb(204, 204, 204); color: #333333; display: block; font-family: 'Courier New'; font-size: 10pt; line-height: 1.2em; max-height: 200px; overflow: auto; padding: 10px 10px 10px 21px;"&gt;type your code here