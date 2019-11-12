# coding=UTF-8
"""
Website https://2017.work
Github  https://github.com/AlkeySheng
AlkeySheng
"""

import json,urllib
import requests

your_token = "把微博API获得的token填入此处"
your_key = "把和风天气API获得的key填入此处"
your_SCKEY　= "如需server酱微信提醒　填入此SCKEY并取消下面requsts.get(×××)代码的注释　不需要请忽略"

def say_goodnight(date,wea1,wea2,wea3,wea4,txt):
    url = "https://api.weibo.com/2/statuses/share.json"
    if len(txt) <= 24:
        payload = {"access_token":your_token,"status":"明天是{}年{}月{}日 https://github.com/\n\n{}\n{}\n{}\n{}\n{}\n「我当然还爱你  晚安」".format(date[0:4],date[5:7],date[8:10],wea1,wea2,wea3,wea4,txt)}
    elif len(txt)<=27:
        payload = {"access_token":your_token,"status":"明天是{}年{}月{}日 https://github.com/\n{}\n{}\n{}\n{}\n{}\n「我当然还爱你  晚安」".format(date[0:4],date[5:7],date[8:10],wea1,wea2,wea3,wea4,txt)}
    else:
        payload = {"access_token":your_token,"status":"明天是{}年{}月{}日 https://github.com/\n\n{}\n{}\n{}\n{}\n\n「我当然还爱你  晚安」".format(date[0:4],date[5:7],date[8:10],wea1,wea2,wea3,wea4)}

    r = requests.post(url,data = payload)
    #requests.get("https://sc.ftqq.com/{}.send?text=已问候").format(your_SCKEY)

def say_goodmorning(txt,src):
    url = "https://api.weibo.com/2/statuses/share.json"
    payload={"access_token":your_token,"status":"{}\n\n\n「只有上帝知道我有多爱你　早上好」".format(txt)}
    files={"pic":open(src,"rb")}
    #POST请求，发表微博
    r = requests.post(url,data=payload,files = files)
    #requests.get("https://sc.ftqq.com/{}.send?text=已问候").format(your_SCKEY)


def get_moti():
    toko = requests.get("https://v1.hitokoto.cn/")
    moti = toko.json()
    txt = "{}https://github.com/AlkeySheng\n\n                                      -「{}」".format(moti["hitokoto"],moti["from"])
    return txt


def get_img():
    url= requests.get("https://api.imo6.cn/anime720/api.php?r=url")
    r = requests.get(url.text)
    src = "{}.jpg".format(url.text[-20:-10])
    urllib.request.urlretrieve(url.text,'{}'.format(src))
    return src

def info(city):
    w = requests.get("https://free-api.heweather.net/s6/weather/forecast?location={}&key={}".format(city,your_key))
    r = requests.get("https://free-api.heweather.net/s6/weather/lifestyle?location={}&key={}".format(city,your_key))
    w.encoding = 'utf-8'
    r.encoding = 'utf-8'
    weathers = w.json()
    lifestyle = r.json()
    txt = "{}".format(lifestyle["HeWeather6"][0]["lifestyle"][0]["txt"])
    pri="{0:{5}<3}{1:{5}<4}  {2:0>2}℃~{3:0>2}℃    日出:{4}".format(weathers["HeWeather6"][0]["basic"]["location"],weathers["HeWeather6"][0]["daily_forecast"][1]["cond_txt_d"],weathers["HeWeather6"][0]["daily_forecast"][1]["tmp_min"],weathers["HeWeather6"][0]["daily_forecast"][1]["tmp_max"],weathers["HeWeather6"][0]["daily_forecast"][1]["sr"],chr(12288))
    date="{}".format(weathers["HeWeather6"][0]["daily_forecast"][1]["date"])
    
    return pri,date,txt


