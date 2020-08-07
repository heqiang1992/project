#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:heqiang

from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from weixin_robot.app import app   #view manager
from tornado.ioloop import IOLoop

s = HTTPServer(WSGIContainer(app))
s.listen(9903) # 监听 9900 端口
IOLoop.current().start()