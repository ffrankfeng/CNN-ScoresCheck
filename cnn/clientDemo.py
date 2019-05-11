#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

from requests import post


img=['test_pic/pic_send/0.png','test_pic/pic_send/1.png','test_pic/pic_send/2.png','test_pic/pic_send/3.png']
score=[40,20,20,100]

def send():
    # 新加任务
    for i in range(1):  # 10.166.33.86
        list4 = post('http://localhost:5555/todos', json.dumps(
            {'img': img,
             'key': 'hgedwd12',
             'score': score,
             'count': len(img),
             'serial': "01k4c" + str(i),
             'category': '1',
             'proportion': 3
             }))
        # response
        print(list4.text)

if __name__ == '__main__':
    send()
