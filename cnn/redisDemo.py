#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis

pool = redis.ConnectionPool(host='10.166.33.86', port=6379)
r = redis.Redis(connection_pool=pool)
# r.set('name', 'zhangsan')   #添加
# dic={"a1":"aa","b1":"bb"}
# r.hmset("dic_name",dic)
# print(r.hget("dic_name","b1"))

for i in range(10):
    task = {
        'id': i,  # task[-1]代表原来的最后一位
        'title': 'mytitle',
        'description': 'mydescription',
        'done': False
    }
    r.rpush('lists:l', task)  # 添加
print(r.lpop('lists:l'))
print(r.lpop('lists:l'))
# print (r.get('name'))   #获取