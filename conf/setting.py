import os
import time


# 项目根目录的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用例数据所在目录
DATA_DIR = os.path.join(BASE_DIR, 'datas')

# 配置文件所在目录
CONF_DIR = os.path.join(BASE_DIR, 'conf')

# 日志文件所在目录
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 报告文件所在目录
REPORT_DIR = os.path.join(BASE_DIR, 'reports')

# 用例模块所在目录
CASES_DIR = os.path.join(BASE_DIR, 'testcases')

# 日志配置
log = {
    'name': 'mylog',
    'level': 'DEBUG',
    'filename': os.path.join(LOG_DIR, time.strftime("%Y-%m-%d") + '.log'),
    'sh_level': 'DEBUG',
    'fh_level': 'DEBUG',
}

# 测试报告配置
# filename: 测试报告文件名
# report_dir: 测试报告存放路径
# title: 测试报告标题
# tester: 测试人员
# desc: 项目名称
# templates: 测试报告模板，可选模板：1,2,3
report_conf = {
    "filename": time.strftime("%Y-%m-%d") + ".html",
    "report_dir": REPORT_DIR,
    "title": "演示用例运行产生的测试报告",
    "tester": "XXX",
    "desc": "XX项目测试报告",
    "templates": 2
}

url = 'http://api.lemonban.com/futureloan'
headers = {
    "X-Lemonban-Meida-Type": "lemonban.v2"
}
test_data = {
    "mobile": "13357824562",
    "pwd": "lemonban"
}

mysql = {
    "host": "api.lemonban.com",
    "post": "3306",
    "user": "future",
    "pwd": "123456",
    "database": "futureloan"
}

if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d"))
