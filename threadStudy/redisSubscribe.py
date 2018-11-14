#！/usr/bin/evn python
# _*_ coding:utf-8 _*_

import  redis
from flask import  Flask, redirect

app = Flask(__name__)
class  Task(object):
    def __init__(self):
        self.rcon = redis.StrictRedis(host='localhost', db=1)
        self.ps = self.rcon.pubsub()
        self.ps.subscribe('channel1')

    def listen_task(self):
        for i in self.ps.listen():
            print('message:', i)
            if i['type'] == 'message':
                print('task get:', i['data'])


if __name__ == '__main__':
    print('listen task channel')
    Task().listen_task()