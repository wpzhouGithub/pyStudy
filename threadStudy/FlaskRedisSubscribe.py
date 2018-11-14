#!/usr/bin/evn python
# _*_ coding:utf-8 _*_

import  redis
import  time
from flask import  Flask
from random import randint

app = Flask(__name__)

rcon = redis.StrictRedis(host='localhost', db=1)
_channel = 'channel'
ps = rcon.pubsub()

def getChannel(user):
    return '%s:%s' % (_channel, user)

@app.route('/get/<user>')
def getMessage(user):
    print 'getMessage'
    channel = getChannel(user)
    print channel
    ps.subscribe(channel)
    for i in ps.listen():
        if i['type'] == 'message':
            return app.make_response(i['data'])

@app.route('/send/<user>')
def sendMessage(user, msg='aaaaaaa'):
    print 'sendMessage'

    channel = getChannel(user)
    msg = msg + str(randint(1,30))
    print msg
    print channel
    r = rcon.publish(channel, msg)
    time.sleep(10)
    print 'r:', r
    return app.make_response(msg)


if __name__ == '__main__':
    app.run(debug=False, threaded=True)
