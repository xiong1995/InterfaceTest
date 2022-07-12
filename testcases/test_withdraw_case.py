"""
体现的前提：登录-->提取token
unittest:
    setup
    setupclass
        提取token并保存为类属性
        提取用户id并保存为类属性

    动态替换参数中的用户id（字符串的replace方法替换）
"""

import unittest
import os
import requests
from jsonpath import jsonpath
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from conf.setting import DATA_DIR, url, test_data, headers
from common.handler_log import log


@ddt
class TestRecharge(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, 'test_recharge.xlsx'), 'withdraw')
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        """用例类的前置方法：登录提取token"""
        # 1.请求登录接口进行登录
        login_url = url + '/member/login'
        params = {
            "mobile_phone": test_data["mobile_phone"],
            "pwd": test_data["pwd"]
        }
        response = requests.post(url=login_url, json=params, headers=headers)
        res = response.json()
        # 2.登录成功后提取token
        token = jsonpath(res, '$..token')[0]
        # 将获取到的token添加到请求头当中
        header = headers
        header['Authorization'] = "Bearer " + token
        # 将含有token的请求头设置为类属性
        cls.header = header
        # setattr(TestRecharge, 'header', header)
        # 提取用户的id给充值接口使用
        cls.member_id = jsonpath(res, '$..id')[0]

    @list_data(cases)
    def test_recharge(self, item):
        # 第一步：准备数据
        # 动态处理需要替换的参数
        recharge_url = url + item['url']
        item['data'] = item['data'].replace('#member_id#', str(self.member_id))
        params = eval(item['data'])
        expected = eval(item['expected'])
        method = item['method'].lower()
        # 第二步：调用接口，获取返回的实际结果
        response = requests.request(method, url=recharge_url, json=params, headers=self.header)
        res = response.json()
        # 第三步：断言
        try:
            self.assertEqual(res['code'], expected['code'])
            self.assertEqual(res['msg'], expected['msg'])
        except AssertionError as e:
            log.error(f"用例---【{item['title']}】---执行失败")
            log.error(e)
        else:
            log.info(f"用例---【{item['title']}】---执行成功")
