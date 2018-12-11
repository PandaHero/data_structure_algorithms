#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/9 16:40
@Author  : TianCi
@File    : test.py
@Software: PyCharm
@desc:
"""
# import mechanicalsoup  # 导入模块
#
# browser = mechanicalsoup.StatefulBrowser()
# browser.open("http://httpbin.org/")
# browser.follow_link("forms")
# # print(browser.get_url())
# # print(browser.get_current_page())
# # 获取需要提交表单位置(css选择器)
# browser.select_form('form[action="/post"]')
# # print(browser.get_current_form())
# # print(browser.get_current_form().print_summary())
# # 填写表单
# browser["custname"] = "Me"
# browser["custtel"] = "00000001"
# browser["custemail"] = "hahaha@.163.com"
# browser["size"] = "medium"
# browser["topping"] = "bacon"
# # browser.launch_browser()  # 启动一个真实的浏览器访问
# response = browser.submit_selected()
# print(response.text)
import time
from urllib.parse import urlencode

import requests


class Message(object):
    # 登陆url
    params = urlencode({"action": "loginIn", "name": "s-kf0zbuur", "password": "zh953218"})
    login_url = "http://api.ndd001.com/do.php?%s" % params
    # 用户信息url
    user_info_url = "http://api.ndd001.com/do.php?action=getSummary&token="
    projectID = "13828"
    count = 0

    def login(self):
        # 发送登陆请求，获取登陆后的token
        login_req = requests.get(self.login_url)
        token = login_req.text.split("|")[-1]
        return token

    def get_user_info(self, token):
        user_req = requests.get(self.user_info_url + str(token))
        return user_req.text

    def get_phone_number(self, token):
        # 获取手机号
        phone_url = "http://api.ndd001.com/do.php?action=getPhone&sid=" + str(self.projectID) + "&token=" + str(token)
        print(phone_url)
        req = requests.get(phone_url)
        if "0" == req.text.split("|")[0]:
            time.sleep(3)
            self.get_phone_number(token)
        else:
            print(req.text.split("|")[-1])
            return req.text.split("|")[-1]

    def get_phone_message(self, token, phone_number):
        # 等待3秒获取手机短信验证码
        time.sleep(10)
        phone_message_url = "http://api.ndd001.com/do.php?action=getMessage&sid=" + str(
            self.projectID) + "&phone=" + str(phone_number) + "&token=" + str(token)
        print(phone_message_url)
        req = requests.get(phone_message_url)
        if "没有接收" in req.text:
            # print(req.text, self.count)
            # time.sleep(3)
            # self.count += 1
            # if self.count < 2:
            #     self.get_phone_message(token, phone_number)
            # else:
            #     print("获取验证码请求次数超过最大值")
            #     self.count = 0
            #     self.add_black_list(token, phone_number)
            #     self.cancel_recv_list(token, phone_number)
            #     # number = self.get_phone_number(token)
            #     # self.get_phone_message(token, number)
            return 0

        else:
            # message = str(req.text.split("。")[0])[-6:]
            print("验证码是", str(req.text.split("。")[0])[-6:])
            return str(req.text.split("。")[0])[-6:]

    # 获取验证码失败，手机号加入黑名单
    def add_black_list(self, token, phone_number):
        add_black_url = "http://api.ndd001.com/do.php?action=addBlacklist&sid=" + str(
            self.projectID) + "&phone=" + str(phone_number) + "&token=" + str(token)
        requests.get(add_black_url)

    # 获取验证码失败，释放手机号
    def cancel_recv_list(self, token, phone_number):
        add_black_url = "http://api.ndd001.com/do.php?action=cancelRecv&sid=" + str(
            self.projectID) + "&phone=" + str(phone_number) + "&token=" + str(token)
        requests.get(add_black_url)


if __name__ == '__main__':
    mes = Message()
    token = mes.login()
    phone = mes.get_phone_number(token)
    # print(phone)
    message = mes.get_phone_message(token, phone)
    print(phone, message)
