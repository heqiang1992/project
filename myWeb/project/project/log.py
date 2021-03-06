#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os, datetime


class logger(object):

    def __open_log(self):
        filePath = os.path.join(os.path.dirname(__file__), 'log.log')
        self.__file_item = open(filePath, "a+")

    def info(self, message):
        self.__open_log()
        time = datetime.datetime.now()
        m = "[ %s ] :" % str(time) + message
        self.__file_item.write(m)
        self.__file_item.close()


def log_info(message, traceback=None):
    filePath = os.path.join(os.path.dirname(__file__), 'log.log')
    file_item = open(filePath, "a+")
    time = datetime.datetime.now()
    m = "[ %s ]	:" % str(time) + str(message) + "\n"
    file_item.write(m)
    if traceback:
        m = "[ %s ]	:" % str(time) + str(traceback) + "\n"
        file_item.write(m)
    file_item.close()
