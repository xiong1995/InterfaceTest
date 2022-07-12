# import unittest
# from unittestreport import ddt, list_data
# from testdemo.common.handle_excel import HandleExcel
# from testdemo.common.handler_log import log
# from testdemo.testcases.login import login_check
# from testdemo.common.handle_json import HandleJson
#
#
# @ddt
# class TestLogin(unittest.TestCase):
#     excel = HandleExcel(r"../testdemo/datas/test001.xlsx", 'Sheet1')
#     cases = excel.read_data()
#
#     hj = HandleJson(r'../testdemo/datas/data.json')
#     res = hj.read_json()
#
#     @list_data(res)
#     def test_login(self, item):
#         expected = eval(item["expected"])
#         params = eval(item["params"])
#         row = item["case_id"] + 1
#
#         res = login_check(**params)
#         try:
#             self.assertEqual(expected, res)
#         except AssertionError as e:
#             log.error(f"用例【{item['title']}】执行失败")
#             log.exception(e)
#             self.excel.write_data(row=row, column=5, value="不通过")
#             raise e
#         else:
#             log.info(f"用例【{item['title']}】执行成功")
#             self.excel.write_data(row=row, column=5, value="通过")
