#!/usr/bin/env Python
# coding=utf-8
import os
import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web

from tornado.options import define,options
from handlers.index import IndexHandler

define('port',default=8000,help='run on teh given port',type=int)

url=[
    (r'/',IndexHandler),
]

settings=dict(
    cookie_secret='MKrZSaIMREmjZnHskwmqi0k06xrjs0QQg48xhOYAW2o=',
    template_path=os.path.join(os.path.dirname(__file__),'templates'),
    # static_path=os.path.join(os.path.dirname(__file__),'static')
)

application=tornado.web.Application(
    handlers=url,
    **settings,
    debug=True
)

def main():
    tornado.options.parse_command_line()
    http_server=tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print('Development server is running at http://127.0.0.1:%s'% options.port)
    print('Quit the server with Control-C')
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()

