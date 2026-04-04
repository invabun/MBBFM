---
title: "[教学] 如何在树莓派试玩雷神之锤III 竞技场 How to play Quake III with Raspberry Pi"
date: 2014-08-30
tags:
  - "Raspberry PI"
  - "树莓派"
---

又是折腾时间~<br />
树莓派能干什么?<br />
<a href="http://ahbundance.blogspot.com/2014/08/raspberry-pi-10.html">前一帖子说了官方给出的10种已知功能</a><br />
其中一条就是拿来玩游戏<br />
这也是大部分人（其实是我啦）的兴趣<br />
<br />
作为低端学习机 才700GHz 即使设置是允许调到1000GHz<br />
又能玩什么游戏呢？<br />
<br />
今天来一个历史悠久的<a href="http://zh.wikipedia.org/wiki/FPS">FPS游戏</a><br />
Quake III<br />
<br />
直接来上效果视频~ （欢迎在youtube 频道上订阅）<br />
<br />
<div class="separator" style="clear: both; text-align: left;">
<iframe allowfullscreen='allowfullscreen' webkitallowfullscreen='webkitallowfullscreen' mozallowfullscreen='mozallowfullscreen' width='320' height='266' src='https://www.youtube.com/embed/8bUo5TSyOtk?feature=player_embedded' frameborder='0'></iframe></div>
<div class="separator" style="clear: both; text-align: left;">
</div>
<a name='more'></a><br />
<br />
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;"><br /></span>
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;">事不宜迟我们来学习吧</span><br />
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;">需要器材：</span><br />
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;">1.安装Raspbian系统的树莓派</span><br />
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;">2.能联网（安装时）</span><br />
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;">3.键盘，滑鼠</span><br />
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;">4.荧幕</span><br />
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;"><br /></span>
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;"><a href="http://www.raspberrypi.org/forums/viewtopic.php?f=78&amp;t=18853">教程也可以参考官方链接英文版</a></span><br />
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;">1: 先登入你的树莓派 无论用SSH 或者直接操作复制下面的代码</span><br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:&nbsp;</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">sudo apt-get install git gcc build-essential libsdl1.2-dev</code></dd></dl>
上面这代码让你安装Quake 3的开源码<br />
<br style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;" />
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;">2: 用以下代码更改部分源码</span><br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:&nbsp;</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">git clone https://github.com/raspberrypi/quake3.git</code></dd></dl>
然后用下面这条更改修改的目录文件夹<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:&nbsp;</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">cd quake3</code></dd></dl>
<br style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;" />
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;">3:现在我们已经完成安装，但是尚未能够进行游戏。我们需要修改一些游戏文件的配置。</span><br />
透过以下代码我们可以进入修改配置画面。<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:&nbsp;</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">nano build.sh</code></dd></dl>
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;">小白式更改：</span><br />
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;">从上面算起第八行 有</span><span style="color: #333333; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;"><span style="line-height: 19.2399997711182px;">ARM_LIBS 如果找不到可以用Ctrl-w 按钮（搜索）打入ARM_LIBS去找。</span></span><br />
<span style="color: #333333; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;"><span style="line-height: 19.2399997711182px;">烧到后将ARM_LIBS 的部分改成以下内容</span></span><br />
<br style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;" />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:&nbsp;</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">ARM_LIBS=/opt/vc/lib</code></dd></dl>
然后就是第16行 更改如下<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:&nbsp;</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">INCLUDES="-I/opt/vc/include -I/opt/vc/include/interface/vcos/pthreads"</code></dd></dl>
最后就是第19行<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:&nbsp;</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">#CROSS_COMPILE=bcm2708-</code></dd></dl>
<br style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;" />
<br style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;" />
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;">4:更改完毕后 按Ctrl+x 储存 然后按 Y 确认覆盖</span><span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;">然后输入 ./build.sh 系统会自动开始编译。这个过程大概会画30分钟吧。</span><br />
<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:&nbsp;</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">./build.sh</code></dd></dl>
<br />
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;">5: 一旦完成，需要再下载一个 pak 文件，这可以让游戏运行。</span><br />
<br />
输入<br />
<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:&nbsp;</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">wget http://dl.dropbox.com/u/1816557/Q3%20Demo%20Paks.zip</code></dd></dl>
<span style="color: #333333; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;"><span style="line-height: 19.2399997711182px;">** 注意 请确认下载的文件解压后放在baseq3文件夹里 否则是无法运行的</span></span><br />
<span style="color: #333333; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;"><span style="line-height: 19.2399997711182px;">文件夹目录 如果你的用户名是默认的 pi 那么会如下</span></span><br />
<span style="color: #333333; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;"><span style="line-height: 19.2399997711182px;">/home/pi/quake3/build/release-linux-arm/baseq3<br />解压后是数个文件 直接放到这个文件夹就行。</span></span><br />
<br />
<span style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;">6:<b>开始游戏！</b></span><br />
<br />
直接输入进入文件夹的命令。<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:&nbsp;</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">cd /quake3/build/release-linux-arm/</code></dd></dl>
然后用以下代码开始游戏。<br />
<br />
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:&nbsp;</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">sudo ./ioquake3.arm</code></dd></dl>
结果就如上边的测试视频一般 好好回忆过去 玩吧~！<br />
<br style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;" />
<span style="color: #333333; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;"><span style="background-color: #fefeff; line-height: 19.2399997711182px;">欢迎订阅我的部落格和<a href="http://www.youtube.com/channel/UC4bgvCbUSHs3p-SNLjZL9mQ">Youtube频道</a></span></span><br />
<span style="color: #333333; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;"><span style="background-color: #fefeff; line-height: 19.2399997711182px;"><br /></span><span style="background-color: #fefeff; line-height: 19.2399997711182px;">感谢树莓派</span></span><br />
<br />
<span style="color: #333333; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;"><span style="background-color: #fefeff; line-height: 19.2399997711182px;">P/S:谁安装成功了 欢迎告诉我哈~</span></span><br />
<br style="background-color: #fefeff; color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px;" />
<br />