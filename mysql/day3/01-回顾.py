import pymysql


with pymysql.connect(user='root', password='root',
                     database='advanced', charset='utf8') as conn:
    cursor = conn.cursor()
    cursor.close()