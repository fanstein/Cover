from __future__ import print_function
from django.shortcuts import render
import os
# Create your views here.
import requests
import unittest
import utils
from utils import *


class ApiTest(object):

    def run_single_testcase(self, testcase):
        req_kwargs = testcase['request']
        try:
            url = req_kwargs.pop('url')
            method = req_kwargs.pop('method')
        except KeyError:
            raise ParamException.paramError("Params Error")
        resp_obj = requests.request(url=url, method=method, **req_kwargs)
        diff_content = utils.diff_response(resp_obj, testcase['response'])
        success = False if diff_content else True
        return success, diff_content

    def test_run_single_testcase_success(self):
        testcase_file_path = os.path.join(os.getcwd(), 'cases/case.json')
        testcases = utils.load_testcases(testcase_file_path)
        success, _ = self.run_single_testcase(testcases)
        print(success)


if __name__ == '__main__':
    ApiTest().test_run_single_testcase_success()