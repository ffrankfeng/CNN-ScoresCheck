
#发布

from redisHelper import RedisHelper
import mnist_app
import  numpy
import os
import json
import time
import threading
from flask import Flask
from flask import request
import Calculation
app = Flask(__name__)
obj = RedisHelper()


img=[]
score=[]
logPath = "log/"
requestCache = "tasks:task"
resultSavePath = "RegResult"
paramSavePath = "ParamResult"
categoryArr = {'0','1','2'}
@app.route('/todos', methods=['GET', 'POST'])
# def route_url():
#     if request.method == 'POST':
def post():
    isFound = True
    errorImg = []
    try:
        data = request.get_data()
        dict_data = json.loads(data.decode("utf-8"))
        # print(dict_data)
        key = dict_data["key"].strip()
        serial = dict_data["serial"].strip()
        # keysp = key.split('_')
        img = dict_data["img"]
        score = dict_data["score"]
        count = dict_data["count"]
        if count < len(score):
            return json.dumps({"status": "failed", "key": key, "serial": serial, "time": 0, "errorImg": None,
                    "information": "img count is less than score length"})
        for url in img:
            if not os.path.exists(url):
                errorImg.append(url)
                isFound = False;
        if isFound == False:
            return json.dumps({"status": "failed", "key": key, "serial": serial, "time": 0, "errorImg": errorImg,
                    "information": "file not found"})
        category = dict_data["category"].strip()
        if category not in categoryArr:
            return json.dumps({"status": "failed", "key": key, "serial": serial, "time": 0, "errorImg": None,
                    "information": "category is illegal"})
        dict_data["time"] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        dict_data["ip"] = request.remote_addr
        proportion = dict_data["proportion"]
    except:
        # print("error")
        return json.dumps({"status": "failed", "key": key, "serial": serial, "time": 0, "errorImg": None,
                           "information": "can not get propery"})
    obj.rpush(requestCache, dict_data)  # 添加
    return json.dumps({"status": "succeed", "key": key, "serial": serial,'proportion':proportion,"time":obj.llen(requestCache)*50 , "errorImg": None, "information": None})



# 联合概率矩阵
def JoinMatrix(ans,index):
    index = numpy.array(index)
    index = index.astype(numpy.double)
    fl = 0
    for i in range(len(index)):
        if index[i][0] != -1:
            index[i][len(index[0])-1] = 1.0
            fl += 1
            for j in range(len(index[0])-1):
                # index[i][len(index[0]) - 1] *= ans[j][index[j]][1]
                m = int(index[i][j])
                n = ans[j][m][1]
                index[i][len(index[0]) - 1] *= index[i][len(index[0]) - 1] * n
    resultReturn = [[0 for i in range(index.shape[1])] for i in range(fl)]
    resultReturn = numpy.array(resultReturn)
    resultReturn = resultReturn.astype(numpy.double)
    for i in range(fl) :
        for j in range(len(index[0])):
            resultReturn[i][j] = index[i][j]
    return  resultReturn
#处理请求
def identify():
    # ans = [[[0 for i in range(2)] for i in range(3)] for i in range(6)]
    # print(ans)
    while True:
        task = obj.lpop(requestCache)
        # print(task)
        if(task !=None):
            # print(123)
            try:
                str1 = str(task, encoding="utf-8")
                data = eval(str1)
                category = data["category"].strip()
                imglist = data["img"]
                ip = data["ip"]
                serial = data["serial"].strip()
                key = data["key"].strip()
                proportion = data["proportion"]
                isSucess = True
                ans = [[[0 for i in range(2)] for i in range(int(proportion))]for i in range(len(imglist))]
                # result = [0 for i in range(len(imglist))]
                for i in range(len(imglist)):
                    jResult = mnist_app.application(imglist[i])
                    # print("jResult.tostring()")
                    # print(jResult.tostring())
                    for j in range(int(proportion)):
                        ans[i][j][0] = jResult.matrix[j][0]
                        ans[i][j][1] = jResult.matrix[j][1]

                    obj.set(paramSavePath + ":" + key+":"+ serial+"-"+str(int(round(time.time() * 1000))),jResult.tostring())
                # else:
                #     reg = {
                #         'isSucess': isSucess,
                #         'count': 0,  # 结果总数
                #         'key': key,  # 用户唯一标识
                #         'serial': serial,  # 本次请求的序列号
                #         'time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
                #         'information': jResult.getinformantin()
                #     }
                #     obj.set(resultSavePath+":"+serial,reg)
                # treeUtil.createTree(ans)
                index = [[-1 for i in range(len(imglist)+1)] for i in range(50)]
                isCorrectBlog = True
                 #计算top n 的相等组合
                Calculation.calculation(ans,index)
                if index[0][0] ==-1:
                    isCorrectBlog = False
                if isCorrectBlog == True:
                    #联合概率矩阵
                    resultReturn = JoinMatrix(ans,index)
                    max = resultReturn[0][resultReturn.shape[1]-1]
                    x = 0
                    for i in range(resultReturn.shape[0]):
                          if resultReturn[i][resultReturn.shape[1]-1] > max:
                              max = resultReturn[i][resultReturn.shape[1]-1]
                              x = i
                    print(x)
                    print(max)
                    print(index[x])
                    print(resultReturn[x])
                # 结果保存到redis
                reg = {
                    'isSucess': isSucess,
                    'count': len(ans),  # 结果总数
                    'key': key,  # 用户唯一标识
                    'serial': serial,  # 本次请求的序列号
                    'time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
                    'information': None
                }
                if isCorrectBlog ==True:
                    for i in range(len(ans)):
                        reg["result"+str(i+1)] = ans[i][int(resultReturn[x][i])][0]
                        reg["proportion" + str(i + 1)] = ans[i][int(resultReturn[x][i])][1]
                    reg["accuracy"] = max
                else:
                    for i in range(len(ans)):
                        reg["result"+str(i+1)] = ans[i][0][0]
                        reg["proportion" + str(i + 1)] = ans[i][0][1]
                    reg["accuracy"] = 0
            except:
                serial = data["serial"].strip()
                reg = {
                    'isSucess': 'failed'
                }
            obj.set(resultSavePath+":"+serial,reg)
            #log日记
            logName = time.strftime('%Y.%m', time.localtime(time.time()))
            f = open(logPath + str(logName)+".log", "a+")
            Date = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
            f.write(str(isSucess)+" - - "+ip + " - - [" + Date + "] - - ")
            f.write(jResult.tostring())
            f.write("\n")
            f.close()
if __name__ == '__main__':
    #处理请求
    threading.Thread(target=identify).start()
    #启动flask
    app.run(
        host='0.0.0.0',
        port=5555,
        debug=True)
