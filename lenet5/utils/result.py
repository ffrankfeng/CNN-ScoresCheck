class Result(object):
    matrix = [[0 for i in range(2)] for i in range(20)]

    def __init__(self,isSucess,key,category,information,url):
        self.isSucess = isSucess
        self.key = key
        self.category = category
        self.information = information
        self.url = url

    def getkey(self):
        return self.key

    def getinformantin(self):
        return self.information

    def getcategory(self):
        return self.category

    def getisSucess(self):
        return self.isSucess

    def setkey(self,parm):
       self.key = parm


    def setcategory(self,parm):
        self.category = parm

    def setisSucess(self,parm):
        self.isSucess = parm



    def setinformation(self, parm):
        self.information = parm
    def seturl(self, parm):
        self.url = parm

    def obj_2_json(self):
        return {
            "isSucess":self.isSucess,
            "matrix": self.matrix,
            "key" : self.key,
            "category" : self.category,
            "information":self.information,
            "url":self.url
        }

    def tostring(self):
        return "isSucess:"+str(self.isSucess)+", matrix:"+str(self.matrix)+", key:"+str(self.key)+", category:"+str(self.category)+", information:"+str(self.information)+", url:"+str(self.url)
