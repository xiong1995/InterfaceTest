# 如何操作json格式文件
import json


# json数据为空 null     -->python:None
# json数据为真 true     -->python:True
# json数据为假 false    -->python:False
class HandleJson:

    def __init__(self, filename):
        self.filename = filename

    def read_json(self):
        with open(self.filename, 'r', encoding='utf8') as f:
            res_json = json.load(f)
        # json_python = json.loads(res_json)
        return res_json


if __name__ == '__main__':
    hj = HandleJson('../datas/data.json')
    res = hj.read_json()
    a = res[0]['params']
    print(type(a))
