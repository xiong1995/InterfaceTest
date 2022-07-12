import pymysql


class HandleMySQL:
    def __init__(self, host, port, user, password, database):
        # 连接数据库
        self.con = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset='utf8',
            # cursorclass=pymysql.cursors.DictCursor  # 设置游标类型，默认为元组，这里设置为字典类型
        )

    def find_one(self, sql):
        with self.con as cur:
            cur.execute(sql)
        res = cur.fetchone()
        cur.close()
        return res

    def find_all(self, sql):
        with self.con as cur:
            cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    def find_count(self, sql):
        with self.con as cur:
            res = cur.execute(sql)
        cur.close()
        return res

    # def __del__(self):
    #     self.con.close()
# # 创建游标
# cur = con.cursor()
# # sql语句
# sql = 'SELECT leave_amount FROM member WHERE mobile_phone="13357824562";'
# # 执行sql语句
# cur.execute(sql)
# res = cur.fetchall()
# print(res)
# # con.commit()    # 提交事务
# # with con as cur:
# #     sql = ""
# #     cur.execute(sql)
# cur.close()
# con.close()
# print(res)
