import unittest
import os
import random
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from common.handler_log import log
from testcases.login import login_check
from common.handle_json import HandleJson
from common.handle_yaml import HandleYaml
from conf.setting import DATA_DIR


@ddt
class TestRegister(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, 'test_recharge.xlsx'), 'register')
    cases = excel.read_data()

    # hj = HandleJson(r'../testdemo/datas/data.json')
    # res_json = hj.read_json()
    # hy = HandleYaml(r'../testdemo/datas/data.yaml')
    # res_yaml = hy.read_yaml()

    @list_data(cases)
    def test_register(self, item):
        # excel存储测试数据使用
        expected = eval(item["expected"])
        params = eval(item["params"])
        if '#mobile#' in item['data']:
            phone = self.random_mobile()
            item['data'] = str(item['data'].replace('#mobile#', phone))
        # yaml,json格式数据驱动
        # expected = item["expected"]
        # params = item["params"]
        row = item["case_id"] + 1
        res = login_check(**params)
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            log.error(f"用例---【{item['title']}】---执行失败")
            log.exception(e)
            self.excel.write_data(row=row, column=5, value="不通过")
            self.excel.bg_color(row=row, column=5, color='FF0000', fill_type='solid')
            raise e
        else:
            log.info(f"用例---【{item['title']}】---执行成功")
            self.excel.write_data(row=row, column=5, value="通过")
            self.excel.bg_color(row=row, column=5, color='FFFFFF', fill_type='none')

    def random_mobile(self):
        """随机生成手机号"""
        mobile = '133'
        # mobile_phone = str(random.randint(13300000000, 13399999999))
        for i in range(8):
            n = str(random.randint(0, 9))
            mobile += n
        return mobile
