
def login_check(username, password):
    """
    登录校验函数
    :param username: 账号
    :param password: 密码
    :return: dict type
    """

    if username != None and password != None:
        if username == 'python35' and password == 'lemonban':
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "登录失败"}
    else:
        return {"code": 1, "msg": "登录失败"}
