# coding:utf8

import datetime
import ConfigParser
import MySQLdb
import os
import requests
import json
import time
from xml.etree import ElementTree
import suds
import cgi
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def send_mail(sender_str, sender_name_str, subject_str, content_str, recipients, cc):
    """
    发送邮件，带抄送
    :param sender_str: 发送人
    :param sender_name_str: 发送邮件名
    :param subject_str: 主题
    :param content_str: 内容
    :param recipients: 收件人
    :param cc: 抄送人
    :return:
    """
    print u"发送邮件至" + str(recipients) + u",主题：" + subject_str
    if recipients:
        recipients_str = ""
        for recipient in recipients:
            recipients_str += (recipient + ",")

        cc_str = ""
        for each in cc:
            cc_str += (each + ",")

        request = ElementTree.Element("Request")

        header = ElementTree.SubElement(request, "Header")
        header.set("UserID", "910880")
        header.set("RequestType", "Commu.Message.SendMailOther")

        mail_other_request = ElementTree.SubElement(request, "MailOtherRequest")

        order_id = ElementTree.SubElement(mail_other_request, "Orderid")

        uid = ElementTree.SubElement(mail_other_request, "Uid")
        uid.text = "SOA"

        source_id = ElementTree.SubElement(mail_other_request, "SourceID")
        source_id.text = "1"

        business_type = ElementTree.SubElement(mail_other_request, "BusinessType")
        business_type.text = "flight"

        module_type = ElementTree.SubElement(mail_other_request, "ModuleType")
        module_type.text = "book"

        eid = ElementTree.SubElement(mail_other_request, "Eid")

        sender = ElementTree.SubElement(mail_other_request, "Sender")
        sender.text = sender_str

        recipient = ElementTree.SubElement(mail_other_request, "Recipient")
        recipient.text = recipients_str[:-1]

        cc = ElementTree.SubElement(mail_other_request, "Cc")
        cc.text = cc_str[:-1]

        bcc = ElementTree.SubElement(mail_other_request, "Bcc")
        # bcc.text = recipients_str[:-1]

        sender_name = ElementTree.SubElement(mail_other_request, "SenderName")
        sender_name.text = sender_name_str

        recipient_name = ElementTree.SubElement(mail_other_request, "RecipientName")
        # recipient_name.text = recipients_str[:-1]

        subject = ElementTree.SubElement(mail_other_request, "Subject")
        subject.text = subject_str

        body_template_id = ElementTree.SubElement(mail_other_request, "BodyTemplateID")
        body_template_id.text = "4"

        body_content = ElementTree.SubElement(mail_other_request, "BodyContent")
        body_content.text = "<entry><content><![CDATA[" + content_str + "</br></br></br></br></br></br></br></br></br></br></br></br>]]></content></entry>"

        importance = ElementTree.SubElement(mail_other_request, "Importance")
        importance.text = "2"

        content_type = ElementTree.SubElement(mail_other_request, "ContentType")
        content_type.text = "text/html"

        charset = ElementTree.SubElement(mail_other_request, "Charset")
        charset.text = "GB2312"

        deadline_time = ElementTree.SubElement(mail_other_request, "DeadlineTime")
        deadline_time.text = "2020-04-06T12:59:57.1034847+08:00"

        s_chedule_time = ElementTree.SubElement(mail_other_request, "ScheduleTime")

        request_xml = "<?xml version=\"1.0\"?>" + ElementTree.tostring(request, "utf-8")

        # 调用wcf邮件接口
        url = "http://soa.uat.qa.nt.ctripcorp.com/SOA.ESB/Ctrip.SOA.ESB.asmx?WSDL"
        client = suds.client.Client(url)
        response_xml = client.service.Request(cgi.escape(request_xml))
        parsed = ElementTree.XML(response_xml)
        header = parsed.findall("Header")
        if header[0].attrib.get("ResultCode") == "Success":
            print u"邮件发送成功！"
        else:
            print u"邮件发送失败，请稍后再试！"
            message = '<h1>度假页面性能优化告警<font color="red">发送失败</font></h1>' + content_str
            send_mail("page&server_alert@ctrip.com", u'度假页面性能优化告警发送失败', u'度假页面性能优化告警发送失败', message, ['fanp@ctrip.com'],
                      ['fanp@ctrip.com'])


