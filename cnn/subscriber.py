#!/usr/bin/env python
# -*- coding:utf-8 -*-
#订阅
from redisHelper import RedisHelper

obj = RedisHelper()
# obj.setchannl("127.0.0.1")
obj.setchannl("DEFG4432RFFR")
redis_sub = obj.subscribe()#调用订阅方法

print("client 1 start listening")
while True:
    msg= redis_sub.parse_response()
    print (msg)