import logging
from conf.setting import log


def create_log(
        name=log['name'],
        level=log["level"],
        filename=log['filename'],
        sh_level=log['sh_level'],
        fh_level=log['fh_level']
):
    # 创建日志收集器并设置收集等级
    log = logging.getLogger(name)
    log.setLevel(level)
    # 创建日志输出渠道并设置输出等级
    # 1.输出到控制台
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    log.addHandler(sh)
    # 2.输出到文件
    fh = logging.FileHandler(filename, encoding='utf8')
    fh.setLevel(fh_level)
    log.addHandler(fh)
    # 设置日志输出格式并绑定到输出渠道
    formats = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
    log_format = logging.Formatter(formats)
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)

    return log


log = create_log()
