# coding=UTF-8
from weibo import *
import json,urllib
import requests

try:
    say_goodmorning(get_moti(),get_img())
except:
    #requests.get("https://sc.ftqq.com/{}.send?text=问候失败！").format(your_SCKEY)
    print("ERROR")