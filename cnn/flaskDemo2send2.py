from requests import put, get ,post
import os
import json
#发布
from redisHelper import RedisHelper
import uuid
img=['/home/stitp/pictures/0.jpg','/home/stitp/pictures/1.jpg','/home/stitp/pictures/2.jpg']
# img=['C:/Users/asus/Desktop/test/0.png','C:/Users/asus/Desktop/test/1.png','C:/Users/asus/Desktop/test/2.png','C:/Users/asus/Desktop/test/3.png']
score=[12,23,66]

def pri():
    for i in range(1): #10.166.33.86
        list4 = post('http://10.166.33.86:5555/todos',json.dumps(
            {   'img': img,
                'key': '1fengf',
                'score': score,
                'count': len(img),
                'serial':"1fengfAA0011A00*K2"+str(i),
                'category': '1',
                'proportion':'3'
                }))
        print(list4.text)
if __name__ == '__main__':
    pri()