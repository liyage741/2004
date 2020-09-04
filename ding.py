# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:framework
# File_name:ding.py.py
# Author: liyage
# Time:2020年09月04日
import json
import requests

def message(link=1):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=d3990b6042243d2efa9a1dc2a38ad798e9b3f73d7659bf77c18cbde53db355dc'
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "：%s " % ('大家好，我是罗海涛，我敢吃屎，一次一顿，你敢吃吗')
        },
        "at":{
            "atMobiles":[
                "15837848151"       #需要填写自己的手机号，钉钉通过手机号@对应人
            ],
            "isAtAll": True     #是否@所有人，默认否
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(url, data=json.dumps(pagrem), headers=headers)

if __name__ == "__main__":
    message()
