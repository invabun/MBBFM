---
title: "How to install flash in Raspberry pi 2 "
date: 2015-03-06
tags:
  - "Raspberry PI"
  - "树莓派"
---

<div>
<br />
I believe some of you already know that Raspberry Pi 2 is support to used flash.<br />
Here I share with you how to install flash in Raspberry Pi 2.<br />
<br />
<div>
1.Install Chromium</div>
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">sudo apt-get install chromium</code></dd></dl>
<br />
<a name='more'></a><br />
<br />
<br /></div>
<div>
2 download flash player for armv7</div>
<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:.</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">wget http://odroidxu.leeharris.me.uk/PepperFlash-12.0.0.77-armv7h.tar.gz&nbsp;</code></dd><dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">tar -xzf PepperFlash-12.0.0.77-armv7h.tar.gz&nbsp;</code></dd><dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">cd PepperFlash&nbsp;</code></dd><dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">chmod +x *&nbsp;</code></dd><dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">sudo cp * /usr/lib/chromium/plugins</code></dd></dl>
<br />
3.add plugin to chromium<br />
<div>

<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">sudo nano /etc/chromium/
</code></dd></dl>
edit last code to<br />
<div>

<dl class="codebox" style="background-color: white; border: 1px solid rgb(216, 216, 216); color: #333333; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 19.2399997711182px; margin-bottom: 1.5em; padding: 3px;">
<dt style="border-top-color: rgb(204, 204, 204); border-top-style: solid; border-top-width: 1px; font-weight: bold; line-height: 2em; margin-bottom: 3px; text-transform: uppercase;">CODE:</dt>
<dd style="line-height: 2em; margin: 0.5em auto;"><code style="background-color: #f7f7f9; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; border-top-left-radius: 3px; border-top-right-radius: 3px; border: 1px solid rgb(225, 225, 232); color: #8b8b8b; display: block; font-family: Monaco, 'Andale Mono', 'Courier New', Courier, mono; height: auto; line-height: 1.3em; margin: 2px 0px; max-height: 200px; overflow: auto; padding: 5px 4px 3px;">CHROMIUM_FLAGS="--ppapi-flash-path=/usr/lib/chromium/plugins/libpepflashplayer.so --ppapi-flash-version=12.0.0.77 -password-store=detect -user-data-dir"
</code></dd></dl>
<br />
<div>
save</div>
<div>
<br /></div>
<div>
4.Open Chromium browser ,type chrome: //plugs in address bar check flash plugin install status .&nbsp;</div>
<div>
<br /></div>
<div>
5.Now enjoy flash !</div>
<div>
<br /></div>
and share with me why you need flash in your Raspberry PI ?</div>
</div>
