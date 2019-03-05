#!/usr/bin/env python
# -*- coding:utf-8 -*-
#订阅
from redisHelper import RedisHelper

obj = RedisHelper()
obj.setchannl('45WFEQ6')
redis_sub = obj.subscribe()#调用订阅方法

print("client 2 start listening")
while True:
    msg= redis_sub.parse_response()
    print (msg)