class Bean(object):
    def __init__(self,x,y,result,probability):
        self.x = x
        self.y = y
        self.result = result
        self.probability = probability

    def getresult(self):
        return self.result

    def getprobability(self):
        return self.probability

    def setresult(self, parm):
        self.result = parm

    def setprobability(self, parm):
        self.probability = parm


    def obj_2_json(self):
        return {
            "result":self.result,
            "probability": self.probability
        }

    def tostring(self):
        return "x:"+str(self.x)+",y:"+str(self.y)+",result:"+str(self.result)+", probability:"+str(self.probability)
