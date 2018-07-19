from django.shortcuts import render
import os
# Create your views here.
import requests
import unittest
import utils
from utils import *


class ApiTest(unittest.TestCase):

    def run_single_testcase(self, testcase):
        req_kwargs = testcase['request']
        try:
            url = req_kwargs.pop('url')
            method = req_kwargs.pop('method')
        except KeyError:
            raise exception.ParamsError("Params Error")
        resp_obj = requests.request(url=url, method=method, **req_kwargs)
        diff_content = utils.diff_response(resp_obj, testcase['response'])
        success = False if diff_content else True
        return success, diff_content

    def test_run_single_testcase_success(self):
        testcase_file_path = os.path.join(os.getcwd(), 'tests/data/demo.json')
        testcases = utils.load_testcases(testcase_file_path)
        success, _ = self.run_single_testcase(testcases[0])
        self.assertTrue(success)