class DB(object):
    """
    数据库操作
    """
    def __init__(self):
        self.db_con = self.__conDb()

    def __conDb(self):
        conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='root', db='testplatformdb',charset="utf8")
        cur = conn.cursor(MySQLdb.cursors.DictCursor)
        return conn, cur

    def discon(self, cur, conn):
        cur.close()
        conn.close()

    def query_sql(self, sql, arg=None):
        conn, cursor = self.__conDb()
        cursor.execute(sql, arg)
        data = cursor.fetchall()
        self.discon(cursor, conn)
        return data

    def execute_sql(self, sql, arg=None):
        conn, cursor = self.__conDb()
        cursor.execute(sql, arg)
        conn.commit()
        self.discon(cursor, conn)


def search_timestamp(days=1):
    """
    查询日期
    :param days: 默认是昨天
    :return: 时间戳
    """
    # 今天日期
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=days)
    yesterday_start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
    # 昨天结束时间戳
    yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1
    return yesterday_start_time, yesterday_end_time


def search_date(day=1):
    """
    查询日期
    :param day: 默认昨天
    :return: 日期格式
    """
    now = datetime.datetime.now()
    end_time = datetime.date(year=now.year, month=now.month, day=now.day)
    start_time = end_time - datetime.timedelta(day)
    end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")
    start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
    return str(start_time), str(end_time)


def display_worker_info(worker_name):
    """
    报错信息
    :param worker_name:
    :return:
    """

    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            print worker_name
            if args:
                print u"参数：",
                for arg in args:
                    print arg,
                print "\n"
            if kwargs:
                print u"参数："
                for key in kwargs:
                    print key + ":" + kwargs[key],
                print "\n"
            print u"开始执行..."
            try:
                func(*args, **kwargs)
            except Exception, e:
                print(e.message)
                message = u"任务调度失败<br>"
                message += u"任务名称：" + worker_name + u"<br>"
                message += u"错误信息：" + str(e) + u"<br>"
                send_mail("WebTestPlatForm-Worker@ctrip.com", u"团队游测试平台-任务调度", u"任务调度失败通知", message, ['fanp@ctrip.com'],
                          ['fanp@ctrip.com'])
                raise e
            print u"执行完毕...\n"

        return wrapper2

    return wrapper1


class HttpReq:
    def __init__(self, url, params, data, headers, method):
        self.response = self.run_main(url, params, data, headers, method)

    def send_post(self, url, data, headers):
        response = requests.post(url=url, data=data, headers=headers).json()
        # return json.dumps(response,sort_keys=True,indent=4)
        return response

    def send_get(self, url, params, headers):
        response = requests.get(url=url, params=params, headers=headers).json()
        # return json.dumps(response,sort_keys=True,indent=4)
        return response

    def run_main(self, url, params, data, headers, method):
        respose = None
        if method == 'GET':
            respose = self.send_get(url, params, headers)
        else:
            respose = self.send_post(url, data, headers)
        return respose


def timestamp2date(timestamp, hastime=True):
    """
    时间戳转日期(处理13和10位时间戳)
    :param timestamp:
    :param hastime:default True
    :return:
    """
    if len(str(timestamp)) == 13:
        timestamp = timestamp/1000
    timeArray = time.localtime(timestamp)
    if hastime:
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    else:
        otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    return otherStyleTime


if __name__ == '__main__':
    url = 'https://...'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    run = HttpReq(url, params=None, data=None, headers=headers, method='POST')
    print(run.response)
