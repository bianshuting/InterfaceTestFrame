# encoding: utf-8
#!usr/bin/python
__author__ = 'admin'
import unittest
from common.Log import MyLog
from common.OperateExcel import OperateExcel
from common.configHTTP import ConfigHttp

class test_request_frontaddress(unittest.TestCase):
    def setUp(self):
        self.log = MyLog.get_log()

    def tearDown(self):
        pass

    def test_request_frontaddress(self):
        self.log.logger.info("读取请求数据...")
        read_excel = OperateExcel("request_QD")
        req_url = read_excel.getUrlBySheet()
        req_method = read_excel.getMethodBySheet()
        req_params = read_excel.getParamsBySheet()
        req_header = read_excel.getHeaderBySheet()

        config_http = ConfigHttp()
        config_http.set_url(req_url)
        config_http.set_method(req_method)
        config_http.set_params(req_params)
        config_http.set_header(req_header)
        res = config_http.get()
        if res != None:
            #print(res.json())
            print(res.text)
        else:
            print("res is None")




if __name__ == '__main__':
    unittest.main()


