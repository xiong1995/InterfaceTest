import re
from common.handle_ini import ConfigHandle


def replace_data(data, cls):
    """
    替换数据的方法
    :param data: 要进行替换的数据
    :param cls: 测试类
    :return: str
    """
    while re.search('#(.*?)#', data):
        res = re.search('#(.*?)#', data)
        # item = res.group()
        # attr = res.group(1)
        # value = getattr(cls, attr)
        # data = data.replace(item, str(value))
        try:
            data = data.replace(res.group(), str(getattr(cls, res.group(1))))
        # data = data.sub('#(.*?)#', getattr(cls, res.group(1)), data, count=1)
        except AttributeError as e:
            # 类属性中没有就到配置文件中找
            data = data.replace(res.group(), str(getattr(cls, res.group(1))))
    return data
