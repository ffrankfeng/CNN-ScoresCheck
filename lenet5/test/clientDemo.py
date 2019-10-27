#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

from requests import post
from config import config
pic = config.PROJECT_PATH+"test_pic/pic_send/"

img=[pic+'0.png',
     pic+'1.png',
     pic+'2.png',
     pic+'3.png']
score=[40,20,20,100]

def send():
    # 新加任务
    for i in range(1):  # 10.166.33.86
        list4 = post('http://localhost:5555/todos', json.dumps(
            {'img': img,
             'key': '0 - '+ str(i),
             'score': score,
             'count': len(img),
             'serial': "01 - " + str(i),
             'category': '1',
             'proportion': 3
             }))
        # response
        print(list4.text)

if __name__ == '__main__':
    send()
