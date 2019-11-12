# weibosayhi
调用新浪微博API实现每天自动发天气、名言加配图等微博动态，并得到发送状态的微信提醒。

[TOC]

### 演示

我的微博 AlkeySheng  [weibo.com/2351446567](https://weibo.com/2351446567)

![alkeysheng weibo](https://github.com/AlkeySheng/weibosayhi/blob/master/TIM%E5%9B%BE%E7%89%8720191112110628.jpg?raw=true)

(居然还涨粉啦ｈｈｈｈｈ)



### 需要

- 获得新浪微博API的[token](https://www.jianshu.com/p/0f20eaaa0047)  自行获取token
- 获得[和风天气](https://dev.heweather.com/)API的key  注册后记住key
- 如需[server酱](http://sc.ftqq.com/3.version)微信提醒(非必要)  获得SCKEY



### 使用

python3 确保安装 json, urllib, requests库

1. `git clone` 本项目并打开`weibo.py`文件，填入`token`,`key`,`SCKEY(非必要)`，保存并退出

2. 打开`goodnight.py`填入天气预报的四个城市`city_1`,`city_2`,`city_3`,`city_4`，保存退出

3. 微博文案自行修改替换，但请注意微博140字数限制

4. 可添加`crontab`任务定时自动执行脚本，`linux`下`crontab -e`命令编辑输入

   ```shell
   29 22 * * * python3 ~/weibosayhi/goodnight.py
   50 7 * * * python3 ~/weibosayhi/goodmorning.py
   ```

   自行替换执行时间和文件实际保存路径 　`Windows`用户自求多福

   