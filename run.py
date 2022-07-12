import unittest
from unittestreport import TestRunner
from conf.setting import report_conf
from unittestreport.core.sendEmail import SendEmail     # 自定义邮件内容

suite = unittest.defaultTestLoader.discover(r'testcases')
runner = TestRunner(suite,
                    filename=report_conf['filename'],
                    report_dir=report_conf['report_dir'],
                    title=report_conf['title'],
                    tester=report_conf['tester'],
                    desc=report_conf['desc'],   # 描述
                    templates=report_conf['templates']
                    )
runner.run()
runner.send_email(
    host='smtp.163.com',
    port=465,
    user='18379262295@163.com',
    password='HBALUJQIWWSRPDZU',
    to_addrs='18379262295@163.com',
    is_file=True
)
# 自定义邮件内容
# se = SendEmail(host='smtp.163.com',
#                port=465,
#                user='18379262295@163.com',
#                password='xjj19951121.')
# se.send_email(subject='邮件主题',
#               content='邮件内容',
#               filename='邮件附件',
#               to_addrs='18379262295@163.com')
