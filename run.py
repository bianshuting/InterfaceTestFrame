# encoding: utf-8
#!usr/bin/python
__author__ = 'admin'

from common.HTMLTestRunnerEN2 import HTMLTestRunner
import unittest
import os
import sys
import time
from common import sendMail

if __name__ == '__main__':
    #pro_path = os.path.dirname(os.path.abspath("."))
    #pro_path = sys.path[0]
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find("InterfaceTestDemo")+len("InterfaceTestDemo")]
    print(rootPath)

    test_path = os.path.join(rootPath, "testsuite")
    #print(test_path)
    discover = unittest.defaultTestLoader.discover(test_path, pattern="test*.py")

    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    filename = os.path.join(rootPath, "testresult")+"/"+ now + '_test_result.html'

    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title="Interface AutoTest Frame Demo",
                            description="the result of testcases excute"
                            )
    runner.run(discover)
    fp.close()

    sendMail.send_mail(sendMail.new_report(os.path.join(rootPath, "testresult")))
