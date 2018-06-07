# coding: utf8
import requests
import sys, os
from common import *

reload(sys)
sys.setdefaultencoding('utf-8')


def tds_req():
    """
    tds任务列表
    :return: 任务
    """
    url = "http://10.28.87.30:8080/tds-web/info/queryTestFormByCondition"
    payload = "{\"tester\":\"fp范鹏\",\"pass\":false,\"released\":false,\"orgName\":\"度假研发部\",\"user\":\"fp范鹏\"}"
    headers = {
        'accept': "application/json, text/javascript, */*; q=0.01",
        'origin': "http://ttd.swat.ctripcorp.com:8099",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
        'content-type': "application/json;charset=UTF-8",
        'referer': "http://ttd.swat.ctripcorp.com:8099/",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
    }
    global response
    data = {}
    try:
        response = requests.request("POST", url, data=payload, headers=headers)
        if response.status_code is not 200:
            return {'message': 'error', 'error': response.content}
    except Exception, e:
        print response.status_code, e
        return {'message': 'error', 'error': e}
    for each in response.json()['appliedForm']:
        type = each['formType']
        project_name = each['projectName']
        project_code = each['projectCode']
        affect_app = each['affectAPP']
        affect_api = each['affectAPPAPI']
        submitter = each['submitter']
        submitDate = timestamp2date(each['submitDate'], False)
        releaseETA = timestamp2date(each['releaseETA'], False)
        data[project_name] = {'type': type, 'project_code': project_code, 'affect_app': affect_app,
                              'affect_api': affect_api, 'submitter': submitter, 'submitDate': submitDate,
                              'releaseETA': releaseETA}
    return {'message': 'success', 'data': data}


if __name__ == '__main__':
    print tds_req()
