# coding:utf-8

class Item(object):
    def __init__(self,id,ip,time,key,url):
        self.id = id
        self.ip = ip
        self.time = time
        self.key = key
        self.url = url


    def getip(self):
        return self.ip

    def getid(self, parm):
        self.id = parm

    def gettime(self, parm):
        self.time = parm

    def getkey(self, parm):
        self.key = parm

    def geturl(self, parm):
        self.url = parm

    def obj_2_json(self):
        return {
            "id":self.id,
            "ip":self.ip,
            "time":self.time,
            "key":self.key,
            "url":self.url
        }