# 如何读取yaml文件
import yaml


class HandleYaml:
    def __init__(self, filename):
        self.filename = filename

    def read_yaml(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            res_yaml = yaml.load(stream=f, Loader=yaml.Loader)
        return res_yaml


if __name__ == '__main__':
    hy = HandleYaml(r'D:\workspace\testdemo\datas\data.yaml')
    res = hy.read_yaml()
    print(res, type(res[0]["expected"]))
