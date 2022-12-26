import pymysql
from datetime import datetime


class News:

    def __init__(self):
        # 准备数据库连接对象
        self.conn = pymysql.connect(user='root', password='root', database='advanced', charset='utf8')
        # 准备游标对象
        self.cursor = self.conn.cursor()

    def add_five_data(self):
        """一次性添加5条记录"""
        try:
            for i in range(2, 7):
                sql = f"INSERT INTO news(id, title, author, content, post_time, clicks) " \
                      f"values ({i}, 'title{str(i)}', 'author{str(i)}', 'content{str(i)}', '{datetime.now()}', {i})"
                self.cursor.execute(sql)
        except Exception as e:
            print(f'提交失败:{e}')
            self.conn.rollback()
        else:
            print('提交成功')
            self.conn.commit()

    def del_by_title(self):
        """根据用户输入的标题删除记录"""
        # 接收用户输入的标题
        title = input('标题：')
        try:
            sql = f'DELETE FROM news WHERE title = "{title}"'
            rows = self.cursor.execute(sql)
            self.conn.commit()
            if rows:
                print('删除成功')
            else:
                print('删除失败')
        except Exception as e:
            print('删除失败')
            self.conn.rollback()

    def __del__(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    news = News()
    # news.add_five_data()
    news.del_by_title()
