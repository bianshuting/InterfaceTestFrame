# encoding: utf-8
#!usr/bin/python
__author__ = 'admin'

import os
import logging
import threading
import time

class Log:
    def __init__(self):
        global logpath, resultpath, prodir
        curPath = os.path.abspath(os.path.dirname(__file__))
        rootPath = curPath[:curPath.find("InterfaceTestDemo\\")+len("InterfaceTestDemo\\")]

        resultpath = os.path.join(rootPath, "testresult")
        if not os.path.exists(resultpath):
            os.mkdir(resultpath)

        now = time.strftime("%Y-%m-%d-%H-%M-%S")
        filename = os.path.join(rootPath, "testresult")+"/"+ now + '_output.log'

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        handler = logging.FileHandler(filename)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler.setFormatter(formatter)
        self.logger.addHandler(handler)


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log



if __name__ == '__main__':
    MyLog.get_log()
