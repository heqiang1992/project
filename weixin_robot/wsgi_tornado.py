#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:heqiang

from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from weixin_robot.app import app  # view manager
from tornado.ioloop import IOLoop

s = HTTPServer(WSGIContainer(app))
s.listen(9903)  # 监听 9900 端口
IOLoop.current().start()

"""
        location / {
            proxy_pass http://localhost:5000;    
            
            
        }
        #关键一点就是这里，意思是所有对http://www.abc.com:80的访问都会重定向到本机的５０００端口上
"""
