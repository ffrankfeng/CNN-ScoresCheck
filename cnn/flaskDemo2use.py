from flask import Flask,request
from flask_restful import Api, Resource, reqparse
import time
import threading
from time import sleep

#发布
from redisHelper import RedisHelper
import mnist_app
import os

logPath = "log/"
requestCache = "tasksTest:task1"
categoryArr = {'0','1','2'}

app = Flask(__name__)
api = Api(app)
obj = RedisHelper()
#请求参数
parser = reqparse.RequestParser()

parser.add_argument('img[]', type=list)
parser.add_argument('score[]', type=list)
parser.add_argument('count', type=int)
parser.add_argument('key', type=str)
parser.add_argument('serial', type=str)
parser.add_argument('category', type=str)
errorImg=[]
img=[]
score=[]
isFound = True
# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):

    def post(self):
        args = parser.parse_args()
        print(args)
        list= request.form.getlist("img[]")
        print(list)
        todo = {
            'ip' : request.remote_addr,
            'time' : time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
            'key' : args['key'],
            'category' : args['category'],
            'img': args['img[]'],
            'score': args['score[]'],
            'count': args['count'],
            'serial': args['serial']
        }
        print(todo)
        key = todo["key"].strip()
        serial = todo["serial"].strip()
        # keysp = key.split('_')
        img = todo["img"]
        score = todo["score"]
        count = todo["count"]
        print(score)
        print(len(score))
        if count < len(score):
            return {"status": "failed", "key": key, "serial": serial,"time":12, "errorImg": None,"information": "img count is less than score length"}
        for url in img:
            if not os.path.exists(url):
                errorImg.append(url)
                isFound= False;
        if isFound == False:
            return {"status": "failed", "key": key,"serial":serial,"time":12, "errorImg":errorImg,"information":"file not found"}
        category = todo["category"].strip()
        if category not in categoryArr:
            return {"status": "failed", "key": key, "serial": serial,"time":12,"errorImg": None, "information": "category is illegal"}

        obj.rpush(requestCache, todo)  # 添加
        return {"status": "succeed", "key": key, "serial": serial,"time":12, "errorImg": None, "information": None}

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')

#处理请求
def identify():

    while True:
        print("ok")
        # task = obj.lpop(requestCache)
        # if(task !=None):
        #     str1 = str(task, encoding="utf-8")
        #     data = eval(str1)
        #     category = data["category"].strip()
        #     imgPath = data["url"].strip()
        #     keyAndNum = data["key"].strip()
        #     ip = data["ip"].strip()
        #
        #     sp = keyAndNum. split('_')
        #     channel = sp[0]
        #     # 分类识别
        #     # if(category == 1)
        #     jResult = mnist_app.application(imgPath)
        #     jResult.setkey(keyAndNum)
        #     jResult.setcategory(category)
        #     print(jResult.obj_2_json())
        #     #定义频道，发布
        #     obj.setchannl(channel)
        #     isFinish = obj.publish(jResult.obj_2_json())
        #     #log日记
        #     logName = time.strftime('%Y.%m', time.localtime(time.time()))
        #     f = open(logPath + str(logName)+".log", "a+")
        #     Date = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
        #     f.write(str(isFinish)+" - - "+ip + " - - [" + Date + "] - - ")
        #     f.write(jResult.tostring())
        #     f.write("\n")
        #     f.close()


if __name__ == '__main__':
    # 处理请求
    threading.Thread(target=identify).start()
    #启动flask
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True)
