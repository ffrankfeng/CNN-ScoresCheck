#!/usr/bin/env python
# -*- coding:utf-8 -*-
#发布
from redisHelper import RedisHelper

dict = "{'key': 123,'title':13,'description':123,'done': False}"
print(type(dict))
task=bytes(dict, encoding='utf-8')
str1 = str(task, encoding="utf-8")
data = eval(str1)
key = data["key"]
# dict = {
#     'key': tasks[-1]['id'] + 1,  # task[-1]代表原来的最后一位
#     'title': request.json['title'],
#     'description': request.json.get('description', ""),
#     'done': False
# }
channel = key
obj = RedisHelper()
# channel = '123'
obj.setchannl(channel)
obj.publish('hello')#发布s
task = {
    'id': 1, #task[-1]代表原来的最后一位
    'title': 'mytitle',
    'description': 'mydescription',
    'done': False
}
print(task['id'])
print(task['title'])
print(type(task))