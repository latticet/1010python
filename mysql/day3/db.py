import pymysql

"""
类名： DB
方法：
    __init__:
        数据库对象
        游标对象
    read: 查询
    write：增删改
    __del__:
        关闭游标对象
        关闭数据库对象
"""


class DB:
    def __init__(self, user, password, database,
                 host='localhost', port=3306,
                 charset='utf8', cursor_type=pymysql.cursors.Cursor):
        # 初始化数据库连接对象和游标对象
        self.conn = pymysql.connect(host=host, port=port,
                                    user=user, password=password,
                                    database=database, charset=charset)
        self.cursor = self.conn.cursor(cursor_type)
        """
        if cursor_type == pymysql.cursors.Cursor:
            self.result_data = ()
        else:
            self.result_data = []
        """
        self.result_data = () if cursor_type == pymysql.cursors.Cursor else []

    def read(self, sql, args=None):
        """查询操作"""
        try:
            # 执行sql语句
            rows = self.cursor.execute(sql, args=args)
            # 获取结果集
            data = self.cursor.fetchall()
        except Exception as e:
            return 0, self.result_data
        else:
            return rows, data

    def write(self, sql, args=None):
        """写入操作"""
        try:
            # 执行sql语句
            rows = self.cursor.execute(sql, args)
        except Exception as e:
            print(e)
            self.conn.rollback()
            return 0
        else:
            self.conn.commit()
            return rows

    def __del__(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    db = DB('root', 'root', 'advanced')

    # 查询
    print(db.read('select * from student where stu_name = %s', ['曹操']))

    # 写入
    rows = db.write('delete from student where stu_name = %s', ['李严'])
    print(rows)

    if rows:
        print('OK')
    else:
        print('Fail')
