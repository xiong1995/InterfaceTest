from configparser import ConfigParser


class ConfigHandle(ConfigParser):

    def __init__(self, conf_file):
        super().__init__()
        self.read(conf_file, encoding='utf8')

    # # 第一步创建配置文件的解析器对象
    # cp = ConfigParser()
    # # 第二步读取配置文件中的内容到配置文件解析器中
    # cp.read('./testdemo/config.ini', encoding='utf8')
    # # 第三步读取配置内容
    # # 方法一：使用get方法读取配置内容，读取内容为字符串格式
    # res = cp.get('logging', 'filename')
    # print(res, type(res))
    # #
    def get_logging(self, key):
        return ConfigParser.get(self, "logging", key)

    def get_mysql(self, key):
        return ConfigParser.get(self, 'mysql', key)

    def get_data(self, key):
        return ConfigParser.get(self, 'datas', key)
