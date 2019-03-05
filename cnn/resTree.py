from ansBean import Bean
class BTree:
    def __init__(self,x,y,result,probability):
        self.left = None
        print(x,y,result,probability)
        self.data = Bean(x,y,result,probability)
        self.middle = None
        self.right = None
        self.parent = None
    def insertleft(self,x,y,result,probability):
        self.left = BTree(x,y,result,probability)
        self.left.parent = self
        return self.left
    def insertright(self,x,y,result,probability):
        self.right = BTree(x,y,result,probability)
        self.right.parent = self
        return self.right
    def insertmiddle(self,x,y,result,probability):
        self.middle = BTree(x,y,result,probability)
        self.middle.parent = self
        return self.middle
    def show(self):
        a = self.data
        print(self.data.tostring())


