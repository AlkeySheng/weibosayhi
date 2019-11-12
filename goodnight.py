# coding=UTF-8
from weibo import *
import json
import requests

city_1:""
city_2:""
city_3:""
city_4:""

try:
    say_goodnight(info(city_1)[1],info(city_1)[0],info(city_2)[0],info(city_3)[0],info(city_4)[0],info(city_1)[2])
except:
    #requests.get("https://sc.ftqq.com/{}.send?text=问候失败！").format(your_SCKEY)
    print("ERROR")