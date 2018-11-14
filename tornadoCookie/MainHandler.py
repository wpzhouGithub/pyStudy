# _*_ coding:utf-8 _*_

import  tornado.web
from tornado.httpserver import HTTPServer

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie('mycookie'):
            self.set_secure_cookie('mycookie', 'myvalue')
            self.write('your cookie was not set, and be set new')
        else:
            self.write('your cookie was set')

    def post(self):
        print self.request.body
        if not self.get_secure_cookie('mycookie'):
            self.set_secure_cookie('mycookie', 'myvalue')
            self.write('your cookie was not set, and be set new')
        else:
            self.write('your cookie was set')


def main():
    application = tornado.web.Application(
        [
            (r"/", MainHandler),
        ],
        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__"
    )

    try:
        sockets = tornado.netutil.bind_sockets(7999)

        server = HTTPServer(application)
        server.add_sockets(sockets)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()

main()