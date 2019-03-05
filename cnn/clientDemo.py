#!/usr/bin/env python
# -*- coding:utf-8 -*-

from requests import post
import threading
#订阅
from redisHelper import RedisHelper

# 客户端Demo
# 1、server url：10.166.33.86:5000/todos
#
# 2、请求参数'url': '/home/stitp/pictures/'+str(i)+'.jpg',   图片路径，在/home/stitp/pictures/有20张测试图片（0.jpg--19.jpg）
#         'key': userID+'_'+str(i),   用户唯一标识+'_'+图片序列号
#         'category': '1'      请求神经网络类别 目前设置为1，表示识别数字0-19
#
# 3、请求完成会得到服务器的响应信息。
# 信息示例： {'status': 'succeed', 'key': '45WFEQ6_0', 'url': '/home/stitp/pictures/0.jpg'}
#            {'status': 'failed', 'key': '45WFEQ6_21', 'url': '/home/stitp/pictures/21.jpg', 'information': 'file not found'}
#
# 4、识别结果接收：
#     redis 订阅channel为userID的频道
# 接收信息示例为：[b'message', b'45WFEQ6', b"{'isSucess': 'true', 'result1': 1, 'result2': 7, 'result3': 3, 'key': '45WFEQ6_7', 'category': '1', 'information': None, 'url': '/home/stitp/pictures/7.jpg'}"]



# ip = '10.166.33.86' # server ip
ip = 'mini1'
userID = '45WFEQ6'  # 用户唯一标识，识别结果返回channel名

# 接受结果
def receive():
    obj = RedisHelper(ip)  # 设置redis的ip
    obj.setchannl(userID)  # 设置订阅频道
    redis_sub = obj.subscribe()  # 调用订阅方法

    # 接收结果
    while True:
        msg= redis_sub.parse_response()
        print ("识别结果：",msg)



def send():
    # 新加任务
    for i in range(22):
        info = post('http://'+ip+':5000/todos',
                     data={'url': '/home/stitp/pictures/'+str(i)+'.jpg',
                           'key': userID+'_'+str(i),
                           'category': '1'
                        }).json()
        print("发送提示：",info)

if __name__ == '__main__':
    # 处理请求
    threading.Thread(target=send).start()
    # 接收
    receive()
