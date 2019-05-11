#!/usr/bin/env python
#-*- coding:utf-8 -*-
import redis
from config import config

# redis工具类
class RedisHelper(object):
    def __init__(self): #10.166.33.86
        self.__conn = redis.Redis(host=config.REDIS_IP,port=config.REDIS_PORT)#连接Redis
        self.channel = '' #定义名称

    def rpush(self,name,values):
        self.__conn.rpush(name,values)
        return True

    def llen(self,name):
        return self.__conn.llen(name)

    def lpop(self,name):
        return  self.__conn.lpop(name)

    def set(self,key,value):
        self.__conn.set(key,value)
        return True
    def setchannl(self,channel):
        self.channel = channel


    def publish(self,msg):#定义发布方法
        if self.__conn.publish(self.channel,msg)>0:
            return "Finish"
        else:
            return "Failure"

    def subscribe(self):#定义订阅方法
        pub = self.__conn.pubsub()
        pub.subscribe(self.channel)
        pub.parse_response()
        return pub