# encoding: utf-8
#!usr/bin/python
__author__ = 'admin'

from common.Log import MyLog
from common.OperateExcel import OperateExcel
import requests

class ConfigHttp:

    def __init__(self):
        self.timeout = 8.0
        self.log = MyLog.get_log()
        self.url = None
        self.method = None
        self.params = {}
        self.header = {}
        self.data = {}

    def set_url(self, url):
        self.url = url

    def set_method(self, method):
        self.method = method

    def set_params(self, params):
        self.params = params

    def set_header(self, header):
        self.header = header

    def set_data(self, data):
        self.data = data

    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.header, timeout=float(self.timeout))
            return response
        except:
            self.log.logger.error("time out...")
            return None

    def post(self):
        try:
            response = requests.post(self.url, headers=self.header, data=self.data, timeout=float(self.timeout))
            return response
        except:
            self.log.logger.error("time out...")
            return None





