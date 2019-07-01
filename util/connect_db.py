import json
import pymysql.cursors


class OperationMysql:
    def __init__(self):
        self.conn = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='henry',
            db='test3',
            charset='utf8',
            cursorclass = pymysql.cursors.DictCursor
        )
        #可能需要返回字典
        # 获取游标
        self.cur = self.conn.cursor()

    def search_one(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        result = json.dumps(result)
        return result


if __name__ == "__main__":
    op_mysql = OperationMysql()
    res = op_mysql.search_one("select * from web_user")
    print(res